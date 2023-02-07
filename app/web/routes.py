from fastapi import FastAPI


def setup_routes(app: FastAPI):
    from app.employees.routes import setup_routes as employees_setup_routes

    employees_setup_routes(app)
