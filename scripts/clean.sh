#!/bin/bash

# Script to clean all Python cache files and directories
# This ensures no stale bytecode interferes with refactored code

echo "Cleaning Python cache files..."

cd ..

# Remove all .pyc files (compiled Python bytecode)
echo "Removing .pyc files..."
find . -name "*.pyc" -exec rm -f {} \;

# Remove all .pyo files (optimized Python bytecode)
echo "Removing .pyo files..."
find . -name "*.pyo" -exec rm -f {} \;

# Remove all __pycache__ directories
echo "Removing __pycache__ directories..."
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# Remove .pytest_cache directories (if using pytest)
echo "Removing .pytest_cache directories..."
find . -name ".pytest_cache" -type d -exec rm -rf {} + 2>/dev/null || true

# Remove .coverage files (if using coverage.py)
echo "Removing coverage files..."
find . -name ".coverage" -exec rm -f {} \; 2>/dev/null || true
find . -name ".coverage.*" -exec rm -f {} \; 2>/dev/null || true

echo "Python cache cleanup complete!"
echo "You may want to restart your Python application to ensure all changes take effect."

# Remove log files if they exist
echo "Removing log files..."
find . -name "*.log" -exec rm -f {} \; 2>/dev/null || true
echo "Log files cleanup complete!"