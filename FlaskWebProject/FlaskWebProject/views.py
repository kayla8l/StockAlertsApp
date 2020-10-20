"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify
from FlaskWebProject import app

pet_database = [
    {
        "id": 1,
        "name": "Maki",
        "age": 1,
        "breed": "corgi",
    },
    {
        "id": 2,
        "name": "Poe",
        "age": 2,
        "breed": "pomeranian",
    },
]
 

@app.route('/pet_app/api/pets', methods=['GET'])
def get_pets():
    return jsonify({'pets': pet_database})


from flask import abort

@app.route('/pet_app/api/pets/<int:pet_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


