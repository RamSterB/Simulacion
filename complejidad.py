import time
import numpy as np
import matplotlib.pyplot as plt
from logic import solve_n_queens_determinist, solve_n_queens_vegas

def measure_algorithm_performance():
    """
    Measure and compare performance of deterministic and Las Vegas N-Queens algorithms
    over a simulated 8-hour period.
    """
    # Board sizes to test
    board_sizes = [4, 5, 6, 8, 10, 12, 15]

    # Store performance results
    determinist_times = {n: [] for n in board_sizes}
    vegas_times = {n: [] for n in board_sizes}

    # Simulate the 8-hour period with controlled iteration count
    simulated_iterations = 1400  # Total iterations to simulate
    for _ in range(simulated_iterations):
        for n in board_sizes:
            # Deterministic algorithm performance
            start_time = time.time()
            solve_n_queens_determinist(n)
            determinist_times[n].append(time.time() - start_time)

            # Las Vegas algorithm performance
            start_time = time.time()
            solve_n_queens_vegas(n)
            vegas_times[n].append(time.time() - start_time)

    # Calculate mean times
    mean_determinist_times = [np.mean(determinist_times[n]) for n in board_sizes]
    mean_vegas_times = [np.mean(vegas_times[n]) for n in board_sizes]

    # Plotting the results
    plt.figure(figsize=(12, 7))

    # Set the width of each bar and positions
    bar_width = 0.35
    index = np.arange(len(board_sizes))

    # Create bar plots
    plt.bar(index - bar_width/2, mean_determinist_times, bar_width, 
            label='Deterministic Algorithm', color='blue', alpha=0.7)
    plt.bar(index + bar_width/2, mean_vegas_times, bar_width, 
            label='Las Vegas Algorithm', color='green', alpha=0.7)

    # Customizing the plot
    plt.xlabel('Board Size (n)', fontsize=12)
    plt.ylabel('Average Execution Time (seconds)', fontsize=12)
    plt.yscale('log')
    plt.title('N-Queens Algorithms: Time Complexity Comparison', fontsize=14)

    # Set x-ticks to board sizes
    plt.xticks(index, board_sizes)

    # Add a grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add legend
    plt.legend()

    # Tight layout to prevent cutting off labels
    plt.tight_layout()

    # Print detailed results
    print("Board Size | Deterministic Time | Las Vegas Time")
    print("-" * 60)
    for n, det_time, vegas_time in zip(board_sizes, mean_determinist_times, mean_vegas_times):
        print(f"{n:10d} | {det_time:.6f} seconds | {vegas_time:.6f} seconds")

    # Save the plot
    plt.show()

if __name__ == "__main__":
    measure_algorithm_performance()
