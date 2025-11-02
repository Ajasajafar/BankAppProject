from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import atexit
import auto_push

# START FLASK APP
app = Flask(__name__)
#     set database connection settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'  #permanent db file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     initialize the database with the app

# DEFINE TABLE STRUCTURE (Model)
#     each model = a table in the database
#     each class variable = a column

# WHEN PROGRAM STARTS
#     create all tables (if not existing)

# WHEN USER SAVES DATA
#     create a new record (row)
#     add to database session
#     commit to save permanently

# WHEN USER WANTS TO SEE DATA
#     query the table for matching rows
#     display them
# END











# initialize or use auto_push as needed. Do NOT call it at import-time to avoid
# unexpected side effects when other modules import `app` (for tests, tooling,
# or WSGI servers). Call it when running the module directly.
atexit.register(auto_push.auto_push)

if __name__ == "__main__":
	# Running the module directly (e.g. `python app.py`) intentionally triggers
	# the auto-push behavior. For normal imports, this block will not execute.
	app.run(debug=True)


