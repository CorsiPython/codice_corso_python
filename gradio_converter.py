import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("## Convertitore Celsius → Fahrenheit")
    with gr.Row():
        with gr.Column():
            celsius = gr.Number(label="°C")
        with gr.Column():
            fahrenheit = gr.Number(label="°F")
            converti = gr.Button("Converti")

    def to_f(value):
        return value * 9 / 5 + 32

    converti.click(fn=to_f, inputs=celsius, outputs=fahrenheit)

demo.launch()
