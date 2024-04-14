from flask import Flask, render_template, request, jsonify

import openai

openai.api_key = "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"


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    chat_messages = [{'role': 'system', 'content': 'You are UTeach, a helpful assistant. You help teacher with scheduling their subjects, and manage their student better, based on the individual personality. '}, {'role': 'user', 'content': input}]
    return get_openai_response(chat_messages)


def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
    )

    return response['choices'][0]['message']['content']

   

if __name__ == '__main__':
    app.run()
