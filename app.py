from flask import Flask, render_template

app = Flask(__name__)

# Route to serve the chatbot HTML file
@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an index.html file in the templates folder

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)  # Run the server on localhost:5050
