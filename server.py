from flask import Flask, render_template, url_for, request, redirect
import csv
from werkzeug.utils import html #  render_template allows us to send multiple html files (from template folder only)
app=Flask(__name__)#name will return __main__ as we are running the main file
#html file on templates folder and js css files on static folder
@app.route('/') #decorator which tells the browser what to do when '/' directory called
def hello():
    return render_template('index.html') #{favicon}:anything inside {{}} is treated as a python command by flask, url_for is the standard/general way to run this command, static gives it the file path to the .ico 

@app.route('/<string:page_name>')
def blog(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('Reply.csv',mode='a',newline='') as database:
        name=data["name"]
        email=data["email"]
        message=data["message"]
        csv_writer=csv.writer(database, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('/Thankyou.html')
        except:
            return 'did not save to database'
    else:
        print('something went wrong try again!!!')