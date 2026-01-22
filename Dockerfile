# 1. Use official Python slim image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all code
COPY . .

# 5. Expose port for FastAPI
EXPOSE 8000

# 6. Start FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
