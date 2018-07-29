# importing flask module
from flask import Flask, render_template, request

# initializing a variable of Flask
app = Flask(__name__)


# decorating index function with the app.route
@app.route('/')
def index():
   return "WELCOME!!! This is the home page"

@app.route('/LoginPassed',  methods=['POST'])
def success():
   if request.method == 'POST':
       email = request.form['email']
       return render_template('success.html', email=email)
   else:
       pass

@app.route('/login')
def login():
   return render_template('login.html')

# Do it...  
if __name__ == "__main__":
   app.run()
