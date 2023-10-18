<<<<<<< HEAD
#from package import Class
from flask import Flask 
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
=======
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import datetime


db=SQLAlchemy()

>>>>>>> 3bba827e9b5c1825a1ef66761011efb2e2845192

#create a function that creates a web application
# a web server will run this web application
def create_app():
<<<<<<< HEAD
  
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug=True
    app.secret_key='somesecretgoeshere'
    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydbname.sqlite'
    #initialise db with flask app
    db.init_app(app)

    bootstrap = Bootstrap5(app)
    
    #initialize the login manager
    #login_manager = LoginManager()
    
    #set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    #login_manager.login_view='auth.login'
    #login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    #from .models import User  # importing here to avoid circular references
    #@login_manager.user_loader
    #def load_user(user_id):
    #    return User.query.get(int(user_id))

    #importing views module here to avoid circular references
    # a common practice.
=======
    app = Flask(__name__)
    #we use this utility module to display forms quickly
    Bootstrap5(app)

    #this is a much safer way to store passwords
    Bcrypt(app)

    #a secret key for the session object
    #(it would be better to use an environment variable here)
    app.secret_key = 'somerandomvalue'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.sqlite'
    db.init_app(app)

    
    #initialise the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
      return User.query.get(int(user_id))
    #add Blueprints
>>>>>>> 3bba827e9b5c1825a1ef66761011efb2e2845192
    from . import views
    app.register_blueprint(views.bp)

    from . import auth
<<<<<<< HEAD
    app.register_blueprint(auth.bp)
    
    return app

=======
    app.register_blueprint(auth.authbp)

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)

    #this creates a dictionary of variables that are available
    #to all html templates
    @app.context_processor
    def get_context():
      year = datetime.datetime.today().year
      return dict(year=year)

    return app
>>>>>>> 3bba827e9b5c1825a1ef66761011efb2e2845192
