import gradio as gr

def greet(line,wav):
    print(wav)
    return "hello"

iface = gr.Interface(fn=greet,inputs=[gr.Textbox(),gr.Audio(type="filepath")],outputs=gr.Video())
iface.launch()
