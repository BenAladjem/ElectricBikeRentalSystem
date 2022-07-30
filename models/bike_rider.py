from models.enums import RidersRole

class  RidersModel:
    abstract = True
    # не се използва, само съдържа общите характеристики на класовете наследници
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class CustomerModel(RidersModel):
    tablename = "customers"

    role = db.Column(db.Enum(RidersRole), default=RidersRole.customer, nullable=False)



class StaffModel(RidersModel):
    tablename = "staffs"
    role = db.Column(db.Enum(RidersRole), default=RidersRole.staff, nullable=False)


class AdministratorModel(RidersModel):
    tablename = "administrators"
    role = db.Column(db.Enum(RidersRole), default=RidersRole.administrator, nullable=False)




