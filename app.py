import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import sys
from pathlib import Path


def get_markitdown():
    try:
        from markitdown import MarkItDown
        return MarkItDown()
    except ImportError:
        return None


SUPPORTED_EXTENSIONS = [
    ("All Supported Files",
     "*.pdf *.docx *.doc *.pptx *.ppt *.xlsx *.xls *.html *.htm "
     "*.csv *.json *.xml *.zip *.epub *.jpg *.jpeg *.png *.gif *.mp3 *.wav"),
    ("PDF Files", "*.pdf"),
    ("Word Documents", "*.docx *.doc"),
    ("PowerPoint", "*.pptx *.ppt"),
    ("Excel", "*.xlsx *.xls"),
    ("HTML", "*.html *.htm"),
    ("CSV / JSON / XML", "*.csv *.json *.xml"),
    ("Images", "*.jpg *.jpeg *.png *.gif"),
    ("Audio", "*.mp3 *.wav"),
    ("ZIP / EPUB", "*.zip *.epub"),
    ("All Files", "*.*"),
]

BG         = "#1e1e2e"
SURFACE    = "#2a2a3d"
ACCENT     = "#7c6af7"
ACCENT_HOV = "#6a58e0"
TEXT       = "#cdd6f4"
SUBTEXT    = "#a6adc8"
SUCCESS    = "#a6e3a1"
ERROR      = "#f38ba8"
BORDER     = "#45475a"


class MarkItDownApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MarkItDown")
        self.geometry("940x680")
        self.minsize(700, 500)
        self.configure(bg=BG)

        self.md = get_markitdown()
        self.current_file = None
        self.converting = False

        self._build_ui()
        self._check_markitdown()

    # ------------------------------------------------------------------ #
    #  UI                                                                  #
    # ------------------------------------------------------------------ #
    def _build_ui(self):
        # ── title bar ──────────────────────────────────────────────────
        header = tk.Frame(self, bg=SURFACE, pady=14)
        header.pack(fill="x")

        tk.Label(
            header, text="⬡  MarkItDown",
            font=("SF Pro Display", 20, "bold"),
            fg=ACCENT, bg=SURFACE
        ).pack(side="left", padx=20)

        tk.Label(
            header, text="Convert any file to Markdown  ·  Local & Private",
            font=("SF Pro Text", 12),
            fg=SUBTEXT, bg=SURFACE
        ).pack(side="left", padx=4)

        # ── drop zone ──────────────────────────────────────────────────
        drop_frame = tk.Frame(self, bg=BG, pady=10)
        drop_frame.pack(fill="x", padx=20)

        self.drop_zone = tk.Frame(
            drop_frame, bg=SURFACE,
            highlightbackground=BORDER, highlightthickness=1,
            cursor="hand2", pady=28
        )
        self.drop_zone.pack(fill="x")

        tk.Label(
            self.drop_zone,
            text="📂  Drop a file here  or",
            font=("SF Pro Text", 13), fg=SUBTEXT, bg=SURFACE
        ).pack(side="left", padx=(40, 8))

        self.browse_btn = tk.Button(
            self.drop_zone,
            text="Browse",
            font=("SF Pro Text", 13, "bold"),
            fg="white", bg=ACCENT,
            activebackground=ACCENT_HOV, activeforeground="white",
            relief="flat", padx=16, pady=6,
            cursor="hand2",
            command=self._browse
        )
        self.browse_btn.pack(side="left")

        self.file_label = tk.Label(
            self.drop_zone, text="",
            font=("SF Pro Text", 12), fg=SUBTEXT, bg=SURFACE
        )
        self.file_label.pack(side="left", padx=16)

        # ── convert button ─────────────────────────────────────────────
        btn_row = tk.Frame(self, bg=BG)
        btn_row.pack(fill="x", padx=20, pady=(6, 0))

        self.convert_btn = tk.Button(
            btn_row,
            text="▶  Convert to Markdown",
            font=("SF Pro Text", 13, "bold"),
            fg="white", bg=ACCENT,
            activebackground=ACCENT_HOV, activeforeground="white",
            relief="flat", padx=22, pady=10,
            cursor="hand2",
            state="disabled",
            command=self._convert
        )
        self.convert_btn.pack(side="left")

        self.save_btn = tk.Button(
            btn_row,
            text="💾  Save .md",
            font=("SF Pro Text", 13),
            fg=TEXT, bg=SURFACE,
            activebackground=BORDER, activeforeground=TEXT,
            relief="flat", padx=16, pady=10,
            cursor="hand2",
            state="disabled",
            command=self._save
        )
        self.save_btn.pack(side="left", padx=(10, 0))

        self.copy_btn = tk.Button(
            btn_row,
            text="📋  Copy",
            font=("SF Pro Text", 13),
            fg=TEXT, bg=SURFACE,
            activebackground=BORDER, activeforeground=TEXT,
            relief="flat", padx=16, pady=10,
            cursor="hand2",
            state="disabled",
            command=self._copy
        )
        self.copy_btn.pack(side="left", padx=(10, 0))

        self.clear_btn = tk.Button(
            btn_row,
            text="✕  Clear",
            font=("SF Pro Text", 13),
            fg=SUBTEXT, bg=SURFACE,
            activebackground=BORDER, activeforeground=TEXT,
            relief="flat", padx=16, pady=10,
            cursor="hand2",
            command=self._clear
        )
        self.clear_btn.pack(side="right")

        # ── status bar ─────────────────────────────────────────────────
        self.status_var = tk.StringVar(value="Ready")
        self.status_bar = tk.Label(
            self, textvariable=self.status_var,
            font=("SF Pro Text", 11), fg=SUBTEXT, bg=SURFACE,
            anchor="w", padx=16, pady=6
        )
        self.status_bar.pack(fill="x", side="bottom")

        # ── progress bar ───────────────────────────────────────────────
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor=SURFACE, background=ACCENT,
            bordercolor=SURFACE, lightcolor=ACCENT, darkcolor=ACCENT
        )
        self.progress = ttk.Progressbar(
            self, style="Custom.Horizontal.TProgressbar",
            mode="indeterminate", length=200
        )
        self.progress.pack(fill="x", side="bottom")

        # ── output text area ───────────────────────────────────────────
        out_frame = tk.Frame(self, bg=BG)
        out_frame.pack(fill="both", expand=True, padx=20, pady=(10, 4))

        tk.Label(
            out_frame, text="OUTPUT",
            font=("SF Mono", 10, "bold"),
            fg=SUBTEXT, bg=BG
        ).pack(anchor="w", pady=(0, 4))

        self.output = scrolledtext.ScrolledText(
            out_frame,
            font=("SF Mono", 12),
            fg=TEXT, bg=SURFACE,
            insertbackground=ACCENT,
            relief="flat",
            wrap="word",
            padx=12, pady=10,
            state="disabled"
        )
        self.output.pack(fill="both", expand=True)

    # ------------------------------------------------------------------ #
    #  Helpers                                                             #
    # ------------------------------------------------------------------ #
    def _check_markitdown(self):
        if not self.md:
            self._set_status(
                "⚠  markitdown not installed — run: pip install 'markitdown[all]'",
                color=ERROR
            )

    def _set_status(self, msg, color=None):
        self.status_var.set(f"  {msg}")
        self.status_bar.configure(fg=color or SUBTEXT)

    def _set_output(self, text):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.configure(state="disabled")

    def _browse(self):
        path = filedialog.askopenfilename(filetypes=SUPPORTED_EXTENSIONS)
        if path:
            self._load_file(path)

    def _load_file(self, path):
        self.current_file = path
        name = Path(path).name
        self.file_label.configure(text=name, fg=TEXT)
        self.convert_btn.configure(state="normal")
        self._set_status(f"Loaded: {name}")

    def _convert(self):
        if not self.current_file or self.converting:
            return
        self.converting = True
        self.convert_btn.configure(state="disabled", text="Converting…")
        self.save_btn.configure(state="disabled")
        self.copy_btn.configure(state="disabled")
        self.progress.start(12)
        self._set_status("Converting…", color=ACCENT)

        threading.Thread(target=self._do_convert, daemon=True).start()

    def _do_convert(self):
        try:
            result = self.md.convert(self.current_file)
            md_text = result.text_content
            self.after(0, self._on_success, md_text)
        except Exception as e:
            self.after(0, self._on_error, str(e))

    def _on_success(self, md_text):
        self.converting = False
        self.progress.stop()
        self._set_output(md_text)
        lines = md_text.count("\n")
        words = len(md_text.split())
        self._set_status(
            f"✓  Done — {lines} lines · {words} words · {len(md_text)} chars",
            color=SUCCESS
        )
        self.convert_btn.configure(state="normal", text="▶  Convert to Markdown")
        self.save_btn.configure(state="normal")
        self.copy_btn.configure(state="normal")

    def _on_error(self, err):
        self.converting = False
        self.progress.stop()
        self._set_status(f"✗  Error: {err}", color=ERROR)
        self.convert_btn.configure(state="normal", text="▶  Convert to Markdown")

    def _save(self):
        default = Path(self.current_file).stem + ".md" if self.current_file else "output.md"
        path = filedialog.asksaveasfilename(
            defaultextension=".md",
            initialfile=default,
            filetypes=[("Markdown", "*.md"), ("Text", "*.txt")]
        )
        if path:
            content = self.output.get("1.0", "end")
            Path(path).write_text(content, encoding="utf-8")
            self._set_status(f"✓  Saved to {path}", color=SUCCESS)

    def _copy(self):
        content = self.output.get("1.0", "end")
        self.clipboard_clear()
        self.clipboard_append(content)
        self._set_status("✓  Copied to clipboard!", color=SUCCESS)

    def _clear(self):
        self.current_file = None
        self.file_label.configure(text="", fg=SUBTEXT)
        self._set_output("")
        self.convert_btn.configure(state="disabled")
        self.save_btn.configure(state="disabled")
        self.copy_btn.configure(state="disabled")
        self._set_status("Ready")


if __name__ == "__main__":
    app = MarkItDownApp()
    app.mainloop()
