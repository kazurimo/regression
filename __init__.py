from flask import Flask

app = Flask(__name__)                                                          
app.run(debug=True)

from flaskr import db
db.create_books_table()

import flaskr.main

