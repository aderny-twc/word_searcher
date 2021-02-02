from flask import Flask, render_template, request, copy_current_request_context
from threading import Thread

from searchtext import search4letters, search4words
from DBcm import *


app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                            'user': 'vsearch',
                            'password': 'vsearchpasswd',
                            'database': 'vsearchlogDB',}


@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to vsearch',)


@app.route('/searcher', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """
        Log details of the web request and the results.
        """

        with UseDataBase(app.config['dbconfig']) as cursor:
            _SQL = """INSERT INTO log
                    (phrase, letters, ip, browser_string, results)
                    VALUES
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                    req.form['letters'],
                                    req.remote_addr,
                                    req.user_agent.browser,
                                    res,))

    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('*** Logging failed with this error: ', str(err))

    title = 'Your results'
    return render_template('results.html',
                            the_results=results,
                            the_title=title,
                            the_letters=letters,
                            the_phrase=phrase,)


if __name__ == '__main__':
    app.run(debug=True)
