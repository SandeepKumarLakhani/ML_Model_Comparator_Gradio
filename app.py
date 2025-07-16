
import gradio as gr

def compare_models(input_text):
    # Simulated responses
    return f"Model A output for: {input_text}", f"Model B output for: {input_text}"

demo = gr.Interface(fn=compare_models, 
                    inputs="text", 
                    outputs=["text", "text"],
                    title="ML Model Comparator",
                    description="Compare outputs of two ML models side-by-side.")

demo.launch()
