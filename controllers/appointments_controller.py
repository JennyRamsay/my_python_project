from flask import Blueprint, Flask, redirect, render_template, request
import repositories.appointment_repository as appointment_repository
import repositories.customer_repository as customer_repository
import repositories.treatment_repository as treatment_repository
from models.appointment import Appointment
from datetime import datetime 

appointments_blueprint = Blueprint("appointments", __name__)


# INDEX
@appointments_blueprint.route("/appointments")
def index():
    appointments = appointment_repository.select_all()
    treatments = treatment_repository.select_all()
    customers = customer_repository.select_all()
    return render_template("/appointments/index.html", appointments=appointments, treatments=treatments, customers=customers)


# NEW
@appointments_blueprint.route("/appointments/new")
def new():
    customers = customer_repository.select_all()
    treatments = treatment_repository.select_all()
    return render_template("/appointments/new.html", customers=customers, treatments=treatments)


# CREATE
@appointments_blueprint.route("/appointments", methods=["POST"])
def create_appointment():
    customer_id = request.form['customer_id']
    treatment_id = request.form['treatment_id']

    customer = customer_repository.select(customer_id)
    treatment = treatment_repository.select(treatment_id)

    appointment = Appointment(customer, treatment)

    # Converts the string treatment time to a time
    datetime_string = treatment.time
    datetime_of_treatment = datetime.strptime(datetime_string,'%H:%M').time()

    # Off-Peak Hours between 09:00 and 17:00, converts them to a time
    minimum_time = "09:00"
    datetime_minimum_time = datetime.strptime(minimum_time,'%H:%M').time()
    maximum_time = "17:00"
    datetime_maximum_time = datetime.strptime(maximum_time, '%H:%M').time()

    # Checks if capacity in class in greater than 1, if so adds customer to class
    # Won't allow customer to be added if the capacity is 0
    if treatment.capacity > treatment.customers_booked:
        if customer.customership == "Premium":
            appointment_repository.save(appointment)
            # Save standard customership customer to appointment if the time of the treatment is between the off-peak hours
        if customer.customership == "Standard" and datetime_of_treatment > datetime_minimum_time and datetime_of_treatment < datetime_maximum_time:
            appointment_repository.save(appointment)
    else:
        print("Day full")
    return redirect("/appointments/new")
   