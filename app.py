from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import auto_push

app = Flask(__name__)











# initialize or use auto_push as needed. Do NOT call it at import-time to avoid
# unexpected side effects when other modules import `app` (for tests, tooling,
# or WSGI servers). Call it when running the module directly.


if __name__ == "__main__":
	# Running the module directly (e.g. `python app.py`) intentionally triggers
	# the auto-push behavior. For normal imports, this block will not execute.
	auto_push.auto_push()


