from flask import Flask
app = Flask(__name__)

# https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/


@app.route('/')
def hello_world():
    return 'Hello! Welcome to my portfolio project, "Plant Shop" - Utilizing Docker in VS Code with Flask!'


def index_customers():
    return 'This is the page to index existing customers or create new ones.'


app.add_url_rule('/get-customers', 'index_customers', index_customers)


def index_plants():
    return 'This is the page to index existing plants or create new ones.'


app.add_url_rule('/get-plants', 'index_plants', index_plants)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
