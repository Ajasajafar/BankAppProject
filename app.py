from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
import atexit
import auto_push

# START FLASK APP
app = Flask(__name__)
#     set database connection settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'  #permanent db file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     initialize the database with the app
db = SQLAlchemy(app)

# DEFINE TABLE STRUCTURE (Model)
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	balance = db.Column(db.Numeric(12, 2), default=0.00, nullable = False)
#     each model = a table in the database
#     each class variable = a column

@app.route('/')
def home():
	return render_template('index.html')

# WHEN USER SAVES DATA
@app.route('/create', methods=['POST'])
def create_account():
#     create a new record (row)
	name = request.form['name']
	new_acc = User(name=name, balance=0.00)

#     add to database session
	db.session.add(new_acc)

#     commit to save permanently
	db.session.commit()
	return redirect('/')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
	if request.method == 'POST':
		name = request.form['name']
		deposit_amount = float(request.form['amount'])

		user = User.query.filter_by(name=name).first()
		if user:
			user.balance += deposit_amount
		else:
			user = User(name=name, balance=deposit_amount)
			db.session.add(user)

		db.session.commit()

When user opens /withdraw → show a form.
When submitted (POST):
    - Read name and amount.
    - Find user.
    - If not found → show “User not found”.
    - If balance < amount → show “Insufficient funds”.
    - Otherwise → subtract amount, commit, show success message.


# initialize or use auto_push as needed. Do NOT call it at import-time to avoid
# unexpected side effects when other modules import `app` (for tests, tooling,
# or WSGI servers). Call it when running the module directly.
atexit.register(auto_push.auto_push)

if __name__ == "__main__":
	# Create all tables before starting the server so the app has its schema
	# available when handling requests. This runs only when the module is
	# executed directly (not when imported by tests/tooling).
	with app.app_context():
		db.create_all()

	# Running the module directly (e.g. `python app.py`) will start the server.
	app.run(debug=True)


