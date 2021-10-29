from flask import Flask, jsonify, request, render_template, url_for
from dialogflow_services import detect_intent_texts

# Create Flask app
app = Flask(__name__)

# Create session for dialogflow
session_id = 123456
chat_logs = []

@app.route('/', methods=['GET', 'POST'] )
def index():
    return "<p>Hello World</p>"

@app.route('/chatbot', methods=['GET', 'POST'] )
def sendMessageToChatbot():
    userQuery = ''
    chatbotResponse = ''
    
    if request.method == 'GET':
        chatbotResponse = 'Hello USER, feel free to ask me any questions!'
        chat_logs.append(['Chatbot', chatbotResponse])

    elif request.method == 'POST':
        userQuery = request.form.get('userMessage')
        if not userQuery == '':
            chatbotResponse = detect_intent_texts(session_id, [userQuery])
            chat_logs.append(['User', userQuery])
            chat_logs.append(['Chatbot', chatbotResponse])

    return render_template('index.html', logs=chat_logs)

if __name__ == '__main__':
    app.run(debug=True)