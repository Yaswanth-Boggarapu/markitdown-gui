<div align="center">

# ⬡ MarkItDown GUI

**A local macOS desktop app to convert any file to Markdown**  
Built on [Microsoft's MarkItDown](https://github.com/microsoft/markitdown) · Dark mode · No internet required

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey?logo=apple)](https://apple.com/macos)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![MarkItDown](https://img.shields.io/badge/Powered%20by-MarkItDown-blueviolet)](https://github.com/microsoft/markitdown)

</div>

---

## ✨ Features

- 📂 **Browse or drag & drop** any file into the app
- ⚡ **One-click conversion** to clean Markdown
- 💾 **Save as `.md`** or **copy to clipboard** instantly
- 🌙 **Dark mode UI** — easy on the eyes
- 🔒 **Fully local** — no data leaves your machine
- 📦 **Packaged as a `.dmg`** — drag to Applications and run

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

## 🚀 Build the DMG (on your Mac)

### Prerequisites

- macOS 11+
- Python 3.10+ — [download here](https://python.org) if needed

### Steps

```bash
# 1. Clone this repo
git clone https://github.com/Yaswanth-Boggarapu/markitdown-gui.git
cd markitdown-gui

# 2. Make the build script executable
chmod +x build.sh

# 3. Run it
./build.sh
```

The script will automatically:
1. Install `markitdown[all]`, `pyinstaller`, and `dmgbuild`
2. Build `MarkItDown.app` via PyInstaller
3. Package it into `MarkItDown.dmg`

### Install the App

1. Double-click `MarkItDown.dmg`
2. Drag `MarkItDown.app` → `/Applications`
3. First launch: **right-click → Open** (to bypass Gatekeeper on unsigned apps)

---

## 🖥️ Run Without Building (Dev Mode)

```bash
pip install 'markitdown[all]'
python3 app.py
```

---

## 🗂️ Project Structure

```
markitdown-gui/
├── app.py              # Main GUI application (tkinter, dark mode)
├── markitdown.spec     # PyInstaller bundle config for macOS .app
├── build.sh            # One-command build script → .app + .dmg
└── README.md
```

---

## 🔧 How It Works

1. `app.py` — tkinter GUI that calls `MarkItDown.convert(filepath)` in a background thread
2. `markitdown.spec` — PyInstaller spec that bundles the app + all dependencies into `MarkItDown.app`
3. `build.sh` — shell script that installs deps, runs PyInstaller, then uses `dmgbuild` to wrap it into a distributable `.dmg`

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| [`markitdown[all]`](https://github.com/microsoft/markitdown) | File → Markdown conversion engine by Microsoft |
| [`pyinstaller`](https://pyinstaller.org) | Packages Python app into standalone `.app` |
| [`dmgbuild`](https://github.com/al45tair/dmgbuild) | Creates macOS `.dmg` disk image |

---

## 🙏 Credits

- [**Microsoft AutoGen Team**](https://github.com/microsoft/markitdown) for the MarkItDown library
- Built by [Yaswanth Boggarapu](https://github.com/Yaswanth-Boggarapu)

---

## 📄 License

MIT — free to use, modify, and distribute.
