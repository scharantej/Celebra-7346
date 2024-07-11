
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    celebration_message = "Congratulations! Scream was successfully created."
    return render_template('index.html', message=celebration_message)

if __name__ == '__main__':
    app.run(debug=True)
