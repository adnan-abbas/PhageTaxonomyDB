from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import json
from flask import Response, make_response
import urllib.request
from flask import Flask, request, send_file
from Bio import Entrez
import os
import zipfile
import tempfile
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
with open('db.json') as config_file:
    config_data = json.load(config_file)

app.config['MYSQL_HOST'] = config_data['mysql_host']
app.config['MYSQL_USER'] = config_data['mysql_user']
app.config['MYSQL_PASSWORD'] = config_data['mysql_password']
app.config['MYSQL_DB'] = config_data['mysql_db']

app.secret_key = 'phagetaxonomy'
mysql = MySQL(app)

generic_query = "SELECT * FROM genome"
generic_parameters = []

bcrypt = Bcrypt(app)
 
@app.route('/', methods=['GET', 'POST'])
def landing():
    if session and (session['role'] == "admin" or session['role'] == "researcher"):
        return redirect(url_for('index'))

    return render_template('landing.html')


@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cur.fetchone()
        cur.close()

        if existing_user:
            flash('Email already exists. Please choose a different email.', 'error')
            return redirect(url_for('register'))


        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email format. Please enter a valid email address.', 'error')
            return redirect(url_for('register'))

        if len(password) < 8:
            flash('Password must be at least 8 characters long.', 'error')
            return redirect(url_for('register'))


        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect(url_for('register'))

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Save the user to the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (email, password_hash, role) VALUES (%s, %s, 'researcher')", (email, hashed_password))
        mysql.connection.commit()
        cur.close()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        cur = mysql.connection.cursor()
        # Your code here
    except AttributeError as e:
        app.logger.error("Error: Unable to connect to the database or get the cursor")
        return "Database connection is not established", 500
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Retrieve user from the database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and bcrypt.check_password_hash(user[2], password):
            # Store user information in session
            print(user[3])
            print(request.form['action'])
            if request.form['action'] == 'login_as_admin' and user[3]!='admin':
                flash('You are not an Admin, please click the Login button','error')
                return redirect(url_for('login'))

            session['user_id'] = user[0]
            session['email'] = user[1]
            session['role'] = user[3]
            flash('Login successful!', 'success')
            return redirect(url_for('index'))  # Redirect to the home page after login
        else:
            flash('Invalid email or password. Please try again.', 'error')


    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    session['role'] = 'guest'
    # Redirect to the login page
    return redirect(url_for('landing'))


@app.route('/add_admin', methods=['GET', 'POST'])
def add_admin():
    
    try:
        cur = mysql.connection.cursor()
        # Your code here
    except AttributeError as e:
        app.logger.error("Error: Unable to connect to the database or get the cursor")
        return "Database connection is not established", 500


    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cur.fetchone()
        cur.close()

        if existing_user:
            flash('Email already exists. Please choose a different email.', 'error')
            return redirect(url_for('add_admin'))


        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email format. Please enter a valid email address.', 'error')
            return redirect(url_for('add_admin'))

        if len(password) < 8:
            flash('Password must be at least 8 characters long.', 'error')
            return redirect(url_for('add_admin'))


        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect(url_for('add_admin'))

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Save the user to the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (email, password_hash, role) VALUES (%s, %s, 'admin')", (email, hashed_password))
        mysql.connection.commit()
        cur.close()

        flash('New admin registration successful!.', 'success')
        return redirect(url_for('add_admin'))
    return render_template('admin_settings.html')  # Render the form template if not a POST request

@app.route('/index', methods=['GET', 'POST'])
def index():
    #if the session has not been set, i.e. the user has not logged in
    if (not session):
        session['role'] = 'guest'
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

    #if session.get('advanced_command'):
    #    query = session['advanced_command']

    #if session.get('advanced_parameters'):
    #    parameters = session['advanced_parameters']

    
    cur.execute(query, parameters)
    genomes = cur.fetchall()
    cur.close()

    # Pass the genomes data to the template
    return render_template('index.html', genomes=genomes)

@app.route('/admin_settings', methods = ['POST', 'GET'])
def admin_settings():
    return render_template('admin_settings.html')

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
        #print(sequence)


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
 
