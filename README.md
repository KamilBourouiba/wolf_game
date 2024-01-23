Simulation Game README
This Python script simulates a simple game between Wolves and Villagers. The game involves rounds of voting and wolf attacks until one group (Wolves or Villagers) emerges victorious. The simulation is run for a specified number of iterations to observe the outcome trends.

How to Use
Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Run the script:

bash
Copy code
python simulation_game.py
Follow the prompts to input the simulation parameters:

How many iterations do you want to simulate?: Number of times the game simulation will run.
How many wolves do you want?: Number of wolf players in each round.
How many villagers do you want?: Number of villager players in each round.
Observe the simulation progress and results.

Code Structure
The script is organized into functions for better readability and modularity:

make_the_pool(players): Counts the occurrences of Wolves and Villagers in the player pool.
vote(players): Generates random votes for each player.
kill_someone(players): Determines a Villager to be killed by Wolves.
vote_someone(players): Conducts voting and eliminates the most voted player if there is a clear choice.
play_game(wolf, villager): Main function to execute the game for a specified number of rounds.
simulate_game(iterations, wolf, villager): Runs the game simulation for the specified number of iterations.
Simulation Progress
During the simulation, the progress is displayed as a progress bar indicating the percentage of completion.

Simulation Results
After completing all iterations, the script displays the following results:

Number of times Villagers win.
Number of times Wolves win.
Contributing
Feel free to contribute to the project by submitting issues or pull requests.

License
This project is licensed under the MIT License.
