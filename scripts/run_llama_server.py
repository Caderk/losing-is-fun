#!/usr/bin/env python3
"""
Start llama-cpp-python server with model selection
"""
import os
import sys
import subprocess
from pathlib import Path

def find_gguf_models(models_dir):
    """Find all GGUF model files in the models directory"""
    models = []
    if models_dir.exists():
        for file in models_dir.glob("*.gguf"):
            models.append(file)
    return sorted(models)

def main():
    # Get project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    models_dir = project_root / "models"
    
    # Find available models
    models = find_gguf_models(models_dir)
    
    if not models:
        print("❌ No GGUF models found in the 'models' directory.")
        print()
        print("Please download a GGUF model and place it in the 'models' directory.")
        print()
        print("Recommended sources:")
        print("  - Hugging Face: https://huggingface.co/models?search=gguf")
        print("  - TheBloke's models: https://huggingface.co/TheBloke")
        print()
        print("Popular choices:")
        print("  - Llama-2-7B-Chat GGUF (Q4_K_M)")
        print("  - Mistral-7B-Instruct GGUF (Q4_K_M)")
        print("  - Dolphin models (Q4_K_M)")
        sys.exit(1)
    
    print("Available GGUF models:")
    print()
    for i, model in enumerate(models, 1):
        size_mb = model.stat().st_size / (1024 * 1024)
        print(f"  {i}. {model.name} ({size_mb:.1f} MB)")
    print()
    
    # Model selection
    if len(models) == 1:
        selected_model = models[0]
        print(f"Using the only available model: {selected_model.name}")
    else:
        while True:
            try:
                choice = input(f"Select a model (1-{len(models)}): ").strip()
                index = int(choice) - 1
                if 0 <= index < len(models):
                    selected_model = models[index]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(models)}")
            except (ValueError, KeyboardInterrupt):
                print("\nCancelled.")
                sys.exit(0)
    
    print()
    print(f"🚀 Starting llama-cpp-python server with model: {selected_model.name}")
    print()
    print("Server will be available at: http://localhost:8080")
    print("Press Ctrl+C to stop the server")
    print()
    
    # Start the server
    try:
        subprocess.run([
            "python", "-m", "llama_cpp.server",
            "--model", str(selected_model),
            "--host", "0.0.0.0",
            "--port", "8080",
            "--n_ctx", "4096",
            "--n_gpu_layers", "0",  # Change to -1 for full GPU offload
        ], check=True)
    except KeyboardInterrupt:
        print("\n\n✋ Server stopped.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("\n❌ llama-cpp-python not found. Did you run the setup script?")
        print("Run: ./scripts/setup_llamacpp.sh")
        sys.exit(1)

if __name__ == "__main__":
    main()
