import random
from collections import defaultdict

# Define possible actions
actions = ["R", "P", "S"]

# Define a function to determine the winner
def get_winner(move1, move2):
    if move1 == move2:
        return 0  # draw
    elif (move1 == "R" and move2 == "S") or (move1 == "P" and move2 == "R") or (move1 == "S" and move2 == "P"):
        return 1  # win
    else:
        return -1  # lose

# Initialize Q-tables for each opponent
Q_tables = {
    'quincy': {move1 + move2 + move3: {a: 0 for a in actions} for move1 in actions for move2 in actions for move3 in actions},
    'abbey': {move1 + move2 + move3: {a: 0 for a in actions} for move1 in actions for move2 in actions for move3 in actions},
    'kris': {move1 + move2 + move3: {a: 0 for a in actions} for move1 in actions for move2 in actions for move3 in actions},
    'murgesh': {move1 + move2 + move3: {a: 0 for a in actions} for move1 in actions for move2 in actions for move3 in actions},
}

# Q-learning parameters
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
epsilon = 0.1  # initial exploration rate
min_epsilon = 0.01  # minimum exploration rate
epsilon_decay = 0.995  # exploration decay rate

# Opponent patterns
patterns = defaultdict(lambda: defaultdict(int))

# Define the player function
def player(prev_play, opponent_history=[], opponent="quincy"):
    if prev_play != "":
        opponent_history.append(prev_play)
    
    q_table = Q_tables[opponent]
    
    # Determine the current state
    if len(opponent_history) >= 3:
        state = opponent_history[-3] + opponent_history[-2] + opponent_history[-1]
    elif len(opponent_history) == 2:
        state = opponent_history[-2] + opponent_history[-1] + random.choice(actions)
    elif len(opponent_history) == 1:
        state = opponent_history[-1] + random.choice(actions) + random.choice(actions)
    else:
        state = random.choice(actions) + random.choice(actions) + random.choice(actions)
    
    # Pattern recognition
    if len(opponent_history) >= 3:
        last_moves = ''.join(opponent_history[-3:])
        if len(opponent_history) > 3:
            prev_moves = ''.join(opponent_history[-4:-1])
            patterns[prev_moves][opponent_history[-1]] += 1
        if last_moves in patterns:
            predicted_move = max(patterns[last_moves], key=patterns[last_moves].get)
            guess = {'R': 'P', 'P': 'S', 'S': 'R'}[predicted_move]  # Counter predicted move
        else:
            guess = max(q_table[state], key=q_table[state].get)
    else:
        guess = max(q_table[state], key=q_table[state].get)
    
    # Dynamic epsilon decay
    global epsilon
    if random.random() < epsilon:
        guess = random.choice(actions)
    epsilon = max(min_epsilon, epsilon * epsilon_decay)
    
    # Update Q-value
    if len(opponent_history) > 1:
        if len(opponent_history) >= 4:
            last_state = opponent_history[-4] + opponent_history[-3] + opponent_history[-2]
        elif len(opponent_history) == 3:
            last_state = opponent_history[-3] + opponent_history[-2] + random.choice(actions)
        else:
            last_state = opponent_history[-2] + random.choice(actions) + random.choice(actions)
        
        reward = get_winner(guess, prev_play)
        
        old_value = q_table[last_state][guess]
        future_value = max(q_table[state].values())
        q_table[last_state][guess] = old_value + alpha * (reward + gamma * future_value - old_value)
    
    return guess

