from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Estado del juego (simple, sin persistencia entre reinicios)
game_state = {
    'board': ['', '', '', '', '', '', '', '', ''],
    'current_player': 'X',
    'winner': None,
    'game_over': False
}

def check_winner(board):
    """Verifica si hay un ganador"""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    
    if '' not in board:
        return 'Tie'
    
    return None

@app.route('/')
def index():
    """Página principal del juego"""
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    """Reinicia el juego"""
    global game_state
    game_state = {
        'board': ['', '', '', '', '', '', '', '', ''],
        'current_player': 'X',
        'winner': None,
        'game_over': False
    }
    return jsonify(game_state)

@app.route('/move', methods=['POST'])
def make_move():
    """Realiza un movimiento"""
    global game_state
    
    if game_state['game_over']:
        return jsonify({'error': 'El juego ha terminado'}), 400
    
    data = request.json
    position = data.get('position')
    
    if position is None or position < 0 or position > 8:
        return jsonify({'error': 'Posición inválida'}), 400
    
    if game_state['board'][position] != '':
        return jsonify({'error': 'Casilla ocupada'}), 400
    
    # Realizar el movimiento
    game_state['board'][position] = game_state['current_player']
    
    # Verificar ganador
    winner = check_winner(game_state['board'])
    
    if winner:
        game_state['winner'] = winner
        game_state['game_over'] = True
    else:
        # Cambiar de jugador
        game_state['current_player'] = 'O' if game_state['current_player'] == 'X' else 'X'
    
    return jsonify(game_state)

@app.route('/state', methods=['GET'])
def get_state():
    """Obtiene el estado actual del juego"""
    return jsonify(game_state)

if __name__ == '__main__':
    # Ejecutar en el puerto 80 (requiere permisos de root)
    # Para desarrollo, puedes usar el puerto 5000
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=False)
