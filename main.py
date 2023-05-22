from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from controller.game import Game
import json

# -------------------------------------------------------------------------------------------
# Initialization & additional functions
# -------------------------------------------------------------------------------------------
game = Game()
app  = Flask(__name__)
Bootstrap(app)

ATTR = {
  "game_board"  : {},
  "game_score"  : {},
  "player_turn" : '',
  "game_over"   : False
}

def update_attributes() :
  ATTR['game_options'] = game.level_options
  ATTR['game_score']   = game.scores
  ATTR['player_turn']  = game.turn
  ATTR['game_board']   = game.board
  ATTR['game_over']    = game.game_over
  

def game_loop() :
  game.update_board()
  game.update_score()
  game.update_turn()
  update_attributes()
  
# -------------------------------------------------------------------------------------------
# Common Routes
# -------------------------------------------------------------------------------------------
@app.route("/")
def home() :
  game_loop()
  return render_template("index.html", options = game.level_options, attr = ATTR )

# -------------------------------------------------------------------------------------------
# Routes for data transfer from/to javascript
# -------------------------------------------------------------------------------------------

# select game difficulties (easy, medium, impossible)
@app.route('/update_level/<string:selected_level>', methods=['POST'])
def select_level(selected_level = None) :
  game_level = json.loads(selected_level).strip()
  if game.game_start == False and game.game_over == False :
    game.select_game_level(level_selected = game_level)
    # print(f'Game Level : {game.game_level}')
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