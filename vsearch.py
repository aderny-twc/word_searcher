from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to vsearch',)


if __name__ == '__main__':
    app.run(debug=True)
