from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime as dt

app = Flask(__name__)
# A secret key is required for Flask's session management and flash messages.
# In a real application, use a strong, randomly generated key and store it securely.
app.config['SECRET_KEY'] = '123321123' # IMPORTANT: Change this!

# Create an instance of the Flask class


# Define the root route, rendering index.html
@app.route('/')
def home():
    # render_template looks for the file in the 'templates' folder
    greetings =['good morning','good evening']
    
    return render_template('index_inh.html', greetings=greetings, current_time = dt.now().hour)

# Define the about route, rendering about.html
@app.route('/about')
def about():
    return render_template('about_inh.html')

# Define a route with a variable for username
@app.route('/user/<username>')
def show_user_profile(username):
    # We can pass variables to the template using keyword arguments
    # The variable 'name' will be available inside the template
    return render_template('profile_inh.html', name=username)

# Define a route with an integer variable for post ID
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # You can also pass multiple variables
    return render_template('post_inh.html', post_id=post_id, title=f'Post {post_id} Details')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # If the request method is POST, it means the form has been submitted.
        # request.form is a dictionary-like object that contains form data.
        # We access values using the 'name' attribute from the HTML input fields.
        user_name = request.form['user_name']
        user_email = request.form['user_email']
        user_message = request.form['user_message']

        # For demonstration, we'll just print the data to the console.
        # In a real app, you would save this to a database, send an email, etc.
        print(f"New Contact Form Submission:")
        print(f"Name: {user_name}")
        print(f"Email: {user_email}")
        print(f"Message: {user_message}")

        # flash() function stores a message to be displayed on the next page.
        flash('Thank you for your message! We will get back to you soon.')

        # redirect() function sends the user to a different URL.
        # url_for() generates the URL for the 'home' function.
        return redirect(url_for('about'))
    else:
        # If the request method is GET, it means the user is just visiting the page
        # to see the form, so we render the contact.html template.
        return render_template('contact_form.html')
# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
