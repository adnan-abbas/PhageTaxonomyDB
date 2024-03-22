from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import json
from flask import Response, make_response
import urllib.request


app = Flask(__name__)
with open('db.json') as config_file:
    config_data = json.load(config_file)

app.config['MYSQL_HOST'] = config_data['mysql_host']
app.config['MYSQL_USER'] = config_data['mysql_user']
app.config['MYSQL_PASSWORD'] = config_data['mysql_password']
app.config['MYSQL_DB'] = config_data['mysql_db']


mysql = MySQL(app)
 
@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.args.get('search_query', '')  # Get the search term from the query parameters
    cur = mysql.connection.cursor()

    # Base SQL query
    query = "SELECT * FROM genome"
    conditions = []
    parameters = []

    # Split the search query based on ','
    if search_query:
        for part in search_query.split(','):
            part = part.strip()
            # Check if the part follows the pattern for different searches
            if part.lower().startswith('species:'):
                species = part.split(':', 1)[1].strip()
                conditions.append("species LIKE %s")
                parameters.append('%' + species + '%')
            elif part.lower().startswith('length:>'):
                length = part.split(':', 1)[1].strip()
                if length.isdigit():  # Making sure the input is a number
                    conditions.append("genome_length > %s")
                    parameters.append(length)
            elif part.lower().startswith('accession:'):
                accession = part.split(':', 1)[1].strip()
                conditions.append("accession_id LIKE %s")
                parameters.append('%' + accession + '%')
            # Add more conditions based on the input pattern

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

    query += " LIMIT 10"  # Ensure only the first 10 are fetched
    cur.execute(query, parameters)
    genomes = cur.fetchall()
    cur.close()

    # Pass the genomes data to the template
    return render_template('index.html', genomes=genomes)



@app.route('/update_data', methods = ['POST', 'GET'])
def update_data():
    if request.method == 'POST':
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
        sql = "UPDATE features SET Classification = %s WHERE Accession = %s"
        val = (classification, accession_id)
        cur = mysql.connection.cursor()
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
    return render_template('index.html', **locals())


@app.route('/update', methods = ['POST','GET'])
def update():
    if request.method == 'POST':
        accession_id = request.form['accession_id']
        cur = mysql.connection.cursor()
        sql_features = "SELECT * FROM features WHERE Accession = %s"
        cur.execute(sql_features, [accession_id])
        data_features = cur.fetchall()
        classification = data_features[0][1]
        mol_gc = data_features[0][2]
        number_cds = data_features[0][3]
        positive_strand = data_features[0][4]
        negative_strand = data_features[0][5]
        trnas = data_features[0][6]


        sql_genome = "SELECT * FROM genome WHERE Accession = %s"
        cur.execute(sql_genome, [accession_id])
        data_genome = cur.fetchall()
        species = data_genome[0][1]
        genome_length = data_genome[0][2]
        modification_date = data_genome[0][3]
        sequence = data_genome[0][4]
        print(sequence)


        sql_taxonomy = "SELECT * FROM taxonomy WHERE Species = %s"
        cur.execute(sql_taxonomy, [species])
        data_taxon = cur.fetchall()
        orders = data_taxon[0][1]
        family = data_taxon[0][2]
        genus = data_taxon[0][3]

        # sql_host = "SELECT * FROM host WHERE Host = %s"
        # cur.execute(sql_host, [accession_id])
        # data_genome = cur.fetchall()
        # species = data_genome[0][1]
        # genome_length = data_genome[0][2]
        # modification_date = data_genome[0][3]
     
        cur.close()
    return render_template('updatedata.html',accession_id = accession_id, classification = classification, mol_gc = mol_gc, number_cds = number_cds, positive_strand = positive_strand, negative_strand= negative_strand,
    trnas = trnas, species =species, genome_length = genome_length, modification_date =modification_date, orders = orders, family = family, genus = genus, sequence = sequence  )  # Pass any necessary data

    
   # return render_template('updatedata.html')



@app.route('/view', methods = ['POST', 'GET'])
def view():
    if request.method == 'POST':
        operation = request.form['operation']
        accession_id = request.form['accession_id']
        #print(request.form)
        if (operation == 'delete'):
            cur = mysql.connection.cursor()
            sql_features = "DELETE FROM features WHERE Accession = %s"
            cur.execute(sql_features, [accession_id])
            sql_genome = "DELETE FROM genome WHERE Accession = %s"
            cur.execute(sql_genome, [accession_id])
            mysql.connection.commit()
            cur.close()
        return render_template('index.html')

    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM genome")
        data = cur.fetchall()
        cur.close()
        
        return render_template('viewdata.html',phages=data)



@app.route('/contribute', methods = ['POST', 'GET'])
def contribute_data():
    return render_template('contributedata.html')


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
        
        insert_in_taxonomy(species, orders, family, genus)
        insert_in_genome(accession_id,species, genome_length, modification_date, genome_sequence)
        insert_in_features(accession_id, classification, mol_gc, number_cds,positive_strand,negative_strand,trnas)
        insert_in_host(host)


    return render_template('insertdata.html')



def insert_in_genome(accession, species, genome_length, modification_date, sequence):
    print("inserting in genome table")
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO genome VALUES (%s, %s, %s, %s,%s)", (accession, species, genome_length,  modification_date, sequence))
    mysql.connection.commit()
    cur.close()
    #return redirect(url_for('index'))

def insert_in_features(accession, classification, mol_gc, number_cds, positive_strand, negative_strand, trnas):
    print("inserting in features")
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO features VALUES (%s, %s, %s, %s,%s, %s, %s)", (accession, classification, mol_gc,  number_cds, positive_strand, negative_strand, trnas))
    mysql.connection.commit()
    cur.close()

def insert_in_taxonomy(species, orders, family, genus):
    print("inserting in taxonomy table")
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO taxonomy VALUES (%s, %s, %s, %s)", (species, orders, family, genus))
    mysql.connection.commit()
    cur.close()

def insert_in_host(host):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM host")
    data = cur.fetchall()
    host_exists_already = False
    for (host_name, id) in data:
        if host_name == host:
            host_exists_already = True

    if (not host_exists_already):
        bact_id = len(data) + 1
        cur.execute("INSERT INTO host VALUES (%s, %s)", (host, bact_id))

    cur.close()
 

#main method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)


#(Accession, Species, Genome Length (bp), Modification Date, Sequence)