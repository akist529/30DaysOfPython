# Importing Flask
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module
from pymongo.mongo_client import MongoClient
MONGODB_URI = 'mongodb+srv://akist0707:ZyIByhCxhIlrAX42@30daysofpython.ilqhwj6.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(MONGODB_URI)

try:
    db = client['thirty_days_of_python']
    db.students.insert_one({'name': 'Alex', 'country': 'USA', 'city': 'Chicago', 'age': 30})
    print(client.list_database_names())
except Exception as e:
    print(e)

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/') # this decorator creates the home route
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about') # this decorator creates the about route
def about ():
    name = '30 Days of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/post', methods=['GET', 'POST'])
def post ():
    name = 'Text Analyzer'

    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

