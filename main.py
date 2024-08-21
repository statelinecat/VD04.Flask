from flask import Flask

from datetime import datetime

app = Flask(__name__)

@app.route('/')

def current_datetime():

    now = datetime.now()

    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    return f'Current date and time: {date_time}'

if __name__ == '__main__':

    app.run()

