import random

def is_safe(board, row, col, n):
    """Verifica si es seguro colocar una reina en la posición dada."""
    # Verificar esta columna hacia arriba
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Verificar diagonal superior izquierda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Verificar diagonal superior derecha
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    """Intenta resolver el problema de las n reinas recursivamente."""
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            # Colocar reina
            board[row][col] = 1

            # Llamada recursiva para la siguiente fila
            if solve_n_queens_util(board, row + 1, n):
                return True

            # Retroceder
            board[row][col] = 0

    return False

def solve_n_queens_determinist(n):
    """Resuelve el problema de las n reinas usando Backtracking."""
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens_util(board, 0, n):
        return board
    else:
        return None
    
def is_safe_vegas(queens, row, col):
    """
    Check if a queen can be placed on board[row][col]
    
    Args:
    queens (list): Current queens' column positions
    row (int): Current row being checked
    col (int): Column to place the queen
    
    Returns:
    bool: True if the queen can be placed safely, False otherwise
    """
    # Check columns and diagonals in previous rows
    for prev_row in range(row):
        # Check same column
        if queens[prev_row] == col:
            return False
        
        # Check 45-degree diagonal (top-right to bottom-left)
        if queens[prev_row] == col - (row - prev_row):
            return False
        
        # Check 135-degree diagonal (top-left to bottom-right)
        if queens[prev_row] == col + (row - prev_row):
            return False
    
    return True

def n_queens_las_vegas(n):
    """
    Solve N-Queens problem using Las Vegas algorithm
    
    Args:
    n (int): Number of queens to place
    
    Returns:
    list: Column positions of queens if a solution is found, 
          None otherwise
    """
    # Initialize queens list with n positions
    queens = [None] * n
    
    # Try to place queens in each row
    for row in range(n):
        # Generate a list of possible columns for this row
        possible_cols = list(range(n))
        random.shuffle(possible_cols)
        
        # Try each column randomly
        found_safe_col = False
        for col in possible_cols:
            if is_safe_vegas(queens, row, col):
                queens[row] = col
                found_safe_col = True
                break
        
        # If no safe column found, we've failed
        if not found_safe_col:
            return None
    
    return queens

def solve_n_queens_vegas(n):
    # Number of attempts to find a solution
    max_attempts = 300
    
    # Try to find a solution
    for attempt in range(max_attempts):
        solution = n_queens_las_vegas(n)
        if solution is not None:
            #print(f"Solution found on attempt {attempt + 1}")
            board = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                board[i][solution[i]] = 1
            return board
    print("No solution found after", max_attempts, "attempts")

if __name__ == "__main__":
    solve_n_queens_vegas(8)