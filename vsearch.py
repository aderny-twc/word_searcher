from flask import Flask, render_template, request, copy_current_request_context
from threading import Thread

from searchtext import search4letters, search4words
from db.mysqlcm import *


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

@app.route('/viewlog')
def viewlog() -> 'html':
    try:
        with UseDataBase(app.config['dbconfig']) as cursor:
            _SQL = """SELECT phrase, letters, ip, browser_string, results
                        FROM log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Result')
        return render_template('viewlog.html',
                                the_title='View Log',
                                the_row_titles=titles,
                                the_data=contents,)
    except ConnectionError as err:
        print('Is your database switched on? Error: ', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is your query correct?. Error: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))
    return 'Error'

if __name__ == '__main__':
    app.run(debug=True)
