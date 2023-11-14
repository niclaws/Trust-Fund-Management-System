import sqlalchemy
from sqlalchemy.sql import expression

from config.db_connection import metadata

student = sqlalchemy.Table(
    "student",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("email", sqlalchemy.String(255)),
    sqlalchemy.Column("password", sqlalchemy.Text),
    sqlalchemy.Column("verification_code", sqlalchemy.String(10)),
    sqlalchemy.Column(
        "is_verified", sqlalchemy.Boolean, server_default=expression.false()
    ),
)
