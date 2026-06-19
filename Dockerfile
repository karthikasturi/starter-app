# Minimal, production-like image for the starter app.
FROM python:3.12-slim

# Keep Python output unbuffered so logs show up immediately in
# `docker logs` / `docker compose logs` — easier to troubleshoot.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

WORKDIR /app

# Install dependencies first so Docker can cache this layer.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code.
COPY app.py .

# Run as a non-root user, closer to a real production setup.
RUN useradd --create-home appuser
USER appuser

EXPOSE 8080

# Serve with gunicorn. Two workers is plenty for a hello-world app.
# Logs go to stdout/stderr so they are easy to inspect.
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", \
     "--access-logfile", "-", "--error-logfile", "-", "app:app"]
