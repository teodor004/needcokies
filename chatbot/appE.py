from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import openai

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

openai.api_key = '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'

@app.route("/")
def index():
    session['role'] = 'curious_child'
    session['count'] = 0  
    initial_question = "Hello! I was wondering, how do plants make sugar from sunlight?"
    return render_template('chat.html', initial_question=initial_question)

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form.get("msg", "").strip()
    session['count'] += 1  

    if session.get('role') == 'curious_child' and session['count'] <= 3:
        chat_messages = [
            {"role": "system", "content": "User: " + user_input},
            {"role": "user", "content": "And why is that important for the plant?"}
        ]
    else:
        
        chat_messages = [
            {"role": "system", "content": "User: " + user_input},
            {"role": "user", "content": "Oh, I see! Thanks for explaining that to me. I think I understand it now!"}
        ]
        session['role'] = 'understanding_child'  

    return jsonify(get_openai_response(chat_messages))

def get_openai_response(messages):
    try:
        context = "You are a curious child asking questions about science in a simple and playful way. Respond to the user's explanations with curiosity and simplicity, asking follow-up questions or expressing amazement like a child would."
        messages.insert(0, {"role": "system", "content": context})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100,
        )
        
        print("Full API Response:", response)
        
        
        if 'choices' in response and len(response['choices']) > 0 and 'message' in response['choices'][0]:
            return {"response": response['choices'][0]['message']['content']}
        else:
            return {"error": "Unexpected response format or missing data"}

    except Exception as e:
        print("Error occurred:", str(e))  
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=False)
