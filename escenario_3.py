import simpy
import random
import time
from logic import solve_n_queens_determinist, solve_n_queens_vegas


# Constants
GAME_DURATION = 8 * 60 * 60  # 8 hours in seconds
ARRIVAL_TIME_MIN = 10  # Minimum inter-arrival time (seconds)
ARRIVAL_TIME_MAX = 30  # Maximum inter-arrival time (seconds)
BOARD_SIZES = [6]  # Possible board sizes

# Statistics
total_games = 0
total_gain = 0

def robot_arrival(env):
    """Generate robots arriving at random intervals."""
    while True:
        # Wait for the next robot to arrive
        yield env.timeout(random.uniform(ARRIVAL_TIME_MIN, ARRIVAL_TIME_MAX))
        # Add a robot to the game queue
        env.process(play_game(env))

def play_game(env):
    """Simulate a single game between a robot and the professor."""
    global total_games, total_gain

    # Choose a random board size
    board_size = random.choice(BOARD_SIZES)

    # Record the start time of the game
    start_time = env.now

    # Both players attempt to solve the N-Queens problem
    robot_solution = env.process(solve_n_queens_vegas_simpy(env, board_size))
    professor_solution = env.process(solve_n_queens_determinist_simpy(env, board_size))

    # Wait for the first to finish
    winner = yield simpy.AnyOf(env, [robot_solution, professor_solution])

    # Determine the result
    game_time = env.now - start_time
    total_games += 1

    if professor_solution in winner:
        # Professor wins
        total_gain += 15
        print(f"Game {total_games}: Professor wins on board size {board_size} in {game_time:.2f} seconds.")
    else:
        # Robot wins
        total_gain -= 10
        print(f"Game {total_games}: Robot wins on board size {board_size} in {game_time:.2f} seconds.")

def solve_n_queens_vegas_simpy(env, board_size):
    """SimPy process for the robot solving N-Queens using the Las Vegas algorithm."""
    start_time = time.time()
    solve_n_queens_vegas(board_size)
    yield env.timeout(time.time() - start_time)  # Simulated execution time
    return solve_n_queens_vegas(board_size)

def solve_n_queens_determinist_simpy(env, board_size):
    """SimPy process for the professor solving N-Queens using the deterministic algorithm."""
    start_time = time.time()
    solve_n_queens_determinist(board_size)
    yield env.timeout(time.time() - start_time)  # Simulated execution time
    return solve_n_queens_determinist(board_size)

# Main simulation function
def main():
    global total_gain

    # Create the SimPy environment
    env = simpy.Environment()

    # Start the robot arrival process
    env.process(robot_arrival(env))

    # Run the simulation
    env.run(until=GAME_DURATION)

    # Output statistics
    print(f"\nSimulation finished after {GAME_DURATION / 3600} hours.")
    print(f"Total games played: {total_games}")
    print(f"Total gain: {total_gain}")
    

if __name__ == "__main__":
    main()
