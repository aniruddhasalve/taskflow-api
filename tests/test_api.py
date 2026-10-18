from fastapi.testclient import TestClient

from app.main import app


def test_health() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_task_lifecycle() -> None:
    with TestClient(app) as client:
        created = client.post("/api/v1/tasks", json={"title": "Ship TaskFlow", "priority": 1})
        assert created.status_code == 201
        task_id = created.json()["id"]
        assert created.json()["status"] == "todo"

        updated = client.patch(f"/api/v1/tasks/{task_id}", json={"status": "done"})
        assert updated.status_code == 200
        assert updated.json()["completed"] is True

        listed = client.get("/api/v1/tasks?status=done")
        assert listed.status_code == 200
        assert any(task["id"] == task_id for task in listed.json())
