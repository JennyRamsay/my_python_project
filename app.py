from flask import Flask, render_template

from controllers.customers_controller import customers_blueprint
from controllers.treatments_controller import treatments_blueprint
from controllers.appointments_controller import appointments_blueprint

app = Flask(__name__)

app.register_blueprint(customers_blueprint)
app.register_blueprint(treatments_blueprint)
app.register_blueprint(appointments_blueprint)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()