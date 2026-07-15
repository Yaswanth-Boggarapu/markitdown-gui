---
title: MarkItDown
emoji: ⬡
colorFrom: violet
colorTo: indigo
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
license: mit
---

<div align="center">

# ⬡ MarkItDown GUI

**Convert any file to Markdown — powered by Microsoft's MarkItDown**  
Dark mode · No data stored · Auto-converts on upload

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-orange?logo=gradio)](https://gradio.app)
[![HuggingFace](https://img.shields.io/badge/🤗-Live%20Demo-yellow)](https://huggingface.co/spaces/yaswanthb0420/markitdown-gui)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![MarkItDown](https://img.shields.io/badge/Powered%20by-MarkItDown-blueviolet)](https://github.com/microsoft/markitdown)

</div>

---

## ✨ Features

- 📂 **Upload any file** — auto-converts on upload
- ⚡ **Instant Markdown output** with one-click copy
- 🌙 **Clean UI** built with Gradio
- 🔒 **No data stored** — files are processed in memory and discarded
- 🚀 **Live on HuggingFace Spaces** — no install needed

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

## 🚀 Run Locally

```bash
git clone https://github.com/Yaswanth-Boggarapu/markitdown-gui.git
cd markitdown-gui
pip install -r requirements.txt
python3 app.py
```

Opens at **http://localhost:7860**

---

## 🔧 How It Works

1. File is uploaded to a temporary path on the server
2. `MarkItDown.convert()` processes it and returns Markdown text
3. Output is displayed and copyable — file is discarded immediately after

---

## 🗂️ Project Structure

```
markitdown-gui/
├── app.py              # Gradio app
├── requirements.txt    # Python dependencies
├── .github/
│   └── workflows/
│       └── sync.yml    # CI/CD: auto-sync GitHub → HF Spaces on push
└── README.md
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| [`markitdown[all]`](https://github.com/microsoft/markitdown) | File → Markdown by Microsoft |
| [`gradio`](https://gradio.app) | Web UI framework |

---

## 🙏 Credits

- [**Microsoft AutoGen Team**](https://github.com/microsoft/markitdown) for MarkItDown
- Built by [Yaswanth Boggarapu](https://github.com/Yaswanth-Boggarapu)

---

## 📄 License

MIT
