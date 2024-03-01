from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
with open('db.json') as config_file:
    config_data = json.load(config_file)

app.config['MYSQL_HOST'] = config_data['mysql_host']
app.config['MYSQL_USER'] = config_data['mysql_user']
app.config['MYSQL_PASSWORD'] = config_data['mysql_password']
app.config['MYSQL_DB'] = config_data['mysql_db']


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

    return render_template('index.html', **locals())


@app.route('/view', methods = ['POST', 'GET'])
def view():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM genome")
    data = cur.fetchall()
    cur.close()
    return render_template('viewdata.html',phages=data, **locals())



@app.route('/contribute', methods = ['POST', 'GET'])
def contribute_data():
    return render_template('contributedata.html', **locals())


@app.route('/insert', methods = ['POST', 'GET'])
def insert_data():
    if request.method == 'POST':
        #this data is coming from insertdata.html AJAX POST call
        accession_id = request.form['accession_id']
        genome_sequence = request.form['sequence']
        modification_date = request.form['modification_date']
        species = request.form['species']
        family = request.form['family']
        genus = request.form['genus']
        orders = request.form['orders']
        genome_length = request.form['genome_length']
        classification = request.form['classification']
        mol_gc = request.form['mol_gc']
        negative_strand = request.form['negative_strand']
        number_cds = request.form['number_cds']
        positive_strand = request.form['positive_strand']
        trnas = request.form['trnas']
        host = request.form['host']

        insert_in_genome(accession_id,species, genome_length, modification_date, genome_sequence)
        insert_in_features(accession_id, classification, mol_gc, number_cds,positive_strand,negative_strand,trnas)
        

    return render_template('insertdata.html', **locals())

def insert_in_genome(accession, species, genome_length, modification_date, sequence):
    print("inserting in genome table")
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO genome VALUES (%s, %s, %s, %s,%s)", (accession, species, genome_length,  modification_date, sequence))
    mysql.connection.commit()
    cur.close()
    #return redirect(url_for('index'))

def insert_in_features(accession, classification, mol_gc, number_cds, positive_strand, negative_strand, trnas):
    print("inserting in features")



#main method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)


#(Accession, Species, Genome Length (bp), Modification Date, Sequence)