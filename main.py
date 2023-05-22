from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from controller.game import Game
import json

game = Game()
app  = Flask(__name__)
Bootstrap(app)

# select difficulties & role
# game.start_game()
# game.game_loop()

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

@app.route('/update_level/<string:selected_level>', methods=['POST'])
def select_level(selected_level=None) :
  user_level = json.loads(selected_level).strip()
  check_user_level = game.game_level is None and user_level in game.level_options
  game.game_level  = user_level if check_user_level else game.game_level
  print(game.game_level)
  return '/'

@app.route('update_role/<string:selected_role>', methods=['POST'])
def select_role(selected_role=None) :
  user_role  = json.loads(selected_level).strip()
  check_role = game.game_level is None and user_level in game.level_options
  game.game_level  = user_level if check_user_level else game.game_level
  print(game.game_level)
  return '/'  

# -------------------------------------------------------------------------------------------
if __name__ == "__main__" :
  app.run(debug=True, host="0.0.0.0", port=2000)