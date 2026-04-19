FROM python:3.14-slim
WORKDIR /app
COPY requirements.txt .
RUN pip instll --no-cache-dir - requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn","--bind", "0.0.0.0:8000","--timeout", "600", "site_1:app"]