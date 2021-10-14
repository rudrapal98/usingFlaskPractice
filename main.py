from flask import Flask, jsonify, request, url_for, redirect, render_template
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
    },
    {
        'id': 2,
        'title': u'Learn Python',
    }
]

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/even', methods=['POST'])
def even():
    n=request.form['num']
    if(n%2==0):
        print(f"{n} is an even number")
        result = {
            "Number" : n,
            "Even" : True 
        }
    else:
        print(f"{n} is an odd number")
        result = {
            "Number" : n,
            "Even" : False
        }
    return jsonify(result)

@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/tasks', methods=['POST'])
def create_task():
    task = {
        'id' : request.json['id'],
        'title' : request.json['title']
    }
    tasks.append(task)
    return jsonify({'task' : task}), 201

if __name__ == '__main__':
    app.run(debug=True)