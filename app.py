from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
#app.config.from_object(config.config['development'])

#app.register_error_handler(404, page_not_found)

app.config['MYSQL_HOST'] = 'localhost'
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "phagetaxonomy"
app.config["MYSQL_DB"] = "ptdb"
# Extra configs, optional:
#app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    cur = mysql.connection.cursor()
    #cur.execute("INSERT INTO Genome VALUES (123456,56)")
    cur.execute("Select * from Genome")
    fetch_data = cur.fetchall()
    cur.close()
    return render_template('index.html', data = fetch_data, **locals())

#main method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
