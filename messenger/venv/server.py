from flask import Flask


app = Flask(__name__)
msg = "hi"


@app.route("/")
def ping():
    return "Ping: OK"

@app.route("/messages")
def messages_view():
    return msg

if __name__ == '__main__':
    app.run()
