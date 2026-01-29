# 🤖 Multi-Agent AI System

A professional Streamlit-based portfolio application showcasing a multi-agent AI system with Web Agent and Finance Agent working together, powered by Phi Agent Framework and Groq LLM.

## 🌟 Features

- **Multi-Agent Collaboration**: Web Agent + Finance Agent + Team Coordinator
- **Real-time Analysis**: Get instant market insights and comprehensive information
- **Interactive UI**: Modern, responsive design with quick-access buttons
- **Chat History**: Track all your queries and responses
- **Professional Dashboard**: Portfolio-ready application with clean UX/UI
- **Error Handling**: Robust logging and error recovery mechanisms

## 📁 Project Structure

```
multi-agent-system/
├── app.py                 # Streamlit UI and interface logic
├── main.py                # Agent initialization and business logic
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variable template
├── .env                  # Your API keys (gitignored)
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API Key (Get one free at [console.groq.com](https://console.groq.com/))

### Installation

1. **Clone or download this repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your Groq API key
# GROQ_API_KEY=your_actual_api_key_here
```

4. **Test the agents (optional)**
```bash
python main.py
```

5. **Run the application**
```bash
streamlit run app.py
```

6. **Open your browser**
The app will automatically open at `http://localhost:8501`

## 📖 How to Use

### Quick Analysis
Click any of the quick-access buttons for instant analysis:
- **NVDA Analysis**: NVIDIA stock information
- **AAPL Insights**: Apple stock insights
- **TSLA Report**: Tesla stock report
- **Market Categories**: Tech Stocks, Market Overview, Economic News, Global Markets

### Custom Query
Type your own query in the search box for customized analysis.

### View History
Review past queries in the expandable chat history section.

## 🛠️ File Descriptions

### `main.py` - Business Logic
Contains all agent-related functionality:
- `check_api_key()`: Validates API key presence
- `initialize_agents()`: Creates Web Agent, Finance Agent, and Team Coordinator
- `process_agent_query()`: Handles query processing with error recovery
- `test_agents()`: Tests agent functionality

### `app.py` - User Interface
Contains all Streamlit UI components:
- `render_sidebar()`: Sidebar with agent info and stats
- `render_quick_actions()`: Quick analysis buttons
- `render_query_input()`: Custom query input section
- `process_query()`: Query processing workflow
- `render_chat_history()`: Chat history display
- `render_footer()`: Footer information

## 🎯 Agent Architecture

### Web Agent 🌐
- Searches for current information
- Provides comprehensive data from knowledge base
- Includes sources and URLs

### Finance Agent 💰
- Analyzes financial data
- Creates formatted tables
- Provides metrics and statistics

### Team Coordinator 🤝
- Orchestrates agent collaboration
- Handles agent failures gracefully
- Provides comprehensive answers

## 📊 Example Queries

Try these queries to explore the system's capabilities:

- "Provide detailed analysis and recent information about NVDA stock"
- "What are the current trends in major technology stocks?"
- "Provide an overview of current stock market conditions"
- "Compare AAPL and MSFT performance"
- "What are the latest important economic developments?"

## 🔧 Technology Stack

- **Frontend**: Streamlit
- **AI Framework**: Phi Agent Framework
- **LLM**: Groq (LLaMA 3.3 70B)
- **Language**: Python 3.8+
- **Logging**: Python logging module

## 🎓 Highlights

This project demonstrates:

✅ **Modular code architecture** (separate UI and business logic)  
✅ **Multi-agent AI system design**  
✅ **Professional error handling and logging**  
✅ **State management in Streamlit**  
✅ **API integration best practices**  
✅ **Clean code principles**  
✅ **Professional UI/UX design**

## 👨‍💻  Profile

**Asadullah Shehbaz**  
AI Engineer

- 🎓 8th Semester BSCS Student
- 📚 8 Months of AI/ML Learning Journey
- 💼 Completed 2 Remote ML Internships
- 🏆 Kaggle Notebook & Dataset Expert
- 🚀 Passionate about AI Engineering

