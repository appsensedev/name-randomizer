from flask import Flask, render_template, request
import random
import csv 
from io import StringIO

app = Flask(__name__)
names = []

@app.route('/')
def index():
    return render_template('index.html', names=names)

@app.route('/add_name', methods=['POST'])
def add_name():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    location = request.form['location']
    racfid = request.form['racfid']
    branch = request.form['branch']

    names.append({'firstname': firstname, 'lastname': lastname, 'location': location, 'racfid': racfid, 'branch': branch})
    
    return render_template('index.html', names=names)

@app.route('/pick_random_name')
def pick_random_name():
    if names:
        random_name = random.choice(names)
    else:
        random_name = "No names added yet"
     # Return a page with a confetti animation
    return render_template('celebration.html', random_name=random_name, names=names)

    #return render_template('index.html', random_name=random_name, names=names)

#add the uploader treatment for the CSV 
@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    csv_file = request.files['csv_file']
    if not csv_file:
        return "No file uploaded"

    # Read the uploaded CSV file
    csv_data = csv_file.read().decode('utf-8')
    csv_reader = csv.DictReader(StringIO(csv_data))
    
    # Process the CSV data
    for row in csv_reader:
        firstname = row.get('firstname', '')
        lastname = row.get('lastname', '')
        location = row.get('location', '')
        racfid = row.get('racfid', '')
        branch = row.get('branch', '')
        
        # Perform any processing or validation as needed
        
        # Add the names to the list
        names.append({'firstname': firstname, 'lastname': lastname, 'location': location, 'racfid': racfid, 'branch': branch})
    
    return render_template('index.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)


#   _                 __                     
#  /_\  _ __  _ __   / _\ ___ _ __  ___  ___ 
# //_\\| '_ \| '_ \  \ \ / _ \ '_ \/ __|/ _ \
#/  _  \ |_) | |_) | _\ \  __/ | | \__ \  __/
#\_/ \_/ .__/| .__/  \__/\___|_| |_|___/\___|
#      |_|   |_|                             
#