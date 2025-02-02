import whisper
import sys

# Load the Whisper model
model = whisper.load_model("base")  # You can use "tiny", "small", "medium", or "large"

def transcribe_audio(audio_path):
    print(f"Transcribing: {audio_path}")
    
    # Transcribe the audio file
    result = model.transcribe(audio_path)
    
    print("\nTranscription:\n")
    print(result["text"])
    
    # Save the transcription to a text file
    with open(audio_path + ".txt", "w", encoding="utf-8") as f:
        f.write(result["text"])

    print("\nSaved transcription to:", audio_path + ".txt")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file>")
    else:
        transcribe_audio(sys.argv[1])
