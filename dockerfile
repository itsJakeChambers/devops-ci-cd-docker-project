# Python official image
FROM python:3.11-slim

# Work directory
WORKDIR /app

# Copy the dependencies 
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code
COPY . .

# Expose the port
EXPOSE 8000

# Launch the app 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]