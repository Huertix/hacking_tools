from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def get_data():
    content = request.json
    content["IP"] = request.remote_addr
    print(content)
    return jsonify({"id": content.get("visitorId")})

# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print content['mytext']
#     return jsonify({"uuid":uuid})

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=80)
