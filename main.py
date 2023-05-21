from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from controller.game import Game

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
    options = game.level_options, 
    select_option = game.level_options[1],
    board = game_board,
    score = game_score
  )

def select_level1() :
  print ("Hello")
  return None

def select_level2(level=None) :
  print(level)
  return None

#Additional Function using javascript
@app.route('/<function>')
def command(function=None):
  exec(function.replace("<br>", "\n"))
  return ''
  
if __name__ == "__main__" :
  app.run(debug=True, host="0.0.0.0", port=2000)