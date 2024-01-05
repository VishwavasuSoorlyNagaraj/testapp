import os.path
from flask import Flask, render_template
from flask_autoindex import AutoIndex
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'matrix'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)
AutoIndex(app, browse_root=os.path.curdir + '/content/')

@app.route('/')
@basic_auth.required
def secret_view():
    return app.run()

