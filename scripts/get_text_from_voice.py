from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json

SetLogLevel(-1)

def getTextFromVoice(MODEL, FILE, ACCEPTED_COMMANDS):
    
    wf = wave.open(FILE, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit(1)

    model = Model(MODEL)

    # You can also specify the possible word or phrase list as JSON list,
    # the order doesn't have to be strict
    rec = KaldiRecognizer(model, wf.getframerate(), ACCEPTED_COMMANDS)
    rec.SetWords(True)
    
    while True:
        data = wf.readframes(200)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            rec.Result()
            rec.SetGrammar(ACCEPTED_COMMANDS)
        else:
            rec.PartialResult()

    return json.loads(rec.FinalResult())