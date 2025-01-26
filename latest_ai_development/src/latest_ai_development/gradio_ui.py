
import gradio as gr
import os
from dotenv import load_dotenv
# import outputs
# from openai import OpenAI
import sambanova_gradio as gt
# gr.load("Meta-Llama-3.1-8B-Instruct", src=sambanova_gradio.registry, accept_token=False)

from latest_ai_development.main import run  # Import the run_search_task function from main.py


# client = openai.OpenAI(
#     api_key=os.environ.get("SAMBANOVA_API_KEY"),
#     base_url="https://api.sambanova.ai/v1",
# )


load_dotenv()
MODEL_NAME = os.getenv("MODEL")
SAMBANOVA_API_KEY = os.getenv("SAMBANOVA_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")


# import sambanova_gradio as gt
# gr.load("Meta-Llama-3.1-8B-Instruct", src=sambanova_gradio.registry, accept_token=False)

# client = openai.OpenAI(
#     api_key=os.environ.get("SAMBANOVA_API_KEY"),
#     base_url="https://api.sambanova.ai/v1",
# )

from latest_ai_development.main import run  # Import the run_search_task function from main.py

def run_gradio_search_task(topic):
    """
    Gradio function to run the search task and display the result.
    """
    # topic = input("Enter the topic you want news on:")
    try:
        result = run(topic)  # Call the function from main.py
        return result
    except Exception as e:
        return f"Error: {e}"

# Create the Gradio interface
interface = gr.Interface(
    fn=run_gradio_search_task,  # The function that Gradio will call
    inputs=gr.Textbox(label="Enter Topic for Research Task"),  # User input
    outputs=gr.Textbox(label="ParaLegal may make mistakes, so please use it at your own discretion"),  # Display the result
)


# Launch the Gradio app
if __name__ == "__main__":
    interface.launch(share=True)  # share=True for a public link