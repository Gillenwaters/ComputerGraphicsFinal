from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_controller():
    with open('./static/js/WebGL_squary_eg.js') as fin:
        starter_code = fin.read()

    return render_template(
        'index.html',
        starter_code = starter_code
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)