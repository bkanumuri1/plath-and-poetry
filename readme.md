Try it out here: https://plathandpoetry.streamlit.app/

# 📝 Plath & Poetry: An AI-Powered Poem Generator

**Plath & Poetry** is a generative AI app that creates emotionally rich, two-line poems inspired by the haunting style of Sylvia Plath. Built with OpenAI's GPT-3.5 Turbo, LangChain, and Streamlit, this project blends large language models with artistic expression.

> “Whether you want a spark of melancholy or a poetic lift of hope — let AI channel Sylvia for you.”

---

## 🚀 Features

- 🧠 **Contextual Memory**: Remembers past prompts within a session to generate thematically connected poems.
- 🎭 **Sylvia Plath Style**: System prompt engineering imitates Plath’s poetic voice and tone.
- 🌐 **Streamlit Interface**: Simple, responsive UI for real-time interaction.
- 🪄 **LangChain Integration**: Uses structured prompt chaining and memory for dynamic, responsive LLM behavior.

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-3.5 Turbo
- **AI Framework**: LangChain
- **Memory**: `ConversationBufferMemory` + `StreamlitChatMessageHistory`
- **Deployment-ready**: Works locally or on platforms like Streamlit Cloud

---

## 📦 Project Structure

```text
plath-and-poetry/
├── chatbot/
│   ├── app.py              # Main Streamlit app with memory + LLM integration
│   └── localllama.py       # (Optional) Local OLlama script
├── .devcontainer/
│   └── devcontainer.json   # VS Code dev container config
├── .env                    # Your API keys (excluded via .gitignore)
├── .gitattributes
├── .gitignore              # Prevents sensitive/config files from being committed
├── readme.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/bkanumuri1/plath-and-poetry.git
cd plath-and-poetry
```

### 2. Set Up Environment Variables

Create a .env file using the example:

```bash
cp .env.example .env
```

Then fill in your OpenAI and LangChain keys:

```bash
OPENAI_API_KEY=your_openai_key
LANGCHAIN_API_KEY=your_langchain_key
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🎯 Why I Built This

As a software engineer with a passion for AI, I wanted to explore how language models could be used for creative self-expression. This project allowed me to apply my knowledge of LangChain and LLM APIs in a poetic and emotionally resonant way.

## 🧠 Next Up

🎛 Mood/style selector

- lets users select a mood for the poem e.g., melancholic, hopeful, dark, playful, surreal

📜 Multi-line/ Dynamic Length Output

- lets users select how many lines they want e.g. 2,4, or a haiku.

🔗 Export & Share Options

- allows users to copy/share poems.

## 🔒 Security

This project uses environment variables to protect API keys. The .env file is excluded via .gitignore. Do not commit your keys to GitHub.
