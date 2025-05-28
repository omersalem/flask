# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class.
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses this to know where to look for static files and templates.
app = Flask(__name__)

# Define a route. This decorator tells Flask which URL should trigger our function.
# When a user visits the root URL ('/'), this function will be executed.
@app.route('/')
def hello_world():
    # This function returns the string "Hello, World!".
    # Flask automatically sends this string as the response to the web browser.
    return 'Hello, World!'

# This block ensures that the Flask development server runs only when the script
# is executed directly (not when imported as a module).
# debug=True enables debug mode, which provides helpful error messages and
# automatically reloads the server when you make code changes.
if __name__ == '__main__':
    app.run(debug=True)

