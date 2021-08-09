from db.run_sql import run_sql
from models.treatment import Treatment


def save(treatment):
    sql = "INSERT INTO treatments (name, day_of_week, time, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [treatment.name, treatment.day_of_week, treatment.time, treatment.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    treatment.id = id


def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM treatments WHERE id=%s"
    values = [id]
    run_sql(sql, values)


def select_all():
    treatments = []
    sql = "SELECT * FROM treatments ORDER BY id"
    results = run_sql(sql)

    for result in results:
        treatment = Treatment(result['name'], result['day_of_week'], result['time'], result['capacity'], result['id'])
        treatment.customers_booked = appointments(treatment)
        treatments.append(treatment)
    return treatments


def select(id):
    sql = "SELECT * FROM treatments WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    treatment = Treatment(result['name'], result['day_of_week'], result['time'], result['capacity'], result['id'])
    treatment.customers_booked = appointments(treatment)
    return treatment


def update(treatment):
    sql = "UPDATE treatments SET (name, day_of_week, time, capacity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [treatment.name, treatment.day_of_week, treatment.time, treatment.capacity, treatment.id]
    run_sql(sql, values)
    treatment.customers_booked = appointments(treatment)


# Counts how many times the same treatment_id appears in the appointment
def appointments(treatment):
    sql = "SELECT COUNT(*) FROM appointments WHERE treatment_id = %s"
    values = [treatment.id]
    result = run_sql(sql, values)[0]
    
    return result["count"]

