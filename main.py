from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from controller.game import Game
import json

game = Game()
app  = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home() :
  game_board = game.get_board()
  game_score = game.get_score()
  
  return render_template(
    "index.html",
    options    = game.level_options,
    board = game_board,
    score = game_score
  )

# -------------------------------------------------------------------------------------------
# Routes to receive data from javascript on click event
# -------------------------------------------------------------------------------------------

# select game difficulties (easy, medium, impossible)
@app.route('/update_level/<string:selected_level>', methods=['POST'])
def select_level(selected_level = None) :
  game_level = json.loads(selected_level).strip()
  if game.game_start == False and game.game_over == False :
    game.select_game_level(level_selected = game_level)
    print(f'Game Level : {game.game_level}')
  return '/'

# select user role (X or O)
@app.route('/update_role/<string:selected_role>', methods=['POST'])
def select_role(selected_role = None) :
  user_role  = json.loads(selected_role).strip()
  if not game.game_start and not game.game_over :
    game.select_player_role(role_selected = user_role)
    print(f'Player Role : {game.player.role} ; Comp role : {game.comp.role}')
  return '/'  

# -------------------------------------------------------------------------------------------
if __name__ == "__main__" :
  app.run(debug=True, host="0.0.0.0", port=2000)