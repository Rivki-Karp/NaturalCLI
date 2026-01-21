import os
from dotenv import load_dotenv
import openai
import gradio as gr

# טוען את משתני הסביבה
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# יצירת client עם פרוקסי
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://proxy.aiwall.org"  # משתמש בפרוקסי
)

# קריאה של קובץ ה-Markdown עם ההנחיות
try:
    with open("instarction2.md", "r", encoding="utf-8") as f:
    instructions = f.read()
except FileNotFoundError:
    instructions = "You are a helpful assistant."

# פונקציה לשאילת שאלות למודל
def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",  # בחר מודל זמין מהרשימה שלך
                  messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# ממשק Gradio
iface = gr.Interface(
    fn=ask_openai,
    inputs=gr.Textbox(lines=5, placeholder="כתוב כאן את השאלה שלך..."),
    outputs=gr.Textbox(label="תשובה מהמודל"),
    title="OpenAI Chat דרך פרוקסי",
    description="ממשק לשאילת שאלות למודל OpenAI דרך פרוקסי"
)

if __name__ == "__main__":
    iface.launch()
