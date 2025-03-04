# Load model directly
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq, pipeline

#processor = AutoProcessor.from_pretrained("steja/whisper-large-persian")
#model = AutoModelForSpeechSeq2Seq.from_pretrained("steja/whisper-large-persian")

pipe = pipeline("automatic-speech-recognition", model="steja/whisper-large-persian")
result = pipeline("./1.mp3")