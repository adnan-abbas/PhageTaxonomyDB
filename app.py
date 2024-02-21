from flask import Flask

app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
