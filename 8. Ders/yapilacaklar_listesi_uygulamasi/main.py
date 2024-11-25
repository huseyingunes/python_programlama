from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'adpufyhgwueiryiuty324t983u4tgrGFDHGSFHDGFH'
bcrypt = Bcrypt(app)

client = MongoClient('mongodb+srv://huseyingunes:3jkGBP9B6i7UeFvo@cluster0.adt0n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['user_db']
users = db['users']

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users.insert_one({
            'name': name,
            'email': email,
            'username': username,
            'password': hashed_password
        })
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username})
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Kullanıcı adı veya şifre yanlış'
    return render_template('login.html', error=error)
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('todo'))
    return redirect(url_for('login'))


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        task = request.form['task']
        users.update_one(
            {'username': session['username']},
            {'$push': {'tasks': {'_id': ObjectId(), 'task': task, 'completed': False}}}
        )

    user = users.find_one({'username': session['username']})
    tasks = user.get('tasks', [])
    return render_template('todo.html', tasks=tasks)

@app.route('/update_task_order', methods=['POST'])
def update_task_order():
    if 'username' not in session:
        return redirect(url_for('login'))

    order = request.json['order']
    for item in order:
        users.update_one(
            {'username': session['username'], 'tasks._id': ObjectId(item['id'])},
            {'$set': {'tasks.$.position': item['position']}}
        )
    return '', 204

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/edit_task/<task_id>', methods=['POST'])
def edit_task(task_id):
    new_task = request.form['new_task']
    users.update_one(
        {'username': session['username'], 'tasks._id': ObjectId(task_id)},
        {'$set': {'tasks.$.task': new_task}}
    )
    return redirect(url_for('todo'))

@app.route('/delete_task/<task_id>', methods=['POST'])
def delete_task(task_id):
    users.update_one(
        {'username': session['username']},
        {'$pull': {'tasks': {'_id': ObjectId(task_id)}}}
    )
    return redirect(url_for('todo'))

@app.route('/complete_task/<task_id>', methods=['POST'])
def complete_task(task_id):
    task = users.find_one(
        {'username': session['username'], 'tasks._id': ObjectId(task_id)},
        {'tasks.$': 1}
    )['tasks'][0]
    new_status = not task['completed']
    users.update_one(
        {'username': session['username'], 'tasks._id': ObjectId(task_id)},
        {'$set': {'tasks.$.completed': new_status}}
    )
    return redirect(url_for('todo'))

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = users.find_one({'username': session['username']})

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if password:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            users.update_one(
                {'username': session['username']},
                {'$set': {'name': name, 'email': email, 'password': hashed_password}}
            )
        else:
            users.update_one(
                {'username': session['username']},
                {'$set': {'name': name, 'email': email}}
            )
        return redirect(url_for('todo'))

    return render_template('edit_profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)