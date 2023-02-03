from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def dojos():
    dojo_list = Dojo.get_all()
    return render_template("dojos.html", dojos=dojo_list)

@app.route("/create_dojo", methods=["POST"])
def add_dojo():
    Dojo.insert({"name": request.form["dojo"]})
    return redirect("/dojos")

@app.route("/ninjas_in_dojo/<int:dojo_id>")
def ninjas(dojo_id):
    # get the dojo from tne db, to pass the name into the page
    dojo = Dojo.get_one_by_id({"id": dojo_id})
    # get a list of ninjas for the dojo id
    dojo_ninjas = Dojo.get_dojo_with_ninjas({"id": dojo_id})
    ninja_list = dojo_ninjas.ninjas
    return render_template("dojo_ninjas.html", dojo=dojo[0]["name"], dojo_id=dojo[0]["id"], ninjas=ninja_list)