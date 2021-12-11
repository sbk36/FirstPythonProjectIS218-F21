"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
from App.calc.calculator import Calculator
import pandas as pd
import csv
app = Flask(__name__)

@app.route("/")
def index():
    """index  Route Response"""
    return render_template('index.html')

@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        #get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        #make the tuple
        my_tuple = (value1, value2)
        if value1 and value2 and value1.isdigit() and value2.isdigit():
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            data = { 'value1': value1, 'value2': value2, 'operation': operation,'result': result }
            df = pd.DataFrame([data])
            df.to_csv('App/results/data.csv', mode='a', index=False, header=False)
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        else:
            result ="Missing or invalid Value"
            data = { 'value1': value1, 'value2': value2, 'operation': operation,'result': result }
            df = pd.DataFrame([data])
            df.to_csv('App/results/data.csv', mode='a', index=False, header=False)
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)

    # Displays the form because if it isn't a post it is a get request
    else:
        return render_template('basicform.html')

@app.route("/table", methods=['GET', 'POST'])
def showtable():
    with open('App/results/data.csv', 'r') as csvfile:
        csv_dict = [row for row in csv.DictReader(csvfile)]
        if len(csv_dict) == 0:
            return render_template('empty_table.html')
        else:
            df = pd.read_csv('App/results/data.csv', header=None)
            data = df.values.tolist()
            return render_template('bootstrap_table.html', data = data)

@app.route("/bad/<value1>/<value2>")
def bad_calc(value1,value2):
    """bad calc Route Response"""
    result = value1 + value2
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response

@app.route("/good/<float:value1>/<float:value2>")
def good_calc(value1,value2):
    """good calc Route Response"""
    my_tuple = (value1,value2)
    Calculator.add_numbers(my_tuple)
    response = "The result of the calculation is: " + str(Calculator.get_last_result_value()) + '<a href="/"> back</a>'
    return response