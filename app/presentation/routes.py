from flask import redirect, render_template, request, url_for


def register_routes(app, service):
    @app.route("/", methods=["GET"])
    def index():
        tasks = service.list_tasks()
        return render_template("index.html", tasks=tasks)

    @app.route("/tasks", methods=["POST"])
    def create_task():
        service.add_task(request.form.get("name", ""))
        return redirect(url_for("index"))

    @app.route("/tasks/<int:task_id>/start", methods=["POST"])
    def start_task(task_id):
        service.start_task(task_id)
        return redirect(url_for("index"))

    @app.route("/tasks/<int:task_id>/stop", methods=["POST"])
    def stop_task(task_id):
        service.stop_task(task_id)
        return redirect(url_for("index"))

    @app.route("/init", methods=["POST"])
    def init():
        service.init_db()
        return redirect(url_for("index"))
