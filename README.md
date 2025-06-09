# AI Chat Box

This is a Python-based AI chat system built with LangChain, supporting LLMs like OpenAI and Anthropic. It fetches information from tools like Wikipedia and DuckDuckGo and can be configured via `.env`.

---

## 🚀 Features

- Query LLMs using LangChain (OpenAI/Anthropic)
- Use tools like DuckDuckGo and Wikipedia
- Modular tool integration
- Environment config via `.env`

---

## 📁 Folder Structure

AI-chat-box/
├── main.py # Main entry point for the app
├── tool.py # Tool functions for external search or processing
├── requirments.txt # Python dependency list
├── sample.env # Template for environment config
├── documentation.txt # Full description of the system
├── README.md # Project overview (this file)
├── venv/ # Python virtual environment


---

## 🔧 Installation

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd AI-chat-box
2. Create & activate a virtual environment
   
   python3 -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows

3. Install dependencies

   pip install -r requirments.txt
   or
   pip3 install -r requirments.txt

4.Set up environment

  Copy sample.env to .env

  Add your API keys (OpenAI, Anthropic, etc.)

5.Run the application

  python main.py

  
Dependencies:

As listed in requriments.txt:

langchain, langchain-community, langchain-openai, langchain-anthropic

wikipedia, duckduckgo-search

python-dotenv, pydantic

👨‍💻 Author
Akshat Gupta
  
