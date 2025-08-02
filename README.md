# 🤖 AI Assistant with LangChain & LangGraph

This project is a terminal-based AI assistant built using:
- [LangChain](https://www.langchain.com/) for managing prompts and tools
- [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration
- [OpenAI API](https://platform.openai.com/) as the backend LLM
- [Python](https://www.python.org/) for development

## 💡 Features

The assistant can:
- 🔢 Perform basic arithmetic (calculator)
- 📏 Convert meters to feet
- ⏰ Tell the current time and date
- 📝 Summarize short text
- 😂 Tell random programming jokes
- 🙋 Greet the user by name

## 🧪 Example Interactions

```bash
You: Add 10 and 25  
Assistant: The result of adding 10.0 and 25.0 is 35.0

You: Convert 5 meters to feet  
Assistant: 5.0 meters is equal to 16.40 feet

You: What’s the current time?  
Assistant: Current date and time: 2025-08-03 00:30:00

You: Summarize this: LangChain is a framework for developing LLM-based applications...  
Assistant: Summary: LangChain is a framework for developing LLM-b...

You: Tell me a joke  
Assistant: Why do programmers prefer dark mode? Because light attracts bugs!

You: Greet Arsh  
Assistant: Hello Arsh! I'm happy to assist you today 😊
```
## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Arsh-pixel-cmd/ai-assistant-langchain.git
cd ai-assistant-langchain
```
### 2. Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### Or if you're using uv:
```bash
uv pip install -r pyproject.toml
```
### 4. Add .env File
#### Create a .env file and add your OpenAI API key:
.env
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
### 5. Run the Assistant
```bash
python main.py
```

## 📁 Project Structure
.
├── main.py              # Main assistant logic
├── pyproject.toml       # Dependency and project metadata
├── .gitignore           # Ignored files and folders
├── .env                 # Contains your OpenAI API Key (excluded from Git)
├── .venv/               # Virtual environment (excluded)
├── .mypy_cache/         # Cache (excluded)
└── README.md            # You're reading this!

## 📜 License
This project is licensed under the MIT License.
