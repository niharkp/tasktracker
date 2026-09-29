FROM python:3.12-slim AS builder

WORKDIR /app
COPY req.txt .
RUN pip install --no-cache-dir --prefix=/install -r req.txt


FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY mapp.py .

RUN useradd -m appuser
USER appuser

EXPOSE 5000

HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000')"

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "mapp:app"]