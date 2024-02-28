from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
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



def get_genomes(user_id):
    conn = mysql.connection
    try:
        with conn.cursor() as cursor:
            query = 'SELECT * FROM post WHERE user_id = %s'
            cursor.execute(query, (user_id,))
            user_posts = cursor.fetchall()

            posts_list = []
            for post in user_posts:
                #print(post)
                post_data = {
                    'post_id': post[0],
                    'user_id': post[1],
                    'timestamp': post[2],
                    'content': Fernet(session[current_user.name]["key"]).decrypt(post[3]).decode('utf-8'),
                    'summary': Fernet(session[current_user.name]["key"]).decrypt(post[4]).decode('utf-8'),
                    'lstm': Fernet(session[current_user.name]["key"]).decrypt(post[5]).decode('utf-8'),
                    'free': post[6],
                    'character_count': post[7],
                    'ai_requests': post[8],
                    'sentiment': post[9],
                    'futurequestion': post[10],
                    # Include other post attributes as needed
                }
                posts_list.append(post_data)

            return posts_list
    finally:
        conn.close()



@app.route('/', methods = ['POST', 'GET'])
def index():
    cur = mysql.connection.cursor()
    #cur.execute("INSERT INTO Genome VALUES (123456,56)")
    cur.execute("Select * from Genome")
    fetch_data = cur.fetchall()
    cur.close()
    return render_template('index.html', data = fetch_data, **locals())


@app.route('/contribute', methods = ['POST', 'GET'])
def contribute_data():
    return render_template('contributedata.html', **locals())


@app.route('/insert', methods = ['POST', 'GET'])
def insert_data():
    return render_template('insertdata.html', **locals())
#main method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
