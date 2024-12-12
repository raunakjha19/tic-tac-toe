from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global variables for the game state
game_board = [' '] * 9  # 3x3 Tic Tac Toe board, initially empty
current_player = 'X'  # First player to move

def check_winner(board):
    """Check if there's a winner or if the game is a draw."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]  # Return the winner ('X' or 'O')

    if ' ' not in board:
        return 'Draw'  # Game is a draw

    return None  # No winner yet

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def make_move():
    global game_board, current_player

    # Get the move from the user
    data = request.json
    position = data.get('position')

    if game_board[position] == ' ':  # Check if the cell is empty
        game_board[position] = current_player
        winner = check_winner(game_board)

        if winner:
            response = {'status': 'win', 'winner': winner, 'board': game_board}
            game_board = [' '] * 9  # Reset for a new game
            current_player = 'X'  # Reset starting player
            return jsonify(response)

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
        return jsonify({'status': 'continue', 'board': game_board})

    return jsonify({'status': 'invalid', 'message': 'Cell already occupied!', 'board': game_board})

if __name__ == '__main__':
    app.run(debug=True)
