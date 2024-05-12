FROM python:3.8-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgtk-3-dev \
    libopenblas-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    gfortran \
    opencc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    opencv-python-headless \
    numpy \
    Pillow

# Copy application code into the image
COPY . /app
WORKDIR /app

# Expose the port that the application will run on
EXPOSE 5000

# Run the application when the container starts
CMD ["python", "app.py"]
