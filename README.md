# starter-app

A tiny hello-world web application, packaged with Docker and Docker Compose.

This repository is intentionally minimal. It is the **starting point for a
Kubernetes support training capstone**: a plain containerised app that a
support team can later convert into Kubernetes manifests, Helm charts,
Ingress, ConfigMaps, Secrets, and other workloads.

It deliberately stops at the **container / Compose stage** — there are no
Kubernetes manifests, Helm charts, or deployment YAML in this repo. Adding
those is the training exercise.

## What it is

A small [Flask](https://flask.palletsprojects.com/) app served by
[gunicorn](https://gunicorn.org/) inside a slim Python container. It has no
database, authentication, queues, or background jobs — just three routes and
a handful of environment variables.

## Routes

| Route      | Description                          | Example response                                                  |
| ---------- | ------------------------------------ | ---------------------------------------------------------------- |
| `/`        | Greeting and basic app info          | `{"message":"Hello, world!","app":"starter-app","version":"1.0.0"}` |
| `/health`  | Simple health check (returns `200`)  | `{"status":"ok"}`                                                |
| `/version` | App name and version                 | `{"app":"starter-app","version":"1.0.0"}`                        |

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/) (bundled with recent Docker)

## Run with Docker Compose

Start the app with a single command:

```bash
docker compose up --build
```

The app is now available on <http://localhost:8080>. Try the routes:

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/version
```

Stop it with `Ctrl+C`, then clean up:

```bash
docker compose down
```

## Build and run with Docker only

If you prefer plain Docker (no Compose):

```bash
docker build -t starter-app:latest .
docker run --rm -p 8080:8080 starter-app:latest
```

## Configuration

The app reads a few optional environment variables (see `.env.example`):

| Variable      | Default        | Used by              |
| ------------- | -------------- | -------------------- |
| `APP_NAME`    | `starter-app`  | `/`, `/version`      |
| `APP_VERSION` | `1.0.0`        | `/`, `/version`      |
| `GREETING`    | `Hello, world!`| `/`                  |
| `PORT`        | `8080`         | listening port       |

These are good candidates to externalise into ConfigMaps and Secrets when you
move the app to Kubernetes.

## Inspecting and troubleshooting

```bash
# Follow logs
docker compose logs -f

# Open a shell in the running container
docker compose exec web sh

# Check container status (incl. health)
docker compose ps
```

## Run locally without Docker (optional)

```bash
pip install -r requirements.txt
python app.py
# serves on http://localhost:8080
```

## Project layout

```
.
├── app.py              # The Flask application (3 routes)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container image definition
├── docker-compose.yml  # One-command local run
├── .env.example        # Sample configuration
├── .gitignore
├── LICENSE
└── README.md
```

## Next steps (the training capstone)

From here, a support team can:

- Write Kubernetes **Deployment** and **Service** manifests for the app.
- Add an **Ingress** to expose it.
- Move configuration into **ConfigMaps** and **Secrets**.
- Package everything as a **Helm chart**.
- Wire up health probes using the existing `/health` route.

None of that lives in this repo by design — it's the work to be done.
