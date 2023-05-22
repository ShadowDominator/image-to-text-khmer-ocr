from PIL import Image
import pytesseract
import gradio as gr
blocks = gr.Blocks()
 
def run_khm_eng(image):
    result = pytesseract.image_to_string(
        image, lang="khm+eng")
    return result


with gr.Blocks() as demo:
    gr.Markdown("## English+Khmer OCR")
    with gr.Row():
        with gr.Column():
            image_in = gr.Image(type="pil")            
            btn = gr.Button("Run")
        with gr.Column():
            text_out = gr.TextArea()

    examples = gr.Examples([["./demo.png", None]], fn=run_khm_eng, inputs=[
                           image_in], outputs=[text_out], cache_examples=False)
    btn.click(fn=run_khm_eng, inputs=[image_in], outputs=[text_out])

demo.launch()
