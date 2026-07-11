# mini-backend

The smallest possible backend: a Flask server with two JSON endpoints.

## Endpoints

- `GET /health` → `{"status": "ok"}`
- `GET /time` → `{"utc_time": "<current UTC ISO timestamp>"}`

## Run it

```bash
pip install flask
python3 app.py
```

Server runs on `http://127.0.0.1:5000`.

## Test it

**curl:**
```bash
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/time
```

**Browser:** open `http://127.0.0.1:5000/health` or `http://127.0.0.1:5000/time` directly.
