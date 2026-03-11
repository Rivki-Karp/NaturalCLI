# 🚀 NaturalCLI: Natural Language to CLI Agent

**NaturalCLI** is an intelligent agent designed to bridge the gap between human language and the command-line interface (CLI). This system takes simple, natural language inputs and accurately translates them into executable CLI commands.

## ✨ Key Features
* **Natural Language Translation:** Effortlessly convert phrases like *"create a new folder named project"* into the command `mkdir project`.
* **High Precision:** Optimized to match the intent with the correct syntax of common CLI tools.
* **Safety First:** Includes a robust validation mechanism—if an input is irrelevant or potentially unsafe, the system responds with `UNKNOWN_COMMAND`.
* **User-Friendly Interface:** Built with **Gradio**, providing a clean and intuitive web-based UI.
* **Cloud Deployment:** Fully compatible and deployed on **Hugging Face Spaces**.

## 🛠 Tech Stack
* **Python:** The core logic of the agent.
* **Gradio:** Used for creating the interactive web interface.
* **LLM Integration:** Powered by advanced language models to interpret intent.
* **GitHub Actions:** Automated "Keep-Alive" workflow to ensure service availability.

## 🚀 Getting Started

### Local Installation
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Rivka-Karp/NaturalCLI.git](https://github.com/Rivka-Karp/NaturalCLI.git)
    cd NaturalCLI/cliAgent
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set Environment Variables:**
    Ensure your API key is configured:
    ```bash
    export OPENAI_API_KEY='your_api_key_here'
    ```
4.  **Run the Application:**
    ```bash
    python main.py
    ```

## 🖥 Usage Examples

| User Input (Natural Language) | System Output (CLI Command) |
| :--- | :--- |
| "Show me all files in the current folder" | `ls -a` |
| "Delete the file named old_data.txt" | `rm old_data.txt` |
| "What is the best recipe for pizza?" | `UNKNOWN_COMMAND` |

## 🌐 Live Demo
The project is hosted on Hugging Face. You can access the live version here:
👉 [NaturalCLI on Hugging Face](https://huggingface.co/spaces/Rivka-Karp/NaturalCLI)

---

### 📝 Maintenance Note
This repository includes a specialized **GitHub Action** located in `.github/workflows/keep_alive.yml`. This workflow pings the Hugging Face Space every 24 hours to prevent the free-tier instance from entering "Sleep Mode," ensuring the agent is always ready for use.
