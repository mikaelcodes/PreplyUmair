
import flask
app = flask.Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('main.html')



app.run(debug=True)