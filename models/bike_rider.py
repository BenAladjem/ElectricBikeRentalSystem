from db import db
from models.enums import RiderRole

class  RiderModel:
    abstract = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class CustomerModel(RidersModel):
    tablename = "customers"
    rentals = db.relationship("Rental", backref="rent", lazy='dynamic')
    role = db.Column(db.Enum(RiderRole), default=RiderRole.customer, nullable=False)



class StaffModel(RidersModel):
    tablename = "staffs"
    role = db.Column(db.Enum(RiderRole), default=RiderRole.staff, nullable=False)


class AdministratorModel(RidersModel):
    tablename = "administrators"
    role = db.Column(db.Enum(RiderRole), default=RiderRole.administrator, nullable=False)




