from db.run_sql import run_sql
from models.appointment import Appointment
from models.customer import Customer
from models.treatment import Treatment

import repositories.customer_repository as customer_repository
import repositories.treatment_repository as treatment_repository


def save(appointment):
    sql = "INSERT INTO appointments (customer_id, treatment_id) VALUES (%s, %s) RETURNING id"
    values = [appointment.customer.id, appointment.treatment.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    appointment.id = id


def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)


def select(id):
    sql = "SELECT * FROM appointments where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    customer = customer_repository.select(result['customer_id'])
    treatment = treatment_repository.select(result['treatment_id'])
    appointment = Appointment(customer, treatment, result['id'])
    return appointment


def select_all():
    appointments = []
    sql = "SELECT * FROM appointments ORDER BY id"
    results = run_sql(sql)

    for row in results:
        customer = customer_repository.select(row['customer_id'])
        treatment = treatment_repository.select(row['treatment_id'])
        appointment = Appointment(customer, treatment, row['id'])
        appointments.append(appointment)
    return appointments