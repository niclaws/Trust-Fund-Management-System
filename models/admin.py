import sqlalchemy

from config.db_connection import metadata

admin = sqlalchemy.Table(
    "admin",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("email", sqlalchemy.String(255)),
    sqlalchemy.Column("password", sqlalchemy.Text),
)
