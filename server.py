import psycopg2
import os
from psycopg2 import pool
from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
      permission = request.form['consent']
      if permission == "Consent":
        return redirect("/survey", code=302)
      else:
        return redirect("/decline", code=302)
    else:
      return render_template('main.html') 
    

@app.route("/survey")
def survey():
    return render_template('survey.html') 

@app.route("/admin/summary")
def admin():
    return render_template('admin.html')

@app.route("/api/results", methods=['GET'])
def handleAPI():
    surveys = []
    query = request.args.get('reverse')
    
    if query == 'true':
        surveys = db.get_reverse_survey()
    else:
        surveys = db.get_survey()
    json = []
    for survey in surveys:
        json.append({"id": survey[0], "age": survey[1], "cats": survey[2], "features": survey[3], "conditionalQuestion": survey[4], "conditionalDetails": survey[5], "ts": survey[6]})

    return jsonify(json)

@app.route("/thanks", methods=['POST'])
def thanks():
    age = request.form['age']
    cats = request.form['cats']
    features = request.form.getlist('features')
    conditionalQuestion = request.form['conditional-question']
    conditionalDetails = request.form['conditional-question-details']
    db.add_survey(age, cats, features, conditionalQuestion, conditionalDetails)
    return render_template('thanks.html')

@app.route('/write_data', methods=['POST'])
def write_data():
    data = request.get_data()
    with open('/data/myfile.txt', 'w') as f:
        f.write(data)
    return 'Docker Volume is Awsome! Data written to file!'

@app.route("/decline")
def decline():
    return render_template('decline.html') 


  