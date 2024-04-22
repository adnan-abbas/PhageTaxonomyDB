# PhageTaxonomyDB - A Database of Phage Viruses

## Setting up MySQL Workbench
1. Download MySQL Workbench.
2. Follow through the steps and setup Workbench locally.
3. Go to "Administration > Data Import/Restore"
4. Go to the Import from Self-Contained File and then select the "phage_db.sql" file from the repository.
5. Select a Default Target Schema and click on Start Import
6. You should be able to view the tables in the left window such as features, genome, etc.

## Setting up the web application
1. Clone the repository
2. Create a python virtual environment by running: `python3 -m venv [YOUR_VIRTUAL_ENV_NAME]` (this step is optional if you want to seperate your global and local python modules)
3. Activate the virtual environment by `\[YOUR_VIRTUAL_ENV_NAME]\ source bin activate`
4. Run `pip install -r requirements.txt`
5. Create a db.json file. You can copy paste the below and add your MySQL credentials:
  {
    "mysql_host": "",
    "mysql_user": "",
    "mysql_password": "",
    "mysql_db": ""
   }
6. Run `python3 app.py` or `flask run`
