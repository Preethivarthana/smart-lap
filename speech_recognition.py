import os
import pyaudio
import json
from vosk import Model, KaldiRecognizer

model_path = "/home/preethi/vosk-model-en-in-0.5"

def recognize_speech():
    if not os.path.exists(model_path):
        print("Please download the Vosk model.")
        exit(1)

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Listening...")

    try:
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                result_json = json.loads(result)
                recognized_text = result_json.get('text', '').strip()
                if recognized_text:
                    print("You said:", recognized_text)
                    return recognized_text
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
