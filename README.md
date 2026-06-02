<div align="center">

# ⬡ MarkItDown GUI

**A local web-based desktop app to convert any file to Markdown**  
Built on [Microsoft's MarkItDown](https://github.com/microsoft/markitdown) · Dark mode · No internet required

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)](https://flask.palletsprojects.com)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey?logo=apple)](https://apple.com/macos)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![MarkItDown](https://img.shields.io/badge/Powered%20by-MarkItDown-blueviolet)](https://github.com/microsoft/markitdown)

</div>

---

## ✨ Features

- 📂 **Browse or drag & drop** any file into the app
- ⚡ **One-click conversion** to clean Markdown
- 💾 **Save as `.md`** or **copy to clipboard** instantly
- 🌙 **Dark mode UI** — runs in your browser, looks native
- 🔒 **Fully local** — no data leaves your machine, no internet needed
- 🖥️ **Auto-opens in browser** when you run `python3 app.py`

---

## 📁 Supported Formats

| Category | Formats |
|---|---|
| Documents | PDF, DOCX, DOC, PPTX, PPT, XLSX, XLS |
| Web | HTML, HTM |
| Data | CSV, JSON, XML |
| Media | JPG, JPEG, PNG, GIF (EXIF + OCR), MP3, WAV |
| Archives | ZIP, EPUB |

---

## 🚀 Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/Yaswanth-Boggarapu/markitdown-gui.git
cd markitdown-gui

# 2. Install dependencies
pip3 install --break-system-packages flask 'markitdown[all]'

# 3. Run
python3 app.py
```

The app auto-opens at **http://localhost:5177** in your browser.

---

## 🗂️ Project Structure

```
markitdown-gui/
├── app.py              # Flask backend — handles file upload & conversion
├── static/
│   └── index.html      # Full dark-mode UI (single file, no build step)
└── README.md
```

---

## 🔧 How It Works

1. `app.py` starts a local Flask server on port `5177` and auto-opens your browser
2. You drop a file or browse — it's uploaded to the local server via `POST /convert`
3. Flask passes the file to `MarkItDown.convert()` and returns the Markdown
4. The UI renders the result — you can save as `.md` or copy to clipboard

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| [`markitdown[all]`](https://github.com/microsoft/markitdown) | File → Markdown conversion engine by Microsoft |
| [`flask`](https://flask.palletsprojects.com) | Lightweight local web server |

---

## 🙏 Credits

- [**Microsoft AutoGen Team**](https://github.com/microsoft/markitdown) for the MarkItDown library
- Built by [Yaswanth Boggarapu](https://github.com/Yaswanth-Boggarapu)

---

## 📄 License

MIT — free to use, modify, and distribute.
