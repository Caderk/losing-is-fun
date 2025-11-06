# Technical Specification: Local LLM Chat Interface

## Project Overview

An elegant, minimalist Next.js chat interface for running local LLM models using llama-cpp-python as the backend. Desktop-optimized UI with real-time streaming responses.

---

## System Architecture

### Frontend Stack

- **Framework**: Next.js 16.0.1 (App Router)
- **React**: 19.2.0
- **Styling**: Tailwind CSS 4.x
- **TypeScript**: 5.x
- **Runtime**: Client-side only (`'use client'`)

### Backend

- **llama-cpp-python** (Python 3.x in virtual environment)
- Server mode with OpenAI-compatible API
- Supports GGUF model format

---

## Directory Structure

```
/home/carlos/projects/losing-is-fun/
├── app/
│   ├── page.tsx                    # Main chat UI (client component)
│   ├── layout.tsx                  # Root layout
│   ├── globals.css                 # Global styles
│   └── api/
│       ├── chat/
│       │   └── route.ts            # llama-cpp-python streaming endpoint
│       └── models/
│           └── route.ts            # List available models
├── components/
│   └── chat/
│       ├── ChatMessage.tsx         # Message bubble component
│       └── ChatInput.tsx           # Input field with auto-resize
├── lib/
│   └── types/
│       └── chat.ts                 # TypeScript interfaces
├── models/                         # Drop GGUF files here
│   └── README.md
├── scripts/
│   ├── setup_llamacpp.sh          # Setup Python venv + llama-cpp-python
│   └── run_llama_server.py        # Start llama-cpp server
├── package.json
├── next.config.ts
├── tsconfig.json
└── tailwind.config.js
```

---

## Implementation Details

### 1. TypeScript Types (`lib/types/chat.ts`)

```typescript
export interface Message {
  role: "user" | "assistant" | "system";
  content: string;
}
```

### 2. Chat Message Component (`components/chat/ChatMessage.tsx`)

**Purpose**: Display individual chat messages with role-based styling

**Features**:

- User messages: Right-aligned, blue gradient background
- Assistant messages: Left-aligned, gray background
- Desktop-optimized spacing (mb-8, max-w-4xl)
- Avatar badges (U for user, A for assistant)
- Markdown support (optional enhancement)

### 3. Chat Input Component (`components/chat/ChatInput.tsx`)

**Purpose**: Auto-resizing textarea with send button

**Features**:

- Textarea auto-expands as user types
- Enter to send, Shift+Enter for newline
- Disabled state during loading
- Desktop-optimized height (min-h-14)
- Keyboard hint text

### 4. Main Page Component (`app/page.tsx`)

**Purpose**: Main chat interface with message management

**Critical Features**:

1. **Model Loading (useEffect)**:
2. **Streaming Message Handler**:
3. **Auto-scroll**:

**Layout Structure**:

- Header: Title + model selector + status indicator
- Messages area: Scrollable with welcome screen when empty
- Input area: Fixed at bottom

### 5. API Route: Chat with llama-cpp-python (`app/api/chat/route.ts`)

**Purpose**: Streaming chat endpoint for llama-cpp-python server

### 6. API Route: Models List (`app/api/models/route.ts`)

**Purpose**: List available GGUF models from `/models` directory

### 7. Python Setup Script (`scripts/setup_llamacpp.sh`)

**Purpose**: Create Python venv and install llama-cpp-python

```bash
#!/bin/bash

# Create virtual environment
python3 -m venv .venv

# Activate venv
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install llama-cpp-python with GPU support (optional)
# For CPU only:
pip install llama-cpp-python[server]

# For GPU (CUDA):
# CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python[server]

echo "Setup complete! Activate with: source .venv/bin/activate"
```

### 8. Python Server Script (`scripts/run_llama_server.py`)

**Purpose**: Start llama-cpp-python server with model selection

### 9. Models Directory (`models/README.md`)

```markdown
# Models Directory

Place your GGUF model files here.

## Download Sources:

- Hugging Face: https://huggingface.co/models
- Search for GGUF quantized models

## Usage:

1. Download GGUF file
2. Place in this directory
3. Run: `python scripts/run_llama_server.py`
4. Select model from list
5. Start Next.js dev server: `npm run dev`
```

---

## Workflow

### Initial Setup

1. **Install dependencies**:

   ```bash
   npm install
   ```

2. **Set up Python environment**:

   ```bash
   chmod +x scripts/setup_llamacpp.sh
   ./scripts/setup_llamacpp.sh
   ```

3. **Download a GGUF model**:
   - Visit Hugging Face
   - Search for "dolphin GGUF" or "llama GGUF"
   - Download Q4_K_M quantization (balanced size/quality)
   - Place in `/models` directory

### Running the Application

**Terminal 1 - Start llama-cpp-python server**:

```bash
source venv/bin/activate
python scripts/run_llama_server.py
# Select model when prompted
# Server starts on http://localhost:8080
```

**Terminal 2 - Start Next.js dev server**:

```bash
npm run dev
# Visit http://localhost:3000
```

### Testing

1. Open browser to `http://localhost:3000`
2. Should see welcome screen with model selector
3. Type a message and press Enter
4. Should see streaming response appear in real-time

---
