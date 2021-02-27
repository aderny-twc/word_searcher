# Vsearch web-application
A simple application based on an example from the book Head First. Updated frontend, added word search functionality.

## Project structure

```
\WORD_SEARCHER
│   .gitignore
│   .screenshots
│   README.md
│   searchtext.py
│   vsearch.py
│   requirements.txt
│
├───static
│       bg.jpg
│       style.css
│
├───templates
│       base.html
│       entry.html
│       results.html
│       viewlog.html
```

## URLs

| route     | description                                      |
| --------- | ------------------------------------------------ |
| /         | main page (Form to fill)                         |
| /searcher | result page (Search results by words or letters) |
| /viewlog  | log page (All results with user information)     |

### Main page

![](.screenshots\main_page.jpg)

### Result page

![](.screenshots\search_res.jpg)

## Installation

```
$ git clone https://github.com/aderny-twc/word_searcher.git
$ cd word_searcher
$ python -m venv venv
$ source /venv/bin/activate
(venv) pip install -r requirements.txt
```

## Database configuration

You need to create a database with these parameters by default (vsearch.py):

```python
app.config['dbconfig'] = {'host': '127.0.0.1',
                            'user': 'vsearch',
                            'password': 'vsearchpasswd',
                            'database': 'vsearchlogDB',}
```

## Application launch

```
(venv) python vsearch.py
```

Runs at localhost address