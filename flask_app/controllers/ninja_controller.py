from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/new_ninja")
def new_ninja():
    dojo_list = Dojo.get_all()
    return render_template("new_ninja.html", dojos=dojo_list)

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
    ninja_data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo"]
    }
    Ninja.insert(ninja_data)
    return redirect("/dojos")

@app.route("/edit_ninja/<int:id>")
def edit_ninja(id):
    ninja = Ninja.get_one_by_id({"id": id})
    return render_template("edit_ninja.html", ninja=ninja[0])

@app.route("/update_ninja/<int:id>", methods=["POST"])
def update_ninja(id):
    ninja_info = {
        "id": id,
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "age": request.form["age"]
    }
    Ninja.update(ninja_info)
    return redirect(f'/ninjas_in_dojo/{request.form["dojo_id"]}')

@app.route("/delete_ninja/<int:id>/<int:dojo_id>")
def delete(id, dojo_id):
    Ninja.delete({"id": id})
    return redirect(f'/ninjas_in_dojo/{dojo_id}')