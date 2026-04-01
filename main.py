from flask import Flask, request, jsonify
import os
import intell  # your backend

app = Flask(__name__)

@app.route('/')
def home():
    return "IntelliSecure Backend Running 🚀"

# 🔹 LOGIN API
@app.route('/login', methods=['POST'])
def login():
    try:
        result = intell.login()
        return jsonify({"status": result})
    except Exception as e:
        return jsonify({"error": str(e)})

# 🔹 REGISTER API
@app.route('/register', methods=['POST'])
def register():
    try:
        intell.register()
        return jsonify({"status": "registered"})
    except Exception as e:
        return jsonify({"error": str(e)})

# 🔹 VIEW ACCOUNTS
@app.route('/accounts')
def accounts():
    try:
        accounts = intell.readAccountsCSV()
        data = []
        for acc in accounts:
            data.append({
                "accNo": acc.accNo,
                "name": acc.name,
                "balance": acc.deposit
            })
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

# 🔹 TRANSACTIONS
@app.route('/transactions')
def transactions():
    try:
        intell.displayTransactions()
        return jsonify({"status": "printed in console"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)