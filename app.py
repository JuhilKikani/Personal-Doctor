import sqlite3
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyDNlj7UBJlr86A2zOyc_W0RFJxakB6bQf0")

# Flask app setup
app = Flask(__name__)

# System instruction for personal doctor
system_instruction = """
Tum ek intelligent aur caring personal health doctor ho. Tumhara kaam hai users se unka naam, age aur gender puchhna sabse pehle. Uska answer aane k bad hi unse poochho ki unhe kya dikkat ho rahi hai — jaise bukhar, body pain, headache ya kuch aur.

Jab user apni problem bataye, toh uske basis pe follow-up questions karo — jaise “kab se ho raha hai?”, “kya sardi bhi hai?”, “kya koi aur health issue bhi hai?” Taaki tum unka health issue clearly samajh sako.

Fir unke symptoms, age aur gender ke hisaab se unhe possible condition batao (lekin professional doctor jaise claim mat karo). Fir simple language mein samjhao ki ye problem kyun ho sakti hai — jaise weather change, infection ya stress.

Uske baad unhe kuch mild medicine ya home remedy suggest karo. Saath mein ye bhi batao ki kya khana chahiye aur kya avoid karna chahiye recovery ke liye. Agar zarurat ho toh medicine lene ka simple time-table bhi batao.

Har baar last mein yeh kah do — "Yeh ek general advice hai, agar symptoms continue ho ya badh jaye toh please doctor se consult karo."

Saath hi unko thoda motivate bhi karo, jaise “Aram karo, sab theek ho jayega” ya “Pani zyada piyo, jaldi recover karoge.”

Conversation Hinglish mein rakho — matlab easy Hindi aur English mix jaisa real life mein log baat karte hain. And Dont use ** in output sentences, it is not converting bold in output so be careful.
"""

# Dictionary to hold per-user chat history
user_chats = {}

# Home route
@app.route('/')
def home():
    return render_template('chat.html')  # make sure chat.html exists in templates folder

# Ask route for AJAX requests
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get('message')
    username = data.get('username', 'Anonymous')

    # Initialize chat history if new user
    if username not in user_chats:
        user_chats[username] = [
            types.Content(role="model", parts=[types.Part(text=system_instruction)])
        ]

    # Append user message
    user_chats[username].append(
        types.Content(role="user", parts=[types.Part(text=user_input)])
    )

    # Generate Gemini response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_chats[username]
    )

    reply = response.text

    # Append model response to chat history
    user_chats[username].append(
        types.Content(role="model", parts=[types.Part(text=reply)])
    )

    # Save to database
    save_message(username, "You", user_input)
    save_message(username, "Doctor", reply)

    return jsonify({'reply': reply})

# Save message in SQLite
def save_message(username, sender, message):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO messages (username, sender, message) VALUES (?, ?, ?)",
        (username, sender, message)
    )
    conn.commit()
    conn.close()

# View history
@app.route("/history")
def view_history():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("SELECT * FROM messages ORDER BY timestamp")
    rows = c.fetchall()
    conn.close()

    history_html = "<h2>Chat History</h2><ul>"
    for row in rows:
        history_html += f"<li><strong>{row[1]} ({row[2]})</strong>: {row[3]} <em>({row[4]})</em></li>"
    history_html += "</ul>"

    return history_html

# Run app
if __name__ == '__main__':
    app.run(debug=True)
