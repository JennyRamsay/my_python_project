import pdb

from models.customer import Customer
import repositories.customer_repository as customer_repository

from models.treatment import Treatment
import repositories.treatment_repository as treatment_repository

from models.appointment import Appointment
import repositories.appointment_repository as appointment_repository

customer_repository.delete_all()
treatment_repository.delete_all()
appointment_repository.delete_all()

customer_1 = Customer("Jennifer Ramsay", "Gold")
customer_repository.save(customer_1)

customer_2 = Customer("Nadine Heltberg", "Platinum")
customer_repository.save(customer_2)

customer_3 = Customer("Nicola Crosson", "Bronze")
customer_repository.save(customer_3)

treatment_1 = Treatment("Botox", "Monday", "13:00", 1)
treatment_repository.save(treatment_1)

treatment_2 = Treatment("Massage", "Monday", "15:00", 2)
treatment_repository.save(treatment_2)

treatment_3 = Treatment("yoga", "Tuesday", "18:00", 12)
treatment_repository.save(treatment_3)

pdb.set_trace()