# download_fasta

@app.route('/download_fasta', methods=['POST'])
def download_fasta():
    data = request.json
    accession_ids = data['selectedIds']
    # Entrez.email = "your_email@example.com"  # It's important to provide your email here

    # Create a temporary directory to store FASTA files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Folder name inside the ZIP
        folder_name = "FASTA_Files"

        # Paths for the temporary files and ZIP archive
        zip_path = os.path.join(temp_dir, "fasta_files.zip")

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for accession_id in accession_ids:
                file_name = f"{accession_id}.fasta"
                file_path = os.path.join(temp_dir, file_name)
                # Fetch the FASTA data and save it to the temporary file
                with Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text") as handle:
                    fasta_data = handle.read()
                with open(file_path, "w") as fasta_file:
                    fasta_file.write(fasta_data)
                
                # Add the file to the ZIP archive, including the folder path
                zipf.write(file_path, arcname=os.path.join(folder_name, file_name))

        # Send the ZIP file
        return send_file(zip_path, as_attachment=True, download_name="fasta_files.zip")

# show_summary
    
@app.route('/summary/<accessionID>')
def show_summary(accessionID):
    cur = mysql.connection.cursor()

    # Fetch genome data
    cur.execute("SELECT * FROM genome WHERE Accession = %s", [accessionID])
    genome_data = cur.fetchone()

    # Check if genome data exists
    if not genome_data:
        flash('No data found for the given Accession ID', 'danger')
        return redirect(url_for('index'))

    # Fetch features data
    cur.execute("SELECT * FROM features WHERE Accession = %s", [accessionID])
    features_data = cur.fetchall()

    # Fetch taxonomy data
    cur.execute("SELECT * FROM taxonomy WHERE Species = %s", [genome_data[1]])
    taxonomy_data = cur.fetchall()

    # Fetch host data
    cur.execute("SELECT * FROM species_attacks WHERE Species = %s", [genome_data[1]])
    host_data = cur.fetchone()

    cur.execute("SELECT * FROM host WHERE BactID = %s", [host_data[1]])
    bact_data = cur.fetchall()
    cur.close()

    # Preparing data for the template
    genome_details = {
        'accession_id': genome_data[0],
        'species': genome_data[1],
        'genome_length': genome_data[2],
        'modification_date': genome_data[3],
        'sequence': genome_data[4]
    }

    # Convert features_data to a list of dictionaries if needed, or pass directly if it's appropriately structured
    features = []
    for feature in features_data:
        features.append({
            'classification': feature[1],
            'mol_gc': feature[2],
            'number_cds': feature[3],
            'positive_strand': feature[4],
            'negative_strand': feature[5],
            'trnas': feature[6]
        })
    # print("Genome Details:", genome_details)
    # print("Features:", features)
    taxonomy = []
    for taxa in taxonomy_data:
        taxonomy.append({
            'species': taxa[0],
            'orders': taxa[1],
            'family': taxa[2],
            'genus': taxa[3]
        })

        bacts = []
    for bact in bact_data:
        bacts.append({
            'Host': bact[0]
        })
    return render_template('summary_page.html', details=genome_details, features=features, taxonomy=taxonomy, bacts=bacts)

@app.route('/data_statistics')
def data_statistics():
    cur = mysql.connection.cursor()

    # Genomic Length Insights
    cur.execute("""
        SELECT MIN(Genome_Length), MAX(Genome_Length), AVG(Genome_Length), COUNT(*), SUM(Genome_Length)
        FROM genome
    """)
    genome_length_insights = cur.fetchone()

    # GC Content Insights for Features (if applicable)
    cur.execute("""
        SELECT MIN(molGC_perc), MAX(molGC_perc), AVG(molGC_perc), COUNT(*), SUM(molGC_perc)
        FROM features
    """)
    gc_content_insights = cur.fetchone()

    # Detailed Features Statistics (e.g., for number_cds)
    cur.execute("""
        SELECT MIN(Number_CDS), MAX(Number_CDS), AVG(Number_CDS), COUNT(*), SUM(Number_CDS)
        FROM features
    """)
    cds_insights = cur.fetchone()

    # Taxonomy Insights - Count of Genomes per Genus
    cur.execute("""
        SELECT genus, COUNT(*) AS genome_count
        FROM taxonomy
        GROUP BY genus
    """)
    genomes_per_genus = cur.fetchall()

    # Total number of unique species
    cur.execute("SELECT COUNT(DISTINCT species) FROM taxonomy")
    total_species = cur.fetchone()[0]

    # Distribution of species across different families
    cur.execute("""
        SELECT family, COUNT(DISTINCT species) AS species_count
        FROM taxonomy
        GROUP BY family
    """)
    species_per_family = cur.fetchall()

    # Average genome length per species (if applicable)
    cur.execute("""
        SELECT taxonomy.species, AVG(genome_length) AS avg_length
        FROM genome
        JOIN taxonomy ON genome.species = taxonomy.species
        GROUP BY taxonomy.species
    """)
    avg_genome_length_per_species = cur.fetchall()

    cur.close()

    return render_template(
        'data_statistics.html',
        genome_length_insights=genome_length_insights,
        gc_content_insights=gc_content_insights,
        cds_insights=cds_insights,
        genomes_per_genus=genomes_per_genus,
        total_species=total_species,
        species_per_family=species_per_family,
        avg_genome_length_per_species=avg_genome_length_per_species
    )

@app.route('/advanced_search', methods=['GET', 'POST'])
def advanced_search():
    return render_template('advanced_search.html')

@app.route('/advanced_search_post', methods=['POST'])
def advanced_search_post():
    cur = mysql.connection.cursor()

    # Base SQL query
    query = "SELECT * FROM genome LEFT JOIN features ON genome.Accession=features.Accession LEFT JOIN taxonomy ON genome.Species=taxonomy.Species LEFT JOIN species_attacks ON genome.Species=species_attacks.Species LEFT JOIN host ON species_attacks.Host = host.BactID"
    conditions = []
    parameters = []

    #this data is coming from insertdata.html
    accession_id = request.form['accession_id']
    species = request.form['species']
    genome_length = request.form['genome_length']
    classification = request.form['classification']
    molgcmax = request.form['molgcmax']
    molgcmin = request.form['molgcmin']
    order = request.form['order']
    family = request.form['family']
    genus = request.form['genus']
    host = request.form['host']


    if accession_id != "":
        temp_conditions = []
        for part in accession_id.split(','):
            part = part.strip()
            temp_conditions.append("genome.Accession LIKE %s")
            parameters.append('%' + part + '%')
        
        conditions.append(" OR ".join(temp_conditions))
    '''
    if modification_date != "":
        temp_conditions = []
        for part in modification_date.split(','):
            part = part.strip()
            temp_conditions.append("Modification Date LIKE %s")
            parameters.append('%' + part + '%')
        conditions.append(" OR ".join(temp_conditions))
    '''
    if species != "":
        temp_conditions = []
        for part in species.split(','):
            part = part.strip()
            temp_conditions.append("genome.Species LIKE %s")
            parameters.append('%' + part + '%')
        conditions.append(" OR ".join(temp_conditions))

    if genome_length != "":
        temp_conditions = []
        for part in genome_length.split(','):
            part = part.strip()
            if part.isdigit():
                temp_conditions.append("genome.Genome_Length > %s")
                parameters.append( part )
        conditions.append(" OR ".join(temp_conditions))

    if classification != "":
        temp_conditions = []
        for part in classification.split(','):
            part = part.strip()
            temp_conditions.append("features.Classification LIKE %s")
            parameters.append('%' + part + '%')
        conditions.append(" OR ".join(temp_conditions))
    if molgcmax != "":
        temp_conditions = []
        for part in molgcmax.split(','):
            part = part.strip()
            if part.replace(".","").isdigit():
                temp_conditions.append("features.molGC_perc < %s")
                parameters.append( part )

        conditions.append(" OR ".join(temp_conditions))
    if molgcmin != "":
        temp_conditions = []
        for part in molgcmin.split(','):
            part = part.strip()
            if part.replace(".","").isdigit():
                temp_conditions.append("features.molGC_perc > %s")
                parameters.append(part)
        conditions.append(" OR ".join(temp_conditions))
    if order != "":
        temp_conditions = []
        for part in order.split(','):
            part = part.strip()
            temp_conditions.append("taxonomy.Orders LIKE %s")
            parameters.append('%' + part + '%')
        conditions.append(" OR ".join(temp_conditions))
    if family != "":
        temp_conditions = []
        for part in family.split(','):
            part = part.strip()
            temp_conditions.append("taxonomy.Family LIKE %s")
            parameters.append('%' + part + '%')
        conditions.append(" OR ".join(temp_conditions))
    if genus != "":
        temp_conditions = []
        for part in genus.split(','):
            part = part.strip()
            temp_conditions.append("taxonomy.Genus LIKE %s")
            parameters.append('%' + part + '%')
        conditions.append(" OR ".join(temp_conditions))
    if host != "":
        temp_conditions = []
        for part in host.split(','):
            part = part.strip()
            temp_conditions.append("host.Host LIKE %s")
            parameters.append('%' + part + '%')
        conditions.append(" OR ".join(temp_conditions))

    if conditions:
        query += " WHERE " + " AND ".join(conditions)
        app.logger.info(query)
        app.logger.info(parameters)

    #generic_query = query
    #generic_parameters = parameters

    session['advanced_command'] = query
    session['advanced_parameters'] = parameters

    cur.execute(query, parameters)
    genomes = cur.fetchall()
    cur.close()

    return render_template('advanced_search_table.html', genomes=genomes)

@app.route('/advanced_search_result', methods=['GET','POST'])
def advanced_search_result():
    search_query = request.args.get('search_query', '')  # Get the search term from the query parameters
    cur = mysql.connection.cursor()

    # Base SQL query
    query = generic_query
    conditions = []
    parameters = generic_parameters
    app.logger.info(generic_query)
    app.logger.info(generic_parameters)

    
    cur.execute(query, parameters)
    genomes = cur.fetchall()
    cur.close()

    # Pass the genomes data to the template
    return render_template('index.html', genomes=genomes)


    #cur.execute(query, parameters)
    #genomes = cur.fetchall()
    #cur.close()

    #return render_template('index.html', genomes=genomes)


    '''
    if family != "":
        temp_conditions = []
        for part in family.split(','):
            part = part.strip()
            temp_conditions.append("Species LIKE %s")
            parameters.append('%' + part + '%')
        conditions.append(" OR ".join(temp_conditions))
    '''

@app.route('/advanced_search_clear', methods=['POST'])
def advanced_search_clear():

    if session.get('advanced_command'):
        session.pop('advanced_command')

    if session.get('advanced_parameters'):
        session.pop('advanced_parameters')

    return render_template('advanced_search_table.html')

@app.route('/advanced_search_table', methods=['GET', 'POST'])
def advanced_search_table():
    #if the session has not been set, i.e. the user has not logged in
    if (not session):
        session['role'] = 'guest'
    search_query = request.args.get('search_query', '')  # Get the search term from the query parameters
    cur = mysql.connection.cursor()

    # Base SQL query


    query = "SELECT * FROM genome LEFT JOIN features ON genome.Accession=features.Accession LEFT JOIN taxonomy ON genome.Species=taxonomy.Species LEFT JOIN species_attacks ON genome.Species=species_attacks.Species LEFT JOIN host ON species_attacks.Host = host.BactID"
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

    if session.get('advanced_command'):
        query = session['advanced_command']

    if session.get('advanced_parameters'):
        parameters = session['advanced_parameters']

    
    cur.execute(query, parameters)
    genomes = cur.fetchall()
    cur.close()

    # Pass the genomes data to the template
    return render_template('advanced_search_table.html', genomes=genomes)




#main method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)


#(Accession, Species, Genome Length (bp), Modification Date, Sequence)