import tkinter as tk
from tkinter import messagebox
import math

# Utility functions to perform matrix operations

def copy_matrix(matrix):
    """Create a deep copy of a matrix."""
    return [row[:] for row in matrix]

def determinant_ref(matrix):
    """Calculate determinant using Row Echelon Form (REF)."""
    n = len(matrix)
    matrix_copy = copy_matrix(matrix)
    sign = 1
    
    for i in range(n):
        pivot = i
        for row in range(i+1, n):
            if abs(matrix_copy[row][i]) > abs(matrix_copy[pivot][i]):
                pivot = row
        
        if matrix_copy[pivot][i] == 0:
            return 0
        
        if pivot != i:
            matrix_copy[i], matrix_copy[pivot] = matrix_copy[pivot], matrix_copy[i]
            sign *= -1
        
        for row in range(i+1, n):
            factor = matrix_copy[row][i] / matrix_copy[i][i]
            for col in range(i, n):
                matrix_copy[row][col] -= factor * matrix_copy[i][col]
    
    det = sign
    for i in range(n):
        det *= matrix_copy[i][i]
    
    return det

def sarrus_rule(matrix):
    """Calculate determinant using Sarrus' Rule (only for 3x3 matrices)."""
    if len(matrix) != 3 or len(matrix[0]) != 3:
        messagebox.showerror("Invalid Input", "Sarrus' Rule only works for 3x3 matrices.")
        return None
    
    a = matrix[0][0] * matrix[1][1] * matrix[2][2]
    b = matrix[0][1] * matrix[1][2] * matrix[2][0]
    c = matrix[0][2] * matrix[1][0] * matrix[2][1]
    d = matrix[2][0] * matrix[1][1] * matrix[0][2]
    e = matrix[2][1] * matrix[1][2] * matrix[0][0]
    f = matrix[2][2] * matrix[1][0] * matrix[0][1]
    
    return (a + b + c) - (d + e + f)

def eigenvalue_determinant(matrix):
    """Calculate eigenvalues for 2x2 and 3x3 matrices."""
    if len(matrix) == 2:
        # For 2x2 matrix
        a, b = matrix[0][0], matrix[0][1]
        c, d = matrix[1][0], matrix[1][1]
        
        trace = a + d
        determinant = a * d - b * c
        
        eigenvalue1 = (trace + ((trace ** 2 - 4 * determinant) ** 0.5)) / 2
        eigenvalue2 = (trace - ((trace ** 2 - 4 * determinant) ** 0.5)) / 2
        
        return [eigenvalue1, eigenvalue2]
    
    elif len(matrix) == 3:
        # Coefficients of the characteristic polynomial λ^3 + bλ^2 + cλ + d = 0
        trace = matrix[0][0] + matrix[1][1] + matrix[2][2]
        determinant = sarrus_rule(matrix)
        
        # Sum of products of principal minors
        minor_sum = (matrix[0][0] * matrix[1][1] +
                     matrix[1][1] * matrix[2][2] +
                     matrix[0][0] * matrix[2][2] -
                     matrix[0][1] * matrix[1][0] -
                     matrix[1][2] * matrix[2][1] -
                     matrix[0][2] * matrix[2][0])
        
        # Coefficients of characteristic polynomial
        p = -trace
        q = minor_sum
        r = -determinant
        
        # Solve cubic equation λ^3 + pλ^2 + qλ + r = 0 using Cardano's method
        A = (3*q - p**2) / 3
        B = (2*p**3 - 9*p*q + 27*r) / 27
        C = (B**2) / 4 + (A**3) / 27
        
        if C > 0:
            C_sqrt = C ** 0.5
            u = (-B / 2 + C_sqrt) ** (1/3)
            v = (-B / 2 - C_sqrt) ** (1/3)
            eigenvalue1 = u + v - p / 3
            return [eigenvalue1]
        else:
            theta = (math.acos(-B / (2 * (-A / 3) ** 1.5))) / 3
            eigenvalue1 = 2 * (-A / 3) ** 0.5 * math.cos(theta) - p / 3
            eigenvalue2 = 2 * (-A / 3) ** 0.5 * math.cos(theta + (2 * math.pi / 3)) - p / 3
            eigenvalue3 = 2 * (-A / 3) ** 0.5 * math.cos(theta + (4 * math.pi / 3)) - p / 3
            return [eigenvalue1, eigenvalue2, eigenvalue3]

