# Local LLM Chat Interface

An elegant, minimalist Next.js chat interface for running local LLM models using llama-cpp-python as the backend. Desktop-optimized UI with real-time streaming responses.

## Features

- 🚀 **Real-time streaming** - See AI responses as they're generated
- 💻 **Desktop-optimized** - Clean, spacious interface designed for desktop use
- 🎨 **Modern UI** - Built with Next.js 16 and Tailwind CSS 4
- 🔄 **Auto-resizing input** - Textarea expands as you type
- 📦 **Local models** - Run GGUF models completely offline
- 🌙 **Dark mode support** - Automatic dark mode detection

## Tech Stack

- **Frontend**: Next.js 16.0.1 (App Router), React 19.2.0, Tailwind CSS 4
- **Backend**: llama-cpp-python (OpenAI-compatible API)
- **Language**: TypeScript 5.x
- **Models**: GGUF format (quantized LLMs)

## Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Set Up Python Environment

```bash
# Run the setup script
./scripts/setup_llamacpp.sh

# This will:
# - Create a Python virtual environment in .venv/
# - Install llama-cpp-python with server support
```

### 3. Download a Model

Download a GGUF model and place it in the `models/` directory.

**Recommended starter models:**

- [TinyLlama-1.1B-Chat](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF) (~700MB) - Fast, great for testing
- [Mistral-7B-Instruct](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF) (~4GB) - Excellent quality
- [Dolphin-2.6-Mistral-7B](https://huggingface.co/cognitivecomputations/dolphin-2.6-mistral-7b-GGUF) (~4GB) - Uncensored

**Tip:** Look for Q4_K_M quantization - it's the sweet spot for quality vs. size.

See [models/README.md](models/README.md) for detailed download instructions.

### 4. Start the LLM Server

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the server script
python scripts/run_llama_server.py
```

The script will:

1. Show available models
2. Let you select one
3. Start the server on http://localhost:8080

### 5. Start the Next.js App

In a **new terminal**:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Usage

1. The interface will automatically detect if the llama-cpp-python server is running
2. A green indicator in the header means you're connected
3. Type your message in the input box
4. Press **Enter** to send (Shift+Enter for new line)
5. Watch the AI response stream in real-time!

## Project Structure

```
├── app/
│   ├── page.tsx                    # Main chat interface
│   ├── layout.tsx                  # Root layout
│   ├── globals.css                 # Global styles
│   └── api/
│       ├── chat-llamacpp/         # Streaming chat endpoint
│       └── models/                # List available models
├── components/
│   └── chat/
│       ├── ChatMessage.tsx        # Message bubble component
│       └── ChatInput.tsx          # Auto-resize input field
├── lib/
│   └── types/
│       └── chat.ts                # TypeScript interfaces
├── models/                        # Place GGUF files here
│   └── README.md                  # Model download guide
├── scripts/
│   ├── setup_llamacpp.sh         # Setup Python environment
│   └── run_llama_server.py       # Start llama-cpp server
└── spec_sheet.md                  # Technical specification
```

## GPU Acceleration (Optional)

### For NVIDIA GPUs:

Edit `scripts/setup_llamacpp.sh` and uncomment:

```bash
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python[server]
```

Then edit `scripts/run_llama_server.py` and change:

```python
"--n_gpu_layers", "-1",  # -1 = full GPU offload
```

### For Apple Silicon (Metal):

Edit `scripts/setup_llamacpp.sh` and uncomment:

```bash
CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python[server]
```

## Troubleshooting

### "Server offline" message

- Make sure the llama-cpp-python server is running: `python scripts/run_llama_server.py`
- Check that it's running on port 8080
- Look for errors in the terminal where the server is running

### Server crashes or runs out of memory

- Try a smaller model (e.g., TinyLlama 1.1B)
- Use a lower quantization (Q4_K_M → Q3_K_M)
- Reduce context size in `run_llama_server.py`: change `--n_ctx 4096` to `--n_ctx 2048`

### Slow responses

- Enable GPU acceleration (see above)
- Use a smaller model
- Close other applications to free up RAM

### Model not found

- Ensure GGUF files are in the `models/` directory
- Check file permissions
- Verify the file isn't corrupted (re-download if needed)

## Configuration

### Adjust Model Parameters

Edit `scripts/run_llama_server.py`:

```python
subprocess.run([
    "python", "-m", "llama_cpp.server",
    "--model", str(selected_model),
    "--host", "0.0.0.0",
    "--port", "8080",
    "--n_ctx", "4096",        # Context window size
    "--n_gpu_layers", "0",    # GPU layers (-1 for all)
])
```

### Adjust Chat Parameters

Edit `app/api/chat-llamacpp/route.ts`:

```typescript
body: JSON.stringify({
  model: model || 'local-model',
  messages,
  stream: true,
  temperature: 0.7,      // Randomness (0.0-1.0)
  max_tokens: 2048,      // Response length
}),
```

## Resources

- [llama-cpp-python Documentation](https://github.com/abetlen/llama-cpp-python)
- [GGUF Models on Hugging Face](https://huggingface.co/models?search=gguf)
- [Model Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
- [Next.js Documentation](https://nextjs.org/docs)

## License

This project is open source and available under the MIT License.
