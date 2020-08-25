from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

posts = [
    {
        'author': 'Nagarajan Paramasivam',
        'title': 'Post 1',
        'content': 'First post',
        'date': 'Aug 24th 2020'
    },
    {
        'author': 'John Oliver',
        'title': 'Post 3',
        'content': 'Third post',
        'date': 'Aug 25th 2020'
    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=posts)

@app.route("/about")
def family():
    return render_template('about.html', title="About")

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(debug=True)