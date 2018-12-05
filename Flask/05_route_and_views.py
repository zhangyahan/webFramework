from flask import Flask


app = Flask(__name__)
app.config['SERVER_NAME'] = 'zhangyahan.com:5000'

"""
1.先执行 app.route('/index')
"""
# @app.route('/index', 
# 		   strict_slashes=None, 
# 		   redirect_to='/index')
# def index():
# 	return 'index'

@app.route('/', subdomain='admin')
def admin_index():
	return 'admin.your-domain.tld'


@app.route('/', subdomain='web')
def web_index():
	return 'web.your-domain.tld'


@app.route('/dynamic', subdomain='<username>')
def username_index(username):
	return username + '.your-domain.tld'



# def index():
# 	return 'index'
# app.add_url_rule('/index', None, index)

if __name__ == '__main__':
	app.run(debug=True)