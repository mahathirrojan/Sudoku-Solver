class Sudoku: 
    def __init__(self, grid):
        self.grid = grid

    def display_grid(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col 
        return None
    
    def check_row(self, row, num):
        return num not in self.grid[row]
    
    def check_column(self, col, num):
        return num not in [self.grid[row][col] for row in range(9)]
    
    def check_box(self, box_start_row, box_start_col, num):
        for row in range(3):
            for col in range(3):
                if self.grid[box_start_row + row][box_start_col + col] == num:
                    return False
        return True
    def is_safe(self,row,col,num):
        return(
            self.check_row(row, num) and
            self.check_column(col,num) and 
            self.check_box(row - row % 3, col - col % 3, num)
        )
    def solve(self):
        empty_pos = self.find_empty()
        if empty_pos is None:
            return True
        row, col = empty_pos
        for num in range(1, 10):
            if self.is_safe(row,col,num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0 # This is for backtracking
        return False 
    
    
    def get_user_input(self):
        print("Enter your Sudoku puzzle row by row. Use '0' for empty cells")
        grid = []
        for _ in range(9):
            row = input("Enter a row (9 separated by spaces: ").split()
            row = [int(num) for num in row]
            grid.append(row)
        return grid
    
    def solve_and_display_sudoku(self):
        user_grid = self.get_user_input()
        sudoku_solver = Sudoku(user_grid)

        print("\nYour Sudoku Puzzle:")
        sudoku_solver.display_grid()

        if sudoku_solver.solve():
            print("\nSolved Sudoku Grid:")
            sudoku_solver.display_grid()
        else:
            print("\nNo solution exists for this.")

sudoku_solver = Sudoku([])
sudoku_solver.solve_and_display_sudoku()