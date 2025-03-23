# Virus Spread Simulation

This is a simple simulation of virus transmission among a population, incorporating factors like vaccination, mask usage, recovery, and reinfection. The simulation uses a random walk model where individuals move around the screen, and the virus spreads based on proximity and certain probabilities. The program visualizes infected, recovered, vaccinated, and masked individuals in different colors, and allows toggling for vaccination and mask mandates.

### Features:
- **Virus Spread**: The virus spreads when an infected individual comes within a certain radius of a healthy person. 
- **Vaccination**: The vaccination reduces the probability of getting infected.
- **Masks**: Individuals wearing masks have a lower probability of transmitting the virus.
- **Recovery**: Infected individuals recover after a set period, after which they can be reinfected.
- **Reinfection**: Recovered individuals have a chance to become reinfected after a certain period.
- **Statistics**: At the end of the simulation, the number of infected, healthy, and recovered individuals is displayed.

### Controls:
- **`M`**: Toggle mask mandate. All individuals will start wearing masks if enabled.
- **`V`**: Toggle vaccination drive. A portion of the population will be vaccinated if enabled.

### Requirements:
- Python 3.x
- `pygame` for the simulation graphics
- `matplotlib` for generating the statistical plot at the end

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/bistcuite/virus-spread-simulation
   ```
2. Install the required dependencies:
   ```bash
   pip install pygame matplotlib
   ```
3. Run the simulation:
   ```bash
   python virus_simulation.py
   ```

### How it Works:
The simulation starts with a population of individuals on the screen. Initially, one individual is infected. The individuals move randomly within the boundaries of the screen. When an infected individual comes close to a healthy person, the virus may spread, depending on several factors like vaccination and mask usage.

Once infected individuals recover, they will still be able to transmit the virus for a period before they stop being contagious. If they become reinfected after recovery, they will be able to spread the virus again.

### Visualization:
- **Red**: Infected individuals
- **Green**: Healthy individuals
- **Blue**: Vaccinated individuals
- **Gray**: Masked individuals
- **Black**: Recovered individuals

### Statistical Outputs:
At the end of the simulation (when the user exits), the following statistics will be displayed:
- **Infected**: The number of individuals currently infected.
- **Healthy**: The number of individuals who are not infected and not recovered.
- **Recovered**: The number of individuals who have recovered from the virus.

### Example Output:
When the simulation finishes, you will see:
- The number of infected individuals.
- The number of healthy individuals.
- The number of recovered individuals.

### License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
