"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi! This is the home page.</title>
      </head>
      <body>
        <h1> Hi! This is the Home Page.</h1>
        <a href="http://localhost:5000/hello">Hello Page</a>
      </body>
      </html>
      """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
        
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? 
          <input type="text" name="person">
          <label for="compliment">Choose a compliment:</label>
          <select name="comp" id="compliment">
          <option value="cute">Cute</option>
          <option value="Pythonriffic">Pythonriffic</option>
          <option value="incredible">Incredible</option>
          <input type="submit" value="Submit">
          </select>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment1 = choice(AWESOMENESS)
    compliment = request.args.get("comp")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
