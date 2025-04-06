from flask import Flask
from routes import auth_routes, job_routes
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # To allow frontend calls from different origin

app.register_blueprint(auth_routes)
app.register_blueprint(job_routes)

if _name_ == '_main_':
    app.run(debug=True)
