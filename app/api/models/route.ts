import { NextResponse } from "next/server";
import { readdir } from "fs/promises";
import { join } from "path";

export async function GET() {
  try {
    const modelsDir = join(process.cwd(), "models");

    // Read files from models directory
    const files = await readdir(modelsDir);

    // Filter for GGUF files
    const ggufFiles = files.filter((file) =>
      file.toLowerCase().endsWith(".gguf"),
    );

    return NextResponse.json({
      models: ggufFiles,
      count: ggufFiles.length,
    });
  } catch (error) {
    console.error("Error reading models directory:", error);
    return NextResponse.json(
      { error: "Failed to read models directory", models: [], count: 0 },
      { status: 500 },
    );
  }
}
