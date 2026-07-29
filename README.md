# 🤖 MoodBot AI

An interactive AI chatbot built using **Streamlit**, **LangChain**, and **Mistral AI**. Choose your chatbot's mood and have a unique conversation based on its personality.

## ✨ Features

- Choose from multiple AI moods:
  - 😂 Funny
  - 😡 Angry
  - 😢 Sad
- Real-time conversational interface
- Chat memory using LangChain message history
- Automatically resets conversation when the mood changes
- Clear chat functionality
- Built with Streamlit for a clean and responsive UI

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- python-dotenv

## 📂 Project Structure

```
AIChatbot/
│── chatbot.py
│── requirements.txt
│── .env
│── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AIChatbot.git
cd AIChatbot
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
MISTRAL_API_KEY=your_api_key_here
```

Get your API key from the Mistral AI platform.

### 5. Run the application

```bash
streamlit run chatbot.py
```

The application will open automatically in your browser.

## 🎭 Available AI Personalities

| Mood | Behavior |
|------|----------|
| 😂 Funny | Responds with humor and jokes |
| 😡 Angry | Responds aggressively and impatiently |
| 😢 Sad | Responds with sadness and sorrow |

## 📦 Requirements

- Python 3.10+
- Streamlit
- LangChain
- LangChain Mistral
- python-dotenv

---

Made with ❤️ using Streamlit, LangChain, and Mistral AI.