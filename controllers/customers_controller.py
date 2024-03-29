from flask import Blueprint, Flask, redirect, render_template, request

from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint("customers", __name__)

# INDEX
@customers_blueprint.route("/customers")
def customers():
    customers = customer_repository.select_all()
    return render_template("/customers/index.html", customers=customers)


# NEW 
@customers_blueprint.route("/customers/new")
def new_customer():
    return render_template("/customers/new.html")


# CREATE
@customers_blueprint.route("/customers", methods=["POST"])
def create_customer():
    full_name = request.form["full_name"]
    customership = request.form["customership"]
    new_customer = Customer(full_name, customership)
    customer_repository.save(new_customer)
    return redirect("/customers")


# EDIT
@customers_blueprint.route("/customers/<id>/edit")
def edit_customer(id):
    customer = customer_repository.select(id)
    return render_template("/customers/edit.html", customer=customer)


# UPDATE
@customers_blueprint.route("/customers/<id>", methods=["POST"])
def update_customer(id):
    full_name = request.form["full_name"]
    customership = request.form["customership"]
    status = request.form["status"]
    customer = Customer(full_name, customership, status, id)
    customer_repository.update(customer)
    return redirect("/customers")