from flask import Flask

# Create App
def create_app() :
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfasdf_secret_key'
    
    # import Blueprint
    from .views import views
    from .auth import auth
    
    # Apply Blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app