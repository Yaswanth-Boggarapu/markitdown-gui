import os
import threading
import webbrowser
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="")

UPLOAD_FOLDER = Path("/tmp/markitdown_uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

def get_md():
    from markitdown import MarkItDown
    return MarkItDown()

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/convert", methods=["POST"])
def convert():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    f = request.files["file"]
    if not f.filename:
        return jsonify({"error": "Empty filename"}), 400
    save_path = UPLOAD_FOLDER / f.filename
    f.save(save_path)
    try:
        md = get_md()
        result = md.convert(str(save_path))
        return jsonify({"markdown": result.text_content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        save_path.unlink(missing_ok=True)

if __name__ == "__main__":
    threading.Timer(1.2, lambda: webbrowser.open("http://localhost:5177")).start()
    print("\n  ⬡  MarkItDown running at http://localhost:5177\n  Press Ctrl+C to quit.\n")
    app.run(port=5177, debug=False)
