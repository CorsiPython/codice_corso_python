import gradio as gr

with gr.Blocks() as demo:
    input_box = gr.Textbox()
    output_box = gr.Textbox()
    btn = gr.Button("Run")

    def process(text):
        return text.upper()

    btn.click(process, inputs=input_box, outputs=output_box)

demo.launch()
