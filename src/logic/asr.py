import whisper

model = whisper.load_model("base")

def asr(wav_path):
    result = model.transcribe(wav_path)
    print(result["text"])
 
if __name__ == "__main__":
    asr("/tmp/gradio/3b578731c88b62394bd4419c04cea3d1f5a26fd4/audio.wav")