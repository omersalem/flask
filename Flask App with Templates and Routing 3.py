# Import Flask and render_template
from flask import Flask, render_template
from datetime import datetime as dt


# Create an instance of the Flask class
app = Flask(__name__)

# Define the root route, rendering index.html
@app.route('/')
def home():
    # render_template looks for the file in the 'templates' folder
    greetings =['good morning','good evening']
    
    return render_template('index.html', greetings=greetings,current_time=dt.now())

# Define the about route, rendering about.html
@app.route('/about')
def about():
    return render_template('about.html')

# Define a route with a variable for username
@app.route('/user/<username>')
def show_user_profile(username):
    # We can pass variables to the template using keyword arguments
    # The variable 'name' will be available inside the template
    return render_template('profile.html', name=username)

# Define a route with an integer variable for post ID
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # You can also pass multiple variables
    return render_template('post.html', post_id=post_id, title=f'Post {post_id} Details')
@app.route('/contact/<email>')
def contact(email):
    return render_template("contact_inh.html", email=email)

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
