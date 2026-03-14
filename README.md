# request-playback

Personal website. Flask app served via Gunicorn behind nginx.

## Stack
- Python/Flask
- Gunicorn (WSGI server)
- nginx (reverse proxy, TLS) — config not included here
- systemd (process management)

## Run locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Production
Gunicorn binds to 127.0.0.1:5000, nginx proxies to it.
```bash
gunicorn -w 2 -b 127.0.0.1:5000 app:app
```

## Roadmap
- [ ] Dockerize
- [ ] k8s deployment
- [ ] Add headers/fingerprinting data as desired