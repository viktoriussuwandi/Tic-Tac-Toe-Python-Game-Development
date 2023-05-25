from flask import Flask, render_template, redirect, url_for, Response, json
from flask_bootstrap import Bootstrap
from controller.game import Game

# ----------------------------------------------------------------------------------------
# Initialization & additional functions
# ----------------------------------------------------------------------------------------
game = Game()
app = Flask(__name__)
Bootstrap(app)

ATTR = {
  "game_board"   : {},
  "game_score"   : {},
  "game_level"   : '',
  "game_options" : [],
  "game_over"    : False,
  "player_turn"  : '',
  "player_cells" : [],
  "comp_cells"   : [],
}

def update_attributes():
  game.game_update_attr()
  ATTR['game_board']     = game.board_current
  ATTR['game_score']     = game.scores
  ATTR['game_level']     = game.game_level_txt
  ATTR['game_options']   = game.level_options
  ATTR['game_over']      = game.game_over
  ATTR['player_turn']    = game.turn_mark
  ATTR['player_cells']   = game.player.cells_selected
  ATTR['comp_cells']     = game.comp.cells_selected

def game_loop():
  update_attributes()

  while game.game_start == True and game.game_over == False:
    if game.game_over == True: break
    else: redirect(url_for('home', attr=ATTR))


# ----------------------------------------------------------------------------------------
# Common Routes
# ----------------------------------------------------------------------------------------
@app.route("/")
def home():
  check_loop = (game.game_start == False
                and game.game_over == True) or (game.game_start == True
                                                and game.game_over == False)
  if check_loop:
    print(game)
    print(game.board)
    game_loop()
    
  return render_template("index.html", attr=ATTR)


# -------------------------------------------------------------------------------------------
# Routes for data transfer from/to index.js
# -------------------------------------------------------------------------------------------


# select game difficulties (easy, medium, impossible)
@app.route('/update_level/<string:selected_level>', methods=['POST'])
def select_level(selected_level=None):
  game_level = selected_level.strip()
  game.select_game_level(level_selected=game_level)  
  return '/'


# select user role (X or O)
@app.route('/update_role/<string:selected_role>', methods=['POST'])
def select_role(selected_role=None):
  user_role = selected_role.strip()
  game.select_player_role(role_selected=user_role)
  return '/'


# Select square cells on game board
@app.route('/update_cells/<string:cells>', methods=['POST'])
def select_cell(cells=None):
  row = int(cells.split('-')[0])
  col = int(cells.split('-')[-1])
  game.select_cells(row, col)
  return '/'

@app.route('/ajax')
def ajax() :
  update_attributes()
  game_data = ATTR
  return Response(json.dumps(game_data), mimetype='application/json')


# -------------------------------------------------------------------------------------------
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=2000)