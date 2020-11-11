import os
from flask import Flask, render_template, request, Markup

UPLOAD_FOLDER = os.path.join(os.curdir, 'uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():

    return render_template(
        'home.html',
        tutorials = ["tutorial1", "tutorial2"]
    )

@app.route('/tutorial')
def tutorial():
    id = request.args.get('id')
    print(id)
    #eventually query the database here to get the corresponding tutorial

    with open ('./static/html/smiley_tutorial.html') as fin:
        tutorial_txt = Markup(fin.read())

    with open('./static/js/smiley_face_starter.js') as fin:
        assisted_code = fin.read()

    with open('./static/js/smiley_face.js') as fin:
        solution_code = fin.read()

    return render_template(
        'index.html',
        tutorial_txt = tutorial_txt,
        assisted_code = assisted_code,
        solution_code = solution_code
    )

@app.route('/upload', methods=['GET', 'POST'])
def upload_controller():
    if request.method == 'POST':
        html = request.files['html']
        solution = request.files['solution']
        starter = request.files['starter']

        html.save(os.path.join(app.config['UPLOAD_FOLDER'], html.filename))
        solution.save(os.path.join(app.config['UPLOAD_FOLDER'], solution.filename))
        starter.save(os.path.join(app.config['UPLOAD_FOLDER'], starter.filename))
    return render_template(
        'upload.html'
    )

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True, threaded=True)
