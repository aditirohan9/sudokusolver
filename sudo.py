from flask import Flask, render_template, request, jsonify


board = [[0 for _ in range(9)] for _ in range(9)]



def check_row(board, row, num):
    if num in board[row]:
        return False
    return True

def check_column(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return False
    return True

def check_box(board, row, col, num):
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_start_row + i][box_start_col + j] == num:
                return False
    return True

def is_valid(board, row, col, num):
    row_valid = check_row(board, row, num)
    column_valid = check_column(board, col, num)
    box_valid = check_box(board, row, col, num)
    
    if row_valid and column_valid and box_valid:
        return True
    
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
        
def solver(board):
    empty_space = find_empty(board)
    
    if not empty_space:
        return True
    else:
        row, col = empty_space
        
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                
                if solver(board):
                    return True
                
                # Backtrack
                board[row][col] = 0
            
    return False
                
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
            
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') # Your HTML file

@app.route('/solve', methods=['POST'])
def solve():
    # 1. Get the data sent from JavaScript
    data = request.get_json()
    board = data.get('board')

    # 2. Try to solve it (we will write this function in Step 3)
    if solver(board):
        # 3. If successful, send the solved board back
        return jsonify({'status': 'success', 'solved_board': board})
    else:
        # If the puzzle is impossible, let the front end know
        return jsonify({'status': 'error'})

if __name__ == '__main__':
    app.run(debug=True)