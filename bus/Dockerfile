# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first for efficient Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Django will run on
EXPOSE 8000

# Default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

