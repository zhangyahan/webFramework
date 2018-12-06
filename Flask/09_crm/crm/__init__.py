from flask import Flask


def create_app():

	app = Flask(__name__)

	from .views.account import ac
	app.register_blueprint(ac, url_prefix='/api')

	return app