import os
from flask import Flask, render_template, request, Markup
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Tutorial  # noqa: E402


@app.route('/')
def home():
    tutorials = db.session.query(Tutorial).all()
    return render_template(
        'home.html',
        tutorials=tutorials
    )


@app.route('/tutorial/<id>')
def tutorial(id):
    with open('./static/html/smiley_tutorial.html') as fin:
        tutorial_txt = Markup(fin.read())

    with open('./static/js/smiley_face_starter.js') as fin:
        assisted_code = fin.read()

    with open('./static/js/smiley_face.js') as fin:
        solution_code = fin.read()

    return render_template(
        'index.html',
        tutorial_txt=tutorial_txt,
        assisted_code=assisted_code,
        solution_code=solution_code
    )


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    errors = []
    if request.method == 'POST':
        name = request.form.get('name')
        html = request.files['html']
        solution = request.files['solution']
        starter = request.files['starter']

        try:
            tutorial = Tutorial(
                name=name,
                tutorial_file=html.filename,
                starter_file=starter.filename,
                solution_file=solution.filename
            )

            db.session.add(tutorial)
            db.session.commit()

            html.save(os.path.join(app.config['UPLOAD_DIR'], html.filename))
            solution.save(os.path.join(
                app.config['UPLOAD_DIR'], solution.filename))
            starter.save(os.path.join(
                app.config['UPLOAD_DIR'], starter.filename))
        except:  # noqa E722
            errors.append('Upload failed.')
    return render_template(
        'upload.html',
        errors=errors
    )


if __name__ == '__main__':
    print(os.environ['APP_SETTINGS'])
    app.run()
