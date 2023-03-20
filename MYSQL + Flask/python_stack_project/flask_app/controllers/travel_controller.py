from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.travel_plans import Travel_Plans
# from flask_app.models.tv_show import TV_Show

@app.route("/main")
def main_page():
    if "logged_id" not in session:
        return redirect("/")

    data = {
        "id": session["logged_id"]
    }
    logged_user = User.find_one_by_id(data)

    # pull data for all travel_plans
    # all_travel_plans = Travel_Plans.get_all_travel_plans()
    # for item in all_travel_plans:
    #     print(item.destination)
    return render_template("dashboard.html", logged_user=logged_user)

@app.route("/create_new")
def create():
    if "logged_id" not in session:
        return redirect("/")
    return render_template("new_trip.html")

@app.route("/planner")
# don't forget to add a method here please
# ps ur future self hates u lol
def add_items():
    if "logged_id" not in session:
        return redirect("/")
    return render_template("planner.html")
    # this will save the dates into the database and have it displayed on the next page 

@app.route("/submit_activity")
def submit_activity():
     if "logged_id" not in session:
        return redirect("/planner")
# here an activity will be saved into database and printed on the page in a table
# with the dates and list of activites for that trip

@app.route("/rome")
def rome():
    if "logged_id" not in session:
        return redirect("/planner")
    
    data = {
        "id": session["logged_id"]
    }
    logged_user = User.find_one_by_id(data)

    return render_template("rome.html", logged_user=logged_user)

@app.route("/alaska")
def alaska():
    if "logged_id" not in session:
        return redirect("/planner")

    data = {
        "id": session["logged_id"]
    }
    logged_user = User.find_one_by_id(data)
        
    return render_template("alaska.html", logged_user=logged_user)
