import tkinter as tk
from PIL import Image, ImageTk

from logic import solve_n_queens_determinist, solve_n_queens_vegas

def display_solution(board, algorithm):
    """Muestra la solución del tablero de n reinas en una ventana gráfica."""
    n = len(board)

    # Crear la ventana principal
    root = tk.Toplevel()
    root.title("Solución al problema de las n reinas - " + algorithm)

    # Crear un canvas para dibujar el tablero
    canvas_size = 600
    cell_size = canvas_size // n
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
    canvas.pack()

    # Cargar imágenes personalizadas y mantener referencias como atributos del canvas
    canvas.images = {}
    queen_image = Image.open("assets/queen.png").resize((cell_size-20, cell_size))
    canvas.images['queen'] = ImageTk.PhotoImage(queen_image)

    tile_white_image = Image.open("assets/tile_white.png").resize((cell_size, cell_size))
    canvas.images['tile_white'] = ImageTk.PhotoImage(tile_white_image)

    tile_black_image = Image.open("assets/tile_black.png").resize((cell_size, cell_size))
    canvas.images['tile_black'] = ImageTk.PhotoImage(tile_black_image)

    # Dibujar el tablero con imágenes
    for i in range(n):
        for j in range(n):
            x0 = j * cell_size
            y0 = i * cell_size

            # Seleccionar imagen de la celda
            tile_photo = canvas.images['tile_white'] if (i + j) % 2 == 0 else canvas.images['tile_black']
            canvas.create_image(x0, y0, anchor=tk.NW, image=tile_photo)

            # Dibujar una reina si está en la posición
            if board[i][j] == 1:
                canvas.create_image(x0+10, y0, anchor=tk.NW, image=canvas.images['queen'])

    root.mainloop()

def select_n_and_solve(algorithm):
    """Interfaz para seleccionar el valor de n y resolver el problema."""
    def start_solver():
        n = int(entry.get())
        
        if algorithm == "vegas":
            solution = solve_n_queens_vegas(n)
        else: 
            solution = solve_n_queens_determinist(n)
        
        if solution:
            display_solution(solution, algorithm)
        else:
            result_label.config(text=f"No se encontró solución determinista para el tablero de {n}x{n}.")
        

    # Crear ventana principal
    root = tk.Tk()
    root.title("Seleccionar valor de n")

    # Etiqueta y entrada para el valor de n

    label = tk.Label(root, text=f"Introduce el valor de n (4-15) ==> algoritmo: {algorithm}")
    label.pack(pady=10, padx=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    # Botón para iniciar la solución
    solve_button = tk.Button(root, text="Resolver", command=start_solver)
    solve_button.pack(pady=10)

    # Etiqueta para mostrar resultados
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)
    root.after(1,root.quit)

    root.mainloop()
    