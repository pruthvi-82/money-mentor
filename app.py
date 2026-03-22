from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    income = int(data['income'])
    expenses = int(data['expenses'])
    goal = int(data.get('goal', 0))

    savings = income - expenses
    savings_percent = (savings / income) * 100

    # score logic
    if savings_percent > 20:
        score = 9
    elif savings_percent > 10:
        score = 6
    else:
        score = 3

    return jsonify({
        "savings": savings,
        "score": score,
        "message": "Try to reduce expenses and save more"
    })

app.run(debug=True)
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data['message']
    income = int(data.get('income', 0))
    expenses = int(data.get('expenses', 0))

    savings = income - expenses

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": f"User savings is ₹{savings}. Give financial advice."},
            {"role": "user", "content": user_msg}
        ]
    )

    return {"reply": response.choices[0].message.content}
