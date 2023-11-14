import enum

import sqlalchemy

from config.db_connection import metadata


class Gender(enum.Enum):
    male = "Male"
    female = "Female"


class Status(enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"


application = sqlalchemy.Table(
    "application",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("student_id", sqlalchemy.ForeignKey("student.id")),
    sqlalchemy.Column("ration_card_number", sqlalchemy.String(255)),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("dob", sqlalchemy.String(255)),
    sqlalchemy.Column("gender", sqlalchemy.Enum(Gender)),
    sqlalchemy.Column("mobile_number", sqlalchemy.String(255)),
    sqlalchemy.Column("year", sqlalchemy.Integer),
    sqlalchemy.Column("income", sqlalchemy.String(255)),
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()
    ),
    sqlalchemy.Column(
        "status", sqlalchemy.Enum(Status), server_default=Status.pending.name
    ),
)
