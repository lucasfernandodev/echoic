import json
import time
from utils.talk import talk
from utils.record_audio import recordAudio;
from utils.mp3_to_wave import mp3ToWav;
from scripts.get_text_from_voice import getTextFromVoice

def receiveCommand(model, allowed_commands):

  rec_mic_output='audio/mic-command.mp3'
  wav_output="audio/wav-command.wav"

  talk('Olá, Qual o seu commando?')
  
  recordAudio(rec_mic_output, 3, 16000)
  print("processing")
  mp3ToWav(16000, rec_mic_output, wav_output, True)
  
  print("send for neural model")

  start_time = time.time()
  data = getTextFromVoice(model, wav_output, json.dumps(allowed_commands))
  
  #Time esapsed getTextFromVoice
  end_time = time.time()
  elapsed=end_time-start_time
  print("Elapsed Time: ", elapsed)
  try:
    command = allowed_commands.index(data['text'])
    return data['text']
  except ValueError:
    return False