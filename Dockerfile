FROM python:3.11-alpine

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run the application
# CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "2500"]
# CMD ["fastapi","--app","main","run","--host=0.0.0.0","--port=2500","--debug"]

# Run the web service on container startup.
CMD ["hypercorn", "main:app", "--bind", "::"]
