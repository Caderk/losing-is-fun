# Models Directory

Place your GGUF model files here.

## What are GGUF models?

GGUF (GPT-Generated Unified Format) is a file format for storing large language models in a quantized format, making them efficient to run on consumer hardware.

## Download Sources

### Recommended Sites:

- **Hugging Face**: https://huggingface.co/models?search=gguf
- **TheBloke's Collections**: https://huggingface.co/TheBloke (High-quality quantized models)

### Popular Models to Try:

1. **Llama-2-7B-Chat-GGUF** (Q4_K_M) - ~4GB
   - Great general-purpose chat model
   - Good balance of size and quality

2. **Mistral-7B-Instruct-GGUF** (Q4_K_M) - ~4GB
   - Excellent instruction following
   - Strong reasoning capabilities

3. **Dolphin-2.6-Mistral-7B-GGUF** (Q4_K_M) - ~4GB
   - Uncensored and versatile
   - Good for creative tasks

4. **TinyLlama-1.1B-Chat-GGUF** (Q4_K_M) - ~700MB
   - Smallest option, fast inference
   - Good for testing

## Quantization Guide

GGUF models come in different quantization levels. Here's what they mean:

- **Q2_K**: Smallest size, lowest quality (~2 bits per weight)
- **Q3_K_M**: Small size, moderate quality (~3 bits)
- **Q4_K_M**: **Recommended** - Good balance (~4 bits)
- **Q5_K_M**: Larger size, better quality (~5 bits)
- **Q6_K**: Even larger, near-original quality (~6 bits)
- **Q8_0**: Largest, highest quality (~8 bits)

**For most users, Q4_K_M is the sweet spot.**

## How to Download

### Option 1: Direct Download from Hugging Face

1. Visit the model page on Hugging Face
2. Click on "Files and versions"
3. Find the `.gguf` file (look for Q4_K_M quantization)
4. Click the download icon
5. Move the downloaded file to this `models/` directory

### Option 2: Using huggingface-cli

```bash
# Install the CLI tool
pip install huggingface-hub

# Download a model (example: Mistral-7B-Instruct)
huggingface-cli download \
  TheBloke/Mistral-7B-Instruct-v0.2-GGUF \
  mistral-7b-instruct-v0.2.Q4_K_M.gguf \
  --local-dir ./models \
  --local-dir-use-symlinks False
```

## Usage

Once you've placed a GGUF model in this directory:

1. **Start the llama-cpp-python server**:

   ```bash
   source .venv/bin/activate
   python scripts/run_llama_server.py
   ```

2. **Select your model** from the list

3. **Start the Next.js dev server** (in another terminal):

   ```bash
   npm run dev
   ```

4. **Open your browser** to http://localhost:3000

## File Size Requirements

Make sure you have enough disk space:

- 7B models (Q4_K_M): ~4-5 GB
- 13B models (Q4_K_M): ~7-8 GB
- 1B models (Q4_K_M): ~600-800 MB

## Troubleshooting

### Model fails to load

- Check if you have enough RAM (model size + 2GB recommended)
- Try a smaller quantization or smaller model

### Server crashes

- Reduce context size: Edit `run_llama_server.py` and lower `--n_ctx`
- Disable GPU layers: Set `--n_gpu_layers 0`

### Slow inference

- Enable GPU acceleration (if you have a compatible GPU)
- Use a smaller model or lower quantization
- Reduce context window size

## Additional Resources

- llama-cpp-python docs: https://github.com/abetlen/llama-cpp-python
- GGUF format specification: https://github.com/ggerganov/ggml/blob/master/docs/gguf.md
- Model performance comparisons: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