def matrix_addition(matrix1, matrix2):
    """Calculate matrix addition."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        messagebox.showerror("Invalid Input", "Matrices must have the same dimensions for addition.")
        return None
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_subtraction(matrix1, matrix2):
    """Calculate matrix subtraction."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        messagebox.showerror("Invalid Input", "Matrices must have the same dimensions for subtraction.")
        return None
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_multiplication(matrix1, matrix2):
    """Calculate matrix multiplication."""
    if len(matrix1[0]) != len(matrix2):
        messagebox.showerror("Invalid Input", "Number of columns in the first matrix must equal the number of rows in the second matrix.")
        return None
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

def transpose(matrix):
    """Transpose a matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def inverse(matrix):
    """Calculate the inverse of a matrix using Gaussian Elimination."""
    n = len(matrix)
    augmented_matrix = [matrix[i] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        if augmented_matrix[i][i] == 0:
            for j in range(i + 1, n):
                if augmented_matrix[j][i] != 0:
                    augmented_matrix[i], augmented_matrix[j] = augmented_matrix[j], augmented_matrix[i]
                    break
        
        pivot = augmented_matrix[i][i]
        if pivot == 0:
            messagebox.showerror("Invalid Input", "Matrix is singular and cannot be inverted.")
            return None
        
        augmented_matrix[i] = [x / pivot for x in augmented_matrix[i]]
        
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [augmented_matrix[j][k] - factor * augmented_matrix[i][k] for k in range(2 * n)]
    
    inverse_matrix = [row[n:] for row in augmented_matrix]
    return inverse_matrix

def lu_decomposition(matrix):
    """Perform LU Decomposition on a matrix."""
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            U[i][k] = matrix[i][k] - sum(L[i][j] * U[j][k] for j in range(i))
        
        # Lower Triangular
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Diagonal as 1
            else:
                L[k][i] = (matrix[k][i] - sum(L[k][j] * U[j][i] for j in range(i))) / U[i][i]
    
    return L, U

def solve_eigenvector(matrix, eigenvalue):
    """Find eigenvector for a given eigenvalue using Gaussian elimination."""
    n = len(matrix)
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    augmented_matrix = [[matrix[i][j] - eigenvalue * identity[i][j] for j in range(n)] for i in range(n)]
    
    # Use Gaussian elimination to solve for the eigenvector
    if n == 2:
        # For 2x2 matrix: Solve the equation (A - λI)v = 0
        if augmented_matrix[0][0] != 0:
            x = -augmented_matrix[0][1] / augmented_matrix[0][0]
            return [x, 1]
        else:
            return [1, 0]
    elif n == 3:
        # Solve (A - λI)v = 0 for 3x3 using Gaussian elimination
        # We set the last component of the vector to 1 (free variable)
        
        if augmented_matrix[2][2] != 0:
            z = 1  # Free variable set to 1
            y = -augmented_matrix[1][2] / augmented_matrix[1][1] * z
            x = (augmented_matrix[0][2] * z + augmented_matrix[0][1] * y) / -augmented_matrix[0][0]
        elif augmented_matrix[1][1] != 0:
            # In case the last row doesn't reduce well, we treat middle row similarly
            z = 1
            y = -augmented_matrix[1][2] / augmented_matrix[1][1] * z
            x = 1  # Free variable
        else:
            # Set the first variable as 1 and solve accordingly if upper rows are problematic
            z = 1
            y = 1
            x = 1
        
        return [x, y, z]


# Tkinter GUI Application

class MatrixCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Enter Size of Matrix 1 (Rows x Cols):").grid(row=0, column=0, padx=10, pady=10)
        self.entry_size1 = tk.Entry(self.root)
        self.entry_size1.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Enter Size of Matrix 2 (Rows x Cols):").grid(row=1, column=0, padx=10, pady=10)
        self.entry_size2 = tk.Entry(self.root)
        self.entry_size2.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Button(self.root, text="Generate Matrices", command=self.generate_matrices).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.matrix_frame1 = tk.Frame(self.root)
        self.matrix_frame1.grid(row=3, column=0, padx=10, pady=10)
        self.matrix_frame2 = tk.Frame(self.root)
        self.matrix_frame2.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Select Operation:").grid(row=4, column=0, padx=10, pady=10)
        self.operation_var = tk.StringVar(value="Determinant")
        operations = ["Determinant", "Addition", "Subtraction", "Multiplication", "Transpose", "Inverse", "LU Decomposition", "Eigenvector"]
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, *operations, command=self.on_operation_change)
        self.operation_menu.grid(row=4, column=1, padx=10, pady=10)
        
        # Method selection for determinant
        self.method_var = tk.StringVar(value="REF")
        self.method_menu = tk.OptionMenu(self.root, self.method_var, "REF", "Laplace", "Sarrus", "Eigenvalue")
        self.method_menu.grid(row=5, column=1, padx=10, pady=10)
        self.method_menu.grid_remove()  # Initially hidden
        
        tk.Button(self.root, text="Calculate", command=self.calculate_matrix).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    
    def on_operation_change(self, operation):
        """Show or hide the method menu based on the selected operation."""
        if operation == "Determinant":
            self.method_menu.grid()
        else:
            self.method_menu.grid_remove()
    
    def generate_matrices(self):
        for widget in self.matrix_frame1.winfo_children():
            widget.destroy()
        for widget in self.matrix_frame2.winfo_children():
            widget.destroy()
        
        try:
            self.rows1, self.cols1 = map(int, self.entry_size1.get().split('x'))
            self.rows2, self.cols2 = map(int, self.entry_size2.get().split('x'))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter matrix sizes in the format 'Rows x Cols'.")
            return
        
        self.matrix_entries1 = [[tk.Entry(self.matrix_frame1, width=5) for _ in range(self.cols1)] for _ in range(self.rows1)]
        for i, row in enumerate(self.matrix_entries1):
            for j, entry in enumerate(row):
                entry.grid(row=i, column=j, padx=5, pady=5)

        self.matrix_entries2 = [[tk.Entry(self.matrix_frame2, width=5) for _ in range(self.cols2)] for _ in range(self.rows2)]
        for i, row in enumerate(self.matrix_entries2):
            for j, entry in enumerate(row):
                entry.grid(row=i, column=j, padx=5, pady=5)

    def get_matrix(self, matrix_entries):
        try:
            return [[float(entry.get()) for entry in row] for row in matrix_entries]
        except ValueError:
            messagebox.showerror("Invalid Input", "All matrix entries must be valid numbers.")
            return None

    def calculate_matrix(self):
        matrix1 = self.get_matrix(self.matrix_entries1)
        matrix2 = self.get_matrix(self.matrix_entries2)
        if matrix1 is None:
            return
        
        operation = self.operation_var.get()
        result = None
        
        if operation == "Determinant":
            if self.rows1 != self.cols1:
                messagebox.showerror("Invalid Input", "Matrix must be square for determinant.")
            else:
                method = self.method_var.get()
                if method == "REF":
                    det = determinant_ref(matrix1)
                elif method == "Sarrus" and self.rows1 == 3:
                    det = sarrus_rule(matrix1)
                elif method == "Eigenvalue" and self.rows1 in [2, 3]:
                    det = eigenvalue_determinant(matrix1)
                else:
                    messagebox.showerror("Invalid Input", f"{method} is not applicable for this matrix size.")
                    return
                result = f"Determinant ({method} method): {det}"
        
        elif operation == "Addition":
            result = matrix_addition(matrix1, matrix2)
        
        elif operation == "Subtraction":
            result = matrix_subtraction(matrix1, matrix2)
        
        elif operation == "Multiplication":
            result = matrix_multiplication(matrix1, matrix2)
        
        elif operation == "Transpose":
            result = transpose(matrix1)
        
        elif operation == "Inverse":
            if self.rows1 != self.cols1:
                messagebox.showerror("Invalid Input", "Matrix must be square for inverse.")
            else:
                result = inverse(matrix1)
        
        elif operation == "LU Decomposition":
            if self.rows1 != self.cols1:
                messagebox.showerror("Invalid Input", "Matrix must be square for LU Decomposition.")
            else:
                L, U = lu_decomposition(matrix1)
                result = f"L:\n{L}\nU:\n{U}"
        
        elif operation == "Eigenvector":
            if self.rows1 != self.cols1:
                messagebox.showerror("Invalid Input", "Matrix must be square for eigenvector.")
            else:
                eigenvalues = eigenvalue_determinant(matrix1)
                if eigenvalues is not None:
                    eigenvectors = [solve_eigenvector(matrix1, ev) for ev in eigenvalues]
                    result = f"Eigenvectors: {eigenvectors}"
                else:
                    messagebox.showerror("Calculation Error", "Failed to compute eigenvalues.")
        
        if result is not None:
            self.display_result(result)
        else:
            self.result_label.config(text="Error: Invalid operation or input matrix")

    def display_result(self, result):
        """Display the result in matrix form or as a scalar."""
        if isinstance(result, (int, float, str)):  # Check if result is scalar or string
            self.result_label.config(text=f"Result: {result}")
        else:  # For matrix (list of lists)
            result_text = "Result:\n" + "\n".join(["\t".join(map(str, row)) for row in result])
            self.result_label.config(text=result_text)


# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorApp(root)
    root.mainloop()
