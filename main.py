import os

from flask import Flask

from app.presentation.filters import register_filters
from app.presentation.routes import register_routes
from app.repository.sqlite_repository import SQLiteTaskRepository
from app.service.task_service import TaskService

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "data.db")


def create_app():
    app = Flask(__name__)
    repository = SQLiteTaskRepository(DB_PATH)
    service = TaskService(repository)

    register_routes(app, service)
    register_filters(app)
    app.teardown_appcontext(repository.close_db)

    with app.app_context():
        service.init_db()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
