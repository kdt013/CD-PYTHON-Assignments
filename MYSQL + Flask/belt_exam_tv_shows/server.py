from flask_app import app
from flask_app.controllers import login_reg
from flask_app.controllers import tv_show_controller
# add more controllers

if __name__ == "__main__":
    app.run(debug = True)