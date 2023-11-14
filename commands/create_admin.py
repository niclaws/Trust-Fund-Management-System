import asyncclick as click

from config.db_connection import database
from managers.admin import AdminManager


# Script for creating admins on the server
# Commands
# 1) export PYTHONPATH=./
# 2) python commands/create_admin.py -e "admin@gmail.com" -n "Admin" -p "123456"
#


@click.command()
@click.option("-e", "--email", type=str, required=True)
@click.option("-n", "--name", type=str, required=True)
@click.option("-p", "--password", type=str, required=True)
async def create_admin(email, name, password):
    admin_data = {"email": email, "name": name, "password": password}
    await database.connect()
    await AdminManager.create_admin(admin_data)
    await database.disconnect()


if __name__ == "__main__":
    create_admin(_anyio_backend="asyncio")
