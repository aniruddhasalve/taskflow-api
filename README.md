# TaskFlow API

A meaningful, Docker-ready task management backend built with FastAPI, SQLAlchemy, SQLite, and Pydantic. It supports persistent task storage, priorities, status filtering, and a complete create/list/update workflow.

## Start with Docker

```bash
docker compose up --build
```

Then open the interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## API endpoints

- `GET /health` — service health and version.
- `POST /api/v1/tasks` — create a task.
- `GET /api/v1/tasks?status=todo&limit=50` — list and filter tasks.
- `PATCH /api/v1/tasks/{task_id}` — update a task, including marking it done.

Example:

```bash
curl -X POST http://localhost:8000/api/v1/tasks \
  -H 'Content-Type: application/json' \
  -d '{"title":"Prepare release","description":"Ship v1","priority":1}'
```

Data persists in the named `taskflow-data` Docker volume.

## Run tests locally

```bash
python -m pip install -r requirements.txt
pytest -q
```

## Author

Aniruddha Salve — salveaniruddha180@gmail.com
