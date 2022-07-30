from sqlalchemy import func

from models.enums import RiderState

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.float, nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    status = db.Column(db.Enum(RiderState), default=RiderState.pending, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    customer = db.relationship('CustomerModel')