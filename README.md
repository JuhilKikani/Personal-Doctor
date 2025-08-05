# 🩺 Personal Doctor - Your AI Health Assistant

**Link:** 🌐 [Live Demo](https://personal-doctor.onrender.com/)  

## 🧑‍💻 Tech Stack Details

| Layer        | Technology                   |
|--------------|-------------------------------|
| **Frontend** | HTML, CSS, JavaScript         |
| **Backend**  | Python Flask                  |
| **Database** | SQLite3                       |
| **LLM API**  | Gemini 2.5 Flash (via Google) |
| **Deployment** | Render                      |

---

## 🚀 Project Overview

**Personal Doctor** is a conversational web-based health assistant powered by **Gemini 2.5 Flash LLM API**. It mimics the behavior of a personal doctor by asking basic user information and providing a personalized and friendly response in Hinglish (Hindi + English). This project showcases how conversational AI can improve healthcare support and be used to build intelligent user-facing applications.

---

## 🎯 Features

- 🤖 AI-Powered Chatbot (LLM: Gemini 2.5 Flash)
- 💬 Interactive chat interface with real-time response
- 🗃️ Collects basic user info (Name, Age, Gender)
- 🌐 Multi-language interaction (primarily Hinglish)
- 🧠 Logic handled via Flask backend
- 📦 Lightweight database storage with SQLite3
- 🚀 Fully deployed on [Render](https://render.com)

---

## 📸 Preview

![Personal Doctor Screenshot](./static/Mobile%20view.png)  
> *Initial user interaction and LLM-generated response.*

---

## ⚙️ How It Works

1. User opens the site and can interact with AI "doctor".
2. The chatbot asks for basic details like name, age, and gender.
3. On user input, Flask handles the request and sends the data to Gemini API.
4. Gemini API generates a natural, friendly response based on context.
5. Flask returns the response and it's displayed on the UI dynamically.

---

## 📁 Project Structure

```bash
Personal-Doctor/
│
├── static/                # CSS and JS files
│   ├── style.css
│   └── script.js
│
├── templates/             # HTML templates
│   └── chat.html
│
├── app.py                 # Main Flask application
├── database.py            # SQLite3 database 
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
