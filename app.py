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