import time
import numpy as np
import matplotlib.pyplot as plt
from logic import solve_n_queens_determinist, solve_n_queens_vegas

def measure_algorithm_performance():
    """
    Measure and compare performance of deterministic and Las Vegas N-Queens algorithms
    """
    # Board sizes to test
    board_sizes = [4, 5, 6, 8, 10, 12, 15]
    
    # Number of runs for each board size
    num_runs = 10
    
    # Store performance results
    determinist_times = []
    vegas_times = []
    
    # Measure performance for each board size
    for n in board_sizes:
        # Deterministic algorithm performance
        det_run_times = []
        start_time = time.time()
        solve_n_queens_determinist(n)
        det_run_times.append(time.time() - start_time)
        determinist_times.append(np.mean(det_run_times))
        
        # Las Vegas algorithm performance
        vegas_run_times = []
        for _ in range(num_runs):
            start_time = time.time()
            solve_n_queens_vegas(n)
            vegas_run_times.append(time.time() - start_time)
        vegas_times.append(np.mean(vegas_run_times))
    
    # Plotting with bar graph
    plt.figure(figsize=(12, 7))
    
    # Set the width of each bar and positions
    bar_width = 0.35
    index = np.arange(len(board_sizes))
    
    

    # Create bar plots
    plt.bar(index - bar_width/2, determinist_times, bar_width, 
            label='Deterministic Algorithm (Normalized)', color='blue', alpha=0.7)
    plt.bar(index + bar_width/2, vegas_times, bar_width, 
            label='Las Vegas Algorithm (Normalized)', color='green', alpha=0.7)
    
    # Customizing the plot
    plt.xlabel('Board Size (n)', fontsize=12)
    plt.ylabel('Normalized Execution Time', fontsize=12)
    plt.yscale('log')
    plt.title('N-Queens Algorithms: Time Complexity Comparison (Normalized)', fontsize=14)
    
    # Set x-ticks to board sizes
    plt.xticks(index, board_sizes)
    
    # Add a grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add legend
    plt.legend()
    
    # Tight layout to prevent cutting off labels
    plt.tight_layout()
    
    # Save the plot
    plt.show()
    
    # Print detailed results
    print("Board Size | Deterministic Time | Las Vegas Time")
    print("-" * 50)
    for n, det_time, vegas_time in zip(board_sizes, determinist_times, vegas_times):
        print(f"{n:10d} | {det_time:17.5f} | {vegas_time:14.5f}")
    
if __name__ == "__main__":
    measure_algorithm_performance()
