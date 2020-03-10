"""Main application file"""
from flask import Flask
app = Flask(__name__)

# Initialize Logger
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

@app.route('/<random_string>')
def returnBackwardsString(random_string):
    """"Reverse and return the provides URI"""
<<<<<<< HEAD
    LOGGER.info('Received a message: %s', random_string)
    return "".join(reversed(random_string))
=======
    return "Breaking the unit test"
>>>>>>> e475a8a2ec203157b97e477d1fb914b3af964b56

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)