from flask import Flask, request, send_file, Response
import json
import logging

logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_test():
    logger.info(f"testin' around I guess")
    return send_file("index.html")


@app.route("/<exp_id>", methods=["GET"])
def index(exp_id):
    logger.info(f"measuring {exp_id}")
    return send_file("index.html")


@app.route("/<exp_id>", methods=["POST"])
def save(exp_id):
    data = json.loads(request.data)
    logger.info(f"dumping data for {exp_id}")
    with open(f"./data/{exp_id}_{data[-1].get('time')}.log", "wb") as f:
        f.write(request.data)
    return "ack"


if __name__ == "__main__":
    app.run(debug=True)
