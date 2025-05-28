# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class.
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses this to know where to look for static files and templates.
app = Flask(__name__)
@app.route("/")
def home_page():
    return '<h1>Home Page</h1>'
@app.route('/contact')
def contact_page():
    return '<h1>Contact Us!</h1>'
@app.route('/name/<name>')
def name_page(name):
    return f' <h1>welcome {name}</h1>'
@app.route('/post/<int:id>')
def post_page(id):
    return f' <h1>Post {id}</h1>' # if the user enters \post\2 it will return Post 2
if __name__ == '__main__':
    app.run(debug=True)