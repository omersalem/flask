from flask import Flask, render_template, request , Response
# JSON: using jsonify
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def main():
    return "<h1>Hello from Flask!</h1>"

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

@app.route('/string')
def return_string():
    return 'Hello, World!'

# Tuple: (response, status, headers)
@app.route('/tuple')
def return_tuple():
    return 'Error black', 400, {'X-Error': 'Invalid request'}



@app.route('/json')
def return_json():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

    return response
if __name__ == '__main__':
    app.run(debug=True,port=9000)

