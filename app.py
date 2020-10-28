from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_controller():
    with open('./static/js/WebGL_blue.js') as fin:
        assisted_code = fin.read()

    with open('./static/js/WebGL_square_eg.js') as fin:
        solution_code = fin.read()

    return render_template(
        'index.html',
        assisted_code = assisted_code,
        solution_code = solution_code
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)