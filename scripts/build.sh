#!/bin/bash
set -e

# Remove old container if it exists
if [ $(docker ps -aq -f name=python_app) ]; then
  echo "Removing old container..."
  docker rm -f python_app || true
fi

echo "Building Docker image..."
docker compose build

echo "Running Docker container..."
docker compose up
