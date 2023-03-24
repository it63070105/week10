# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    JUPYTER_TOKEN=my_token \
    JUPYTER_PORT=8888

# Expose the Jupyter port
EXPOSE ${JUPYTER_PORT}

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=${JUPYTER_PORT}", "--no-browser", "--allow-root", "--NotebookApp.token=${JUPYTER_TOKEN}"]
