from enum import Enum


class RiderRole(Enum):
    customer = "Customer"
    staff = "Staff"
    administrator = "Administrator"


class RiderState(Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
