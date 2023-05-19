from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from controller.game import Game

game = Game()
app  = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home() :
  difficult_options = game.difficult_options
  return render_template(
    "index.html", 
    options = difficult_options, 
    select_option = difficult_options[1]
  )

if __name__ == "__main__" :
  app.run(debug=True, host="0.0.0.0", port=2000)