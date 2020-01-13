from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='./dist',
            template_folder='./dist')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
