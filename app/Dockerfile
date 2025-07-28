# Base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Environment config
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install build tools and dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Configure pip
RUN mkdir -p /root/.pip && echo "\
[global]\n\
timeout = 100\n\
index-url = https://pypi.org/simple\n\
" > /root/.pip/pip.conf

# Copy wheels and requirements
COPY wheels /wheels
COPY requirements.txt .

# Install torch manually from CPU wheel index
RUN pip install --no-cache-dir torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu

# Install the rest of the packages from wheel cache
RUN pip install --no-index --find-links=/wheels -r requirements.txt

# Copy pretrained model
COPY pretrained_models /app/pretrained_models

# Copy application code
COPY . /app

# Default command
CMD ["python", "main.py"]
