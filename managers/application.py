import sqlalchemy

from config.db_connection import database
from models import application, Status


class ApplicationManager:
    @staticmethod
    async def create_application(data):
        await database.execute(application.insert().values(data))

    @staticmethod
    async def approve(id_):
        await database.execute(
            application.update()
            .values(status=Status.approved.name)
            .where(application.c.id == id_)
        )

    @staticmethod
    async def reject(id_):
        await database.execute(
            application.update()
            .values(status=Status.rejected.name)
            .where(application.c.id == id_)
        )

    @staticmethod
    async def get_pending_applications():
        return await database.fetch_all(
            sqlalchemy.select(
                [
                    application.c.id,
                    application.c.ration_card_number,
                    application.c.name,
                    application.c.dob,
                    application.c.gender,
                    application.c.mobile_number,
                    application.c.year,
                    application.c.income,
                    application.c.created_at,
                    application.c.status,
                ]
            ).where(application.c.status == Status.pending.name)
        )

    @staticmethod
    async def get_approved_applications():
        return await database.fetch_all(
            sqlalchemy.select(
                [
                    application.c.id,
                    application.c.ration_card_number,
                    application.c.name,
                    application.c.dob,
                    application.c.gender,
                    application.c.mobile_number,
                    application.c.year,
                    application.c.income,
                    application.c.created_at,
                    application.c.status,
                ]
            ).where(application.c.status == Status.approved.name)
        )

    @staticmethod
    async def get_rejected_applications():
        return await database.fetch_all(
            sqlalchemy.select(
                [
                    application.c.id,
                    application.c.ration_card_number,
                    application.c.name,
                    application.c.dob,
                    application.c.gender,
                    application.c.mobile_number,
                    application.c.year,
                    application.c.income,
                    application.c.created_at,
                    application.c.status,
                ]
            ).where(application.c.status == Status.rejected.name)
        )
