from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Network test to Pod1"

if __name__ == "__main__":
    application.run()
