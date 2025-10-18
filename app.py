from flask import Flask, send_from_directory

# Minimal Flask app to serve the static site root and assets.
app = Flask(__name__, static_folder='')


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/<path:path>')
def static_files(path):
    # Serve any other file (CSS, JS, images, pages)
    return send_from_directory('.', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
