from flask import Flask, render_template, request , Response, url_for , redirect , abort , make_response, session
# JSON: using jsonify
from flask import jsonify
def get_user(username):
    username=username
    return username
app = Flask(__name__)

# @app.route('/')
# def main():
#     return "<h1>Hello from Flask!</h1>"

@app.route('/name/<name>')
def hello(name):
    return f"welcome to main page {name}"
@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f"{num1}+{num2}={num1+num2}"

@app.route('/search')
def search():
    q = request.args.get('q')  # Get the 'q' parameter
    return f"Search term: {q}" # so when the user enters /search?q=flask it will return Search term: flask
@app.route('/search2')
def search2():
    query = request.args.get('q', '')  # Default to empty string if not provided
    page = request.args.get('page', 1, type=int)  # Convert to int, default to 1
    return f'Searching for "{query}" on page {page}'
# so if we write http://127.0.0.1:9000/search2?q=2&page=1 then the result will be 
# Searching for "2" on page 1

@app.route('/example', methods=['POST'])
def example():
    return "This route only accepts POST requests."

@app.before_request
def handle_non_post():
    if request.endpoint == 'example' and request.method != 'POST':
        return "Method not allowed. Please use POST.", 405 # to test this use http://127.0.0.1:9000/example

# Multiple routes for the same function
@app.route('/projects/') #here we used two routes for the same function so if the user
# enter /projects or /projects/<index_no> it will return the same thing
@app.route('/projects/<path:index>') #path variable same as int but it contains slashes and -
def projects(index="10/10"):
    return f'The project page {index}'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form
        return 'Processing login'
    else:
        # Show the login form
        return 'Please log in'

from flask import Response

@app.route('/custom-response')
def custom_response():
    content = 'Hello, omar!'
    response = Response(content, status=200, mimetype='text/plain')
    response.headers['X-Custom-Header'] = 'Custom Value'
    return response
@app.route('/custom-response2')
def custom_response2():
    content = '''
    <html>
      <body style="background-color: black; color: white;">
        <h1>Hello, World!</h1>
      </body>
    </html>
    '''
    response = Response(content, status=200, mimetype='text/html')
    response.headers['X-Custom-Header'] = 'Custom Value'
    return response

@app.route('/string') #we can put any name of variable /string1 or /string2
def return_string():
    return 'Hello, World!' # here we used string instead of response

# Tuple: (response, status, headers)
@app.route('/tuple') #it is just names of variables and you can change it as you want
def return_tuple():
    return 'Error black', 400, {'X-Error': 'Invalid request'} # here we used tuple instead of response
#the result will be error black



@app.route('/json') # we can put /json2 or /json3 it is just a name of variable
def return_json():
    data = {'name': 'John', 'age': 30} #this is a dictionary of data that will be converted to json using
    # the jsonify function
    return jsonify(data) # here we used jsonify instead of response 
@app.route('/about')
def about():
    # Generate the URL for the 'index' route
    koora = url_for('external_redirect') # here we use url_for to generate the url
    # for the /json route by using the name of the function (return_json) 
    return f'Go back to the <a href="{koora}">kooora website</a>!' #this function on line 107

@app.route('/')
def index():
    return 'Welcome to the homepage!'
@app.route('/redirect-example')
def redirect_example():
    # Redirect to the index page
    return redirect(url_for('index')) # so here it will redirect me to the index page

@app.route('/external')
def external_redirect():
    # Redirect to an external URL
    return redirect('https://www.kooora.com') # o here it will redirect me to kooora.com

@app.route('/user/<username>')
def show_user_profile(username):
    user = get_user(username)  # Assume this function retrieves a user
    if user == "omersalem":
        # Show a 404 error page
        abort(404) # so here if i entered /user/omersalem it will return 404 not found
    return f'User: {user}'
@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found please check again and again', 404 #so any time you put wrong url it will return 404
# the message in the return "Page not found please check again and again"

@app.errorhandler(500) #When an unexpected server error occurs, it returns
#"Internal server error" with the 500 status code.
def internal_server_error(e):
    return 'Internal server error', 500
#This code sets a cookie named 'username' with the value 'john' that expires in 30 days. 
# When a user visits the '/set-cookie' route, the cookie is stored in their browser.
@app.route('/set-cookie')
def set_cookie():
    response = make_response('Cookie set!')
    response.set_cookie('username', 'john', max_age=60*60*24*30)  # 30 days
    return response
'''
You can see the stored cookie in your browser's developer tools:
Right-click on the page and select Inspect.
Go to the Application tab.
In the left sidebar, under Storage, click on Cookies.
Select your website's URL.
You’ll see the list of cookies stored for that site, including the 'username' cookie with value 'john'.
'''

@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Username from cookie: {username}'

'''
This code defines a Flask route /get-cookie that retrieves the value of a cookie named username
from the request and returns it as a string. In other words, when a user visits
the /get-cookie URL, the server will check if a username cookie is stored 
in the user's browser and display its value.
(request.cookies.get('username') is used to safely retrieve the cookie
 value, returning None if the cookie does not exist.)
'''
# Set a secret key for signing the session cookie
app.secret_key = 'your_secret_key'  # In production, use a secure random key
# the secret key is used to sign the session cookie and to encrypt it

@app.route('/set-session')
def set_session():
    """
    Sets a session variable 'username' to 'john' and returns a success message.

    When a user visits the '/set-session' route, the server will store a session
    variable named 'username' with the value 'john' in the user's browser. The
    user will see a success message "Session data set!" in their browser.
    """
    session['username'] = 'john' # here we store the username in the session
    return 'Session data set!'

@app.route('/get-session')
def get_session():
    """
    Retrieves and returns the 'username' stored in the session.
    When a user visits the '/get-session' route, the server retrieves
    the session variable 'username'. The username is then returned 
    as part of a formatted string.
    """

    username = session.get('username') 
    return f'Username from session: {username}'

@app.route('/clear-session')
def clear_session():
    """
Clears the 'username' key from the session.When a user visits the '/clear-session' route,
 the server removes the 'username' key from the session. 
 The user will see a success message "Session cleared!" in their browser.
    """
    session.pop('username', None)  # Remove the username key if it exists
    return 'Session cleared!'
@app.route('/debug-session')
def debug_session():
    """
    Debug route to dump the current session contents as a JSON object.
    This route is useful for inspecting the session data in the browser.
    and returns a JSON object containing the session data. the session data
    is not stored in the browser because it is sensitive information
    """


    return dict(session)
if __name__ == '__main__':
    app.run(debug=True,port=9000)

'''
The main difference between a cookie and a session is where the data is stored and how it is managed:

Cookie:

Small pieces of data stored directly in the user's browser.
Sent with every HTTP request to the server.
Can be read and modified by the client (unless secured properly).
Limited in size (~4KB).
Used to store simple info like session IDs, preferences, etc.
Needs to be secured (using Secure, HttpOnly, SameSite flags) to prevent theft or manipulation.
Session:

Server-side storage of user data/linking data to user.
The client only stores a session ID in a cookie.
When the user makes a request, the server uses the session ID to retrieve stored data.
More secure for sensitive data because actual data lives on the server.
Suitable for storing larger or sensitive information securely.
In essence:

Cookies are stored on the client side.
Sessions store data on the server, with only an identifier (cookie) stored on the client.

'''