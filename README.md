## Flask RESTful API Starter - Railway Ready

Flask RESTful API starter template ready to deploy on Railway (`railway.app`), with a clean folder structure, SOLID design, and a standardized response shape.

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/flask-restful-api?referralCode=asepsp&utm_medium=integration&utm_source=template&utm_campaign=generic)

### Features

- **Clean folder structure** using an application factory (`app/`).
- **Standardized API response**:

```json
{
  "data": {},
  "status": 200,
  "message": "Success"
}
```

- **Built-in endpoints**:
  - `GET /` – root application info.
  - `GET /health` – simple health check.
  - `GET /status` – service status & uptime.
- **Docker-ready**: includes `Dockerfile`, `.dockerignore`.
- **Railway-ready**: reads `PORT` from environment variables.

### Folder Structure

```text
.
├── app
│   ├── __init__.py        # Application factory & wiring dependency
│   ├── config.py          # Configuration (dev/production)
│   ├── core
│   │   └── response.py    # ResponseFactory & ApiResponse (SOLID)
│   └── routes.py          # Routes / controllers
├── main.py                # Local entry point (development)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Image definition for Railway
├── .env                   # Local config (do not commit)
├── .env.example           # Example env file
├── .gitignore
├── .dockerignore
├── LICENSE
└── README.md
```

### Local Setup & Run

1. **Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# or
.venv\Scripts\activate     # Windows
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file**

```bash
cp .env.example .env
```

Adjust values if needed.

4. **Run the server (development)**

```bash
python main.py
```

The app will run at `http://localhost:8000` (based on `PORT` in `.env`).

### Built-in Endpoints

- **GET `/`**
  - **Description**: root endpoint that returns basic app info and environment.
  - **Example response**:

```json
{
  "data": {
    "app": "Flask Railway API",
    "environment": "development"
  },
  "status": 200,
  "message": "Root endpoint"
}
```

- **GET `/health`**

```json
{
  "data": {
    "healthy": true
  },
  "status": 200,
  "message": "Health check OK"
}
```

- **GET `/status`**

```json
{
  "data": {
    "uptime_seconds": 12,
    "environment": "development"
  },
  "status": 200,
  "message": "Service status"
}
```

### Deploy to Railway (Dockerfile)

1. Push this project to a Git repository (GitHub/GitLab).
2. In Railway:
   - Create New Project → Deploy from Repo.
   - Select this repository.
   - Railway will detect the `Dockerfile`.
3. Set minimum **Environment Variables**:
   - `ENVIRONMENT=production`
   - (optional) `APP_NAME`, `PORT` (Railway typically provides `PORT` automatically).

The Dockerfile runs `gunicorn`:

```bash
gunicorn -w 3 -b 0.0.0.0:8000 main:app
```

Railway provides the port via the `PORT` environment variable, while this image exposes `8000`. If you want to strictly bind to Railway's `PORT`, update the `CMD` in the `Dockerfile` to read `PORT` dynamically.

### Design Notes (SOLID)

- **Single Responsibility**:
  - `ResponseFactory` only handles response shape.
  - `routes.py` defines endpoints and uses injected dependencies.
  - `config.py` handles configuration.
- **Open/Closed**:
  - To add new response types (e.g., pagination), add a new method in `ResponseFactory` without changing existing ones.
- **Simple Dependency Injection**:
  - `ResponseFactory` is injected into the app (`app.response_factory`) and accessed via `current_app` inside endpoints.

You can add more blueprints/routes and keep the response shape consistent by using `ResponseFactory`.

