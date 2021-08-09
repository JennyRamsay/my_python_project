from db.run_sql import run_sql
from models.customer import Customer


def save(customer):
    sql = 'INSERT INTO customers (full_name, customership, status) VALUES (%s, %s, %s) RETURNING id'
    values = [customer.full_name, customer.customership, customer.status]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id


def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)


def select_all():
    customers = []
    sql = "SELECT * FROM customers ORDER BY id"
    results = run_sql(sql)

    for result in results:
        customer = Customer(result['full_name'], result['customership'], result['status'], result['id'])
        customers.append(customer)
    return customers


def select(id):
    sql = "SELECT * FROM customers WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    customer = Customer(result['full_name'], result['customership'], result['status'], result['id'])
    return customer


def update(customer):
    sql = "UPDATE customers SET (full_name, customership, status) = (%s, %s, %s) WHERE id = %s"
    values = [customer.full_name, customer.customership, customer.status, customer.id]
    run_sql(sql, values)