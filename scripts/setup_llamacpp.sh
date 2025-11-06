#!/bin/bash

echo "Setting up llama-cpp-python environment..."

# Create virtual environment
python3 -m venv .venv

# Activate venv
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install llama-cpp-python with server support
# For CPU only:
pip install llama-cpp-python[server]

# For GPU (CUDA) support, uncomment the following line instead:
# CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python[server]

# For Metal (macOS Apple Silicon) support, uncomment the following line instead:
# CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python[server]

echo ""
echo "Setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To start the llama-cpp-python server, run:"
echo "  python scripts/run_llama_server.py"
