# Use official Python image
FROM python:3.13.2-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Start the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

