import os
#from dotenv import load_dotenv
import openai
import gradio as gr

# Load environment variables
api_key = os.environ["OPENAI_API_KEY"]

# Create client with a proxy
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://proxy.aiwall.org"  # Uses a proxy
)

# Read the Markdown file containing the instructions
try:
    with open("instarction2.md", "r", encoding="utf-8") as f:
        instructions = f.read()
except FileNotFoundError:
    instructions = "You are a helpful assistant."

# Function to query the model
def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1", 
                  messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
iface = gr.Interface(
    fn=ask_openai,
    inputs=gr.Textbox(lines=5, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Model Response"),
    title="NaturalCLI Chat",
    description="Converts natural language input into CLI commands."
)

if __name__ == "__main__":
    iface.launch()
