# English+Khmer OCR

This is a code repository for an English+Khmer OCR (Optical Character Recognition) application. The application uses the Tesseract OCR engine and PIL (Python Imaging Library) to extract text from images containing both English and Khmer characters.

## Installation

1. Clone the repository:
```shell
git clone https://github.com/ShadowDominator/image-to-text-khmer-ocr.git
 ```
2. Install the required packages:
```shell
pip install pytesseract gradio pillow
```
Additionally, you will need to install Tesseract OCR on your system. Refer to the Tesseract installation guide for instructions specific to your operating system.
https://tesseract-ocr.github.io/tessdoc/Installation.html

## Usage
1. Import the necessary libraries:
```shell
from PIL import Image
import pytesseract
import gradio as gr
```
2. Define the OCR function:
```shell
def run_khm_eng(image):
    result = pytesseract.image_to_string(image, lang="khm+eng")
    return result
```

3. Create the Gradio interface:
``` shell
with gr.Blocks() as demo:
    gr.Markdown("## English+Khmer OCR")
    with gr.Row():
        with gr.Column():
            image_in = gr.Image(type="pil")
            btn = gr.Button("Run")
        with gr.Column():
            text_out = gr.TextArea()

    examples = gr.Examples([["./demo.png", None]], fn=run_khm_eng, inputs=[image_in], outputs=[text_out], cache_examples=False)
    btn.click(fn=run_khm_eng, inputs=[image_in], outputs=[text_out])

demo.launch()
```
4. Run 
```shell 
cd project_name
gradio app.py
```



