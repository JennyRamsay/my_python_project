from flask import Blueprint, Flask, redirect, render_template, request

from models.treatment import Treatment
import repositories.treatment_repository as treatment_repository

treatments_blueprint = Blueprint("treatments", __name__)


# INDEX
@treatments_blueprint.route("/treatments")
def treatments():
    treatments = treatment_repository.select_all()
    return render_template("/treatments/index.html", treatments=treatments)


# NEW
@treatments_blueprint.route("/treatments/new")
def new_treatment():
    return render_template("/treatments/new.html")


# CREATE
@treatments_blueprint.route("/treatments", methods=["POST"])
def create_treatment():
    name = request.form["name"]
    day_of_week = request.form["day_of_week"]
    time = request.form["time"]
    capacity = request.form['capacity']
    new_treatment = Treatment(name, day_of_week, time, capacity)
    treatment_repository.save(new_treatment)
    return redirect("/treatments")


# EDIT
@treatments_blueprint.route("/treatments/<id>/edit")
def edit_treatment(id):
    treatment = treatment_repository.select(id)
    return render_template("/treatments/edit.html", treatment=treatment)


# UPDATE
@treatments_blueprint.route("/treatments/<id>", methods=["POST"])
def update_treatment(id):
    name = request.form["name"]
    day_of_week = request.form["day_of_week"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    treatment = Treatment(name, day_of_week, time, capacity, id)
    treatment_repository.update(treatment)
    return redirect("/treatments")


# DELETE
@treatments_blueprint.route("/treatments/<id>/delete", methods=["POST"])
def delete_treatment(id):
    treatment_repository.delete(id)
    return redirect("/treatments")


