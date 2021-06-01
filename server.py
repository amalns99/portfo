from re import template
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/resume.pdf")
def resume():
    return render_template('resume.pdf')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', newline='', mode='a')as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'Something went wrong, Try again .!!'
