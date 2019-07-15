from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask World!"


@app.route("/generic-metrics")
def get_generic_metrics():
    return jsonify([
        {
            'key': 'memory_used_mbs',
            'help': 'The service memory used, unit mbs.',
            'value': 500,
            'status': 'ok',
            'node': 'hci1'
        },
        {
            'key': 'memory_used_mbs',
            'help': 'The service memory used, unit mbs.',
            'value': 100,
            'status': 'ok',
            'node': 'hci2'
        },
        {
            'key': 'disk_used_gbs',
            'help': 'The service disk used, unit mbs.',
            'value': 200,
            'status': 'ok',
            'node': 'hci3',
            'disk': 'dva'
        }
    ])


app.run(host="0.0.0.0", port=5000)
