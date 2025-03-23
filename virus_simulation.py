import pygame
import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
POPULATION = 200
INFECTION_RADIUS = 10
INFECTION_PROBABILITY = 0.1
RECOVERY_TIME = 500
VACCINATION_RATE = 0.7
MASK_EFFECTIVENESS = 0.5
STEP_SIZE = 7  # Step size for random walk
REINFECTION_PROBABILITY = 0.05  # Lower probability for reinfection
CARRIER_TIME = 300  # Time they remain carriers
MAX_SIMULATION_TIME = 10000  # Max simulation time steps

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virus Spread Simulation")

class Person:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.infected = False
        self.recovery_timer = 0
        self.vaccinated = False
        self.masked = False
        self.recovered = False
        self.carrier_time = 0
        self.mask_wearing = random.random() < 0.5  # Randomly assign mask wearers

    def move(self):
        angle = random.uniform(0, 2 * math.pi)
        self.x += STEP_SIZE * math.cos(angle)
        self.y += STEP_SIZE * math.sin(angle)

        if self.x <= 0 or self.x >= WIDTH:
            self.x = max(0, min(WIDTH, self.x - STEP_SIZE * math.cos(angle)))
        if self.y <= 0 or self.y >= HEIGHT:
            self.y = max(0, min(HEIGHT, self.y - STEP_SIZE * math.sin(angle)))

    def draw(self):
        color = RED if self.infected else (BLUE if self.vaccinated else (GRAY if self.mask_wearing else (BLACK if self.recovered else GREEN)))
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)

    def update(self, people):
        if self.infected:
            self.recovery_timer += 1
            if self.recovery_timer > RECOVERY_TIME:
                self.infected = False
                self.recovered = True
                self.recovery_timer = 0

            for person in people:
                if not person.infected and not person.vaccinated and not person.recovered:
                    distance = ((self.x - person.x) ** 2 + (self.y - person.y) ** 2) ** 0.5
                    if distance < INFECTION_RADIUS:
                        probability = INFECTION_PROBABILITY * (1 - MASK_EFFECTIVENESS if person.mask_wearing else 1)
                        if random.random() < probability:
                            person.infected = True
        elif self.recovered and self.carrier_time < CARRIER_TIME:
            self.carrier_time += 1
            for person in people:
                if not person.infected and not person.vaccinated and not person.recovered:
                    distance = ((self.x - person.x) ** 2 + (self.y - person.y) ** 2) ** 0.5
                    if distance < INFECTION_RADIUS:
                        probability = INFECTION_PROBABILITY * (1 - MASK_EFFECTIVENESS if person.mask_wearing else 1) * 0.5  # Lower chance of infecting
                        if random.random() < probability:
                            person.infected = True
        elif self.recovered and random.random() < REINFECTION_PROBABILITY:
            self.infected = True
            self.recovered = False
            self.carrier_time = 0

def draw_stats(people):
    infected_count = sum(1 for p in people if p.infected)
    healthy_count = sum(1 for p in people if not p.infected and not p.recovered and not p.vaccinated)
    recovered_count = sum(1 for p in people if p.recovered)
    carrier_count = sum(1 for p in people if p.recovered and p.carrier_time > 0)

    font = pygame.font.SysFont(None, 24)
    text_surface = font.render(f"Infected: {infected_count}  Healthy: {healthy_count}  Recovered: {recovered_count}  Carriers: {carrier_count}", True, BLACK)
    screen.blit(text_surface, (10, 10))

def plot_stats(infected_counts, healthy_counts, recovered_counts):
    # Plotting the statistics over time
    plt.figure(figsize=(10, 6))
    plt.plot(infected_counts, label="Infected")
    plt.plot(healthy_counts, label="Healthy")
    plt.plot(recovered_counts, label="Recovered")
    plt.xlabel('Time (Steps)')
    plt.ylabel('Population')
    plt.legend()
    plt.title('Virus Spread Simulation Over Time')
    plt.show()

people = [Person() for _ in range(POPULATION)]
people[0].infected = True  # Start with one infected person

running = True
mask_mandate = False
vaccination_drive = False

infected_counts = []
healthy_counts = []
recovered_counts = []

for t in range(MAX_SIMULATION_TIME):
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                mask_mandate = not mask_mandate
                for person in people:
                    person.mask_wearing = mask_mandate
            elif event.key == pygame.K_v:
                vaccination_drive = not vaccination_drive
                if vaccination_drive:
                    for person in people:
                        if random.random() < VACCINATION_RATE:
                            person.vaccinated = True

    for person in people:
        person.move()
        person.update(people)
        person.draw()

    draw_stats(people)

    infected_counts.append(sum(1 for p in people if p.infected))
    healthy_counts.append(sum(1 for p in people if not p.infected and not p.recovered and not p.vaccinated))
    recovered_counts.append(sum(1 for p in people if p.recovered))

    pygame.display.flip()
    pygame.time.delay(30)

plot_stats(infected_counts, healthy_counts, recovered_counts)
pygame.quit()
