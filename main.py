from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from controller.game import Game

game = Game()
app  = Flask(__name__)
Bootstrap(app)

# select difficulties & role
while not game.game_start : game.start_game()
print(f'Game level  : { game.level_options[game.game_level] }')
print(f'Player role : { game.role_options[game.player.role] }')
print(f'Comp role   : { game.role_options[game.comp.role] }')


# @app.route("/")
# def home() :
#   difficult_options = game.difficult_options
#   game_board = game.get_board()
#   game_score = game.get_score()
  
#   return render_template(
#     "index.html", 
#     options = difficult_options, 
#     select_option = difficult_options[1],
#     board = game_board,
#     score = game_score
#   )

# if __name__ == "__main__" :
#   app.run(debug=True, host="0.0.0.0", port=2000)