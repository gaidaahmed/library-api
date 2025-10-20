# Library API (SLO demo)

OpenAPI-driven demo with CRUD on books.

## Run locally (Python)
```bash
cd server
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m swagger_server
# API: http://localhost:8080


## Client SDK (Python)
Generated from Swagger Editor at `client-python/`.

```bash
cd client-python
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
python - <<'PY'
from swagger_client import Configuration, ApiClient
from swagger_client.api.book_api import BookApi
cfg = Configuration(); cfg.host = "http://localhost:8081"
api = BookApi(ApiClient(cfg))
print(api.list_books())
PY

