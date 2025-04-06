
# This is just a preview snippet of the main.py of my project reels. 
import asyncio
import os
import sys
import random

# --snip--

async def run():
    print("📖 Generating story...")
    story_text = storygen()

    print("🗣️ Converting story to voice...")
    audio_filename = get_next_filename(OUTPUT_DIR, "voice", "mp3")
    audio_path = os.path.join(OUTPUT_DIR, audio_filename)

    # Run voicegen in parallel
    voice_task = asyncio.create_task(voicegen(story_text, audio_path))

    print("🎥 Preparing video...")
    video_file = get_random_video()
    output_video = os.path.join(OUTPUT_DIR, get_next_filename(OUTPUT_DIR, "video", "mp4"))

    # Wait for voice generation to finish before proceeding
    await voice_task

    final_path = videogen(video_file, audio_path, output_video)

    # Delete audio file after processing
    os.remove(audio_path)

    print(f"✅ Final video saved at: {final_path}")


if __name__ == "__main__":
    asyncio.run(run())
