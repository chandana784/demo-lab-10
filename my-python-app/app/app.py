from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/health')
def health():
    return {"status": "healthy", "path": os.getcwd()}

if __name__ == '__main__':
    print("🚀 Starting on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
