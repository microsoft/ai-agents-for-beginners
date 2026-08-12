FROM mcr.microsoft.com/devcontainers/python:3.12

# Install pip for Python 3.12
RUN python -m pip install --upgrade pip

# Copy requirements.txt and install the packages
COPY requirements.txt .
RUN pip install -r requirements.txt