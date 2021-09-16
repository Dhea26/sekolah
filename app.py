from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = 'kunci session' #untuk memberikan session

db = [
    {
        "username": "Dhea",
        "password": "dhea",
        
    },

    {
        "username": "kim",
        "password": "kim",
        
    },

    {
        "username": "sukem",
        "password": "sukem",
       
    },

    {
        "username": "sri",
        "password": "sri",
        
    },
]

# routing

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/program')
def program():
    return render_template('program.html')
    

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        for d in db:
            if d['username'] == request.form['username']:
                if d['password'] == request.form['password']:
                    return redirect(url_for('program'))


    return render_template('login.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/gallery')
def igallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.jinja_env.auto_reload=True
    app.run(debug=True, host='0.0.0.0')
