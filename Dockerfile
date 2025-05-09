FROM python:3.11-slim

WORKDIR /app

# Install dependencies via pip (lebih stabil)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 2500

# Jalankan dengan uvicorn, bukan uv
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2500"]
