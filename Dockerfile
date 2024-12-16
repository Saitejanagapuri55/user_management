FROM python:3.12-bookworm as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=true \
    PATH="/.venv/bin:$PATH"

WORKDIR /myapp

# Install system dependencies and security updates
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev libc-bin=2.36-9+deb12u7 --allow-downgrades \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN python -m venv /.venv \
    && . /.venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Runtime Stage
FROM python:3.12-slim-bookworm as final
COPY --from=base /.venv /.venv

WORKDIR /myapp
COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
