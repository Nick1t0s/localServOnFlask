from flask import Flask
import sys
sys.stdout = open("C:\\winTest\\localserver\\output.txt", "w")
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()
sys.stdout.close()
