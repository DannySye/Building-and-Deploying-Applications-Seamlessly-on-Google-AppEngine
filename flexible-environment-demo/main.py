# main.py for the Flexible Environment
from flask import Flask, request, render_template_string, session, redirect, url_for
import random
import os

app = Flask(__name__)
# A secret key is required for using sessions, which store data between requests.
app.secret_key = os.urandom(24)

# HTML and CSS template for the game.
# We use render_template_string to keep everything in one file.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Guessing Game</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-lg p-8 text-center">
        <h1 class="text-3xl font-bold text-gray-800 mb-2">Guess the Number!</h1>
        <p class="text-gray-600 mb-6">I'm thinking of a number between 1 and 100.</p>
        
        <form action="/guess" method="post" class="mb-4">
            <input type="number" name="guess" class="w-full px-4 py-3 border border-gray-300 rounded-lg text-lg text-center focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Enter your guess" required min="1" max="100">
            <button type="submit" class="w-full mt-4 bg-blue-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-blue-700 transition duration-300 shadow-md">Guess</button>
        </form>

        {% if message %}
            <div class="p-4 rounded-lg 
                {% if message and 'Correct' in message %} bg-green-100 text-green-800 
                {% elif message and ('high' in message or 'low' in message) %} bg-yellow-100 text-yellow-800 
                {% else %} bg-gray-200 text-gray-800 
                {% endif %}">
                <p class="font-medium text-lg">{{ message }}</p>
                {% if turns is not none %}
                    <p class="text-sm">You took {{ turns }} guesses.</p>
                {% endif %}
            </div>
        {% endif %}

        {% if message and 'Correct' in message %}
            <a href="/reset" class="w-full mt-4 inline-block bg-gray-700 text-white font-bold py-3 px-4 rounded-lg hover:bg-gray-800 transition duration-300 shadow-md">Play Again</a>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """Start the game or show the main page."""
    # Generate a new random number if one isn't already in the session.
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['turns'] = 0
    
    message = session.pop('message', None)
    turns = session.pop('turns_taken', None)
    return render_template_string(HTML_TEMPLATE, message=message, turns=turns)

@app.route('/guess', methods=['POST'])
def guess():
    """Handle the user's guess."""
    if 'number' not in session:
        return redirect(url_for('index'))

    try:
        user_guess = int(request.form['guess'])
        session['turns'] += 1
        target_number = session['number']
        
        if user_guess < target_number:
            message = "Too low! Try a higher number."
        elif user_guess > target_number:
            message = "Too high! Try a lower number."
        else:
            message = f"Correct! The number was {target_number}."
            session['turns_taken'] = session['turns']
            # Clear the session number to end the game until reset
            session.pop('number', None)

        session['message'] = message
    except (ValueError, KeyError):
        session['message'] = "Please enter a valid number."

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    """Reset the session to start a new game."""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # This is used when running locally only.
    app.run(host='0.0.0.0', port=8080, debug=True)

