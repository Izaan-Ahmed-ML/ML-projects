# Rock Paper Scissors

This was the boilerplate for the Rock Paper Scissors project. 
Instructions for building project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors.
Origin:

The initial implementation was a basic strategy for the Rock-Paper-Scissors game, where the player simply repeated the opponent's move from two plays ago. The task was to implement a Q-learning-based approach to defeat various predefined opponents: Quincy, Abbey, Kris, and Murgesh.

**Problems Identified:**

Basic Strategy: The original strategy was too simplistic and did not adapt to the opponents' patterns effectively.
Inconsistent Performance: The Q-learning model initially implemented showed inconsistent performance, especially struggling against opponents like Abbey and Kris.
Suboptimal Parameter Tuning: Initial Q-learning parameters such as alpha, gamma, and epsilon were not fine-tuned, leading to suboptimal learning and exploitation.

**Solutions Implemented:**

Q-learning Integration: Implemented Q-learning to allow the player to learn and adapt based on the opponent's history.
Enhanced Pattern Recognition: Improved the pattern recognition mechanism to better predict the opponent's moves by extending the analysis to sequences of the last three moves.
Dynamic Epsilon Adjustment: Implemented a dynamic epsilon decay strategy to balance exploration and exploitation more effectively. This ensures more exploration in the initial stages and focuses on exploitation as the game progresses.

Learning from Losses: Increased the learning rate for losses to emphasize adjusting the strategy when the player loses, ensuring quicker adaptation to opponents' strategies.
Multiple Strategies and Fine-tuning: Developed multiple strategies and fine-tuned Q-learning parameters to consistently achieve a win rate above 60% against all opponents.

**Summary of Results**

Consistent High Performance: Achieved a win rate of over 60% against all opponents consistently.
Improved Adaptability: The player can now effectively adapt to different opponents' strategies through enhanced pattern recognition and dynamic parameter adjustment.
The final implementation represents a robust Q-learning-based approach capable of outperforming various predefined strategies in the Rock-Paper-Scissors game.
