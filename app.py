import gradio as gr
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown()

SUPPORTED = [
    ".pdf", ".docx", ".doc", ".pptx", ".ppt",
    ".xlsx", ".xls", ".html", ".htm", ".csv",
    ".json", ".xml", ".zip", ".epub",
    ".jpg", ".jpeg", ".png", ".gif",
    ".mp3", ".wav"
]

def convert(file):
    if file is None:
        return "No file uploaded."
    ext = Path(file.name).suffix.lower()
    if ext not in SUPPORTED:
        return f"❌ Unsupported format: `{ext}`\n\nSupported: {', '.join(SUPPORTED)}"
    try:
        result = md.convert(file.name)
        return result.text_content
    except Exception as e:
        return f"❌ Error: {str(e)}"

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="violet",
        neutral_hue="slate",
    ),
    title="MarkItDown",
    css="""
    .gr-button-primary { background: #7c6af7 !important; border: none !important; }
    footer { display: none !important; }
    """
) as demo:

    gr.Markdown("""
# ⬡ MarkItDown
**Convert any file to Markdown — local processing, no data stored.**

Supports: PDF · DOCX · PPTX · XLSX · HTML · CSV · JSON · XML · ZIP · EPUB · Images · Audio
""")

    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(
                label="Upload File",
                file_types=SUPPORTED,
            )
            convert_btn = gr.Button("▶ Convert to Markdown", variant="primary")

        with gr.Column(scale=2):
            output = gr.Textbox(
                label="Markdown Output",
                lines=28,
                show_copy_button=True,
                placeholder="Converted Markdown will appear here…",
            )

    convert_btn.click(fn=convert, inputs=file_input, outputs=output)
    file_input.change(fn=convert, inputs=file_input, outputs=output)

    gr.Markdown("""
---
Built by [Yaswanth Boggarapu](https://github.com/Yaswanth-Boggarapu) · 
Powered by [microsoft/markitdown](https://github.com/microsoft/markitdown)
""")

if __name__ == "__main__":
    demo.launch()
