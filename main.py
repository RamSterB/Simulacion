from interfaz import select_n_and_solve

import simulacion
import complejidad
import tkinter as tk

def launch_gui():
    """Launch the GUI for N-Queens."""
    select_n_and_solve("determinist")
    select_n_and_solve("vegas")

def run_simulation():
    """Run the SimPy simulation."""
    simulacion.main()

def show_complexity_graph():
    """Display the complexity analysis graph."""
    complejidad.measure_algorithm_performance()

def main():
    """Main function to unify all components."""
    # Create the main window
    root = tk.Tk()
    root.title("N-Queens Project")
    root.geometry("400x300")

    # Add buttons for each functionality
    tk.Label(root, text="Welcome to the N-Queens Project!", font=("Helvetica", 16)).pack(pady=20)

    tk.Button(root, text="Solve N-Queens (GUI)", command=launch_gui, width=30, height=2).pack(pady=10)
    tk.Button(root, text="Run Simulation", command=run_simulation, width=30, height=2).pack(pady=10)
    tk.Button(root, text="Show Complexity Graph", command=show_complexity_graph, width=30, height=2).pack(pady=10)

    tk.Label(root, text="Select an option to proceed.").pack(pady=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()

