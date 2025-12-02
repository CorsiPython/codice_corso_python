import gradio as gr


def dividi(a, b):

    if b == 0:
        raise gr.Error("Division by Zero")

    return a / b


def somma(a, op, b):

    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: dividi(x, y),
    }

    return ops[op](a, b)


app = gr.Interface(
    fn=somma,
    inputs=[
        gr.Number(label="A"),
        gr.Radio(["+", "-", "*", "/"], value="+"),
        gr.Number(label="B"),
    ],
    outputs=gr.Number(label="Result"),
    examples=[[4, "+", 3], [12, "/", 0], [100, "*", 0]],
    title="Python Calculator",
    description="## A *simple* way to perform basic arithmetic",
)

app.launch(theme=gr.themes.Origin())
