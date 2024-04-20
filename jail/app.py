from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if users.get(username) == password:
            return redirect(url_for('dashboard'))
        else:
            return render_template('error.html')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('after_signup'))
    return render_template('signup.html')

@app.route('/after_signup')
def after_signup():
    return "Account created successfully! <a href='/login'>Login</a>"

@app.route('/dashboard')
def dashboard():
    return "(should show the menu page here)"

if __name__ == '__main__':
    app.run(debug=True)
