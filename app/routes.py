from flask import(
    Flask,
    request
)
from app.database import task

app = Flask(__name__)


@app.get("/")
@app.get("/tasks")
def scan():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out

@app.put("/tasks/<int:pk>/")
def update(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "",204

@app.delete("/tasks/<int:pk>/")
def delete(pk):
    task_data = request.json
    task.delete_by_id(task_data, pk)
    return "",204

# @app.put("/tasks/<int:pk>/")
# def update(pk):
#     task_data = request.json
#     task.update_by_id(task_data, pk)
#     return "",204