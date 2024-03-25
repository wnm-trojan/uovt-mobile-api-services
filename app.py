"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Bootloader of the application.
"""

import os
from api import Response, create_app
from core import bootstrap
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_jwt_extended import JWTManager

# Initialize the application
app = create_app()

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# JWT Authentication
jwt = JWTManager(app)

# Load configuration
bootstrap(app, db)

# Initialize the configurations
db.init_app(app)
ma.init_app(app)


# Main configurations
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=os.getenv('DEBUG'))
    pass
