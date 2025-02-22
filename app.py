from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # Centralized page with buttons

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)  # Launcher runs on port 3000
