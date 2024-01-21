from os import path
import json
from utils.vad import vad
from utils.record_audio import recordAudio
from utils.mp3_to_wave import mp3ToWav;

from scripts.get_text_from_voice import getTextFromVoice


def isAwake(awake_model):
  
  wake_command="hi tony"

  sample=16000
  aggressiveness=2
  rec_duration=2

  rec_awakening_output="audio/mic-awakening.mp3"
  wave_awakening_output='audio/wave-awakening.wav'
  vad_awakening_output="audio/vad-awakening.wav"

  # Grava o audio e espera o tempo gravado em RECORDING_DURATION até o audio terminar
  recordAudio(rec_awakening_output, rec_duration, sample)

  # Converte para .wav
  mp3ToWav(sample, rec_awakening_output, wave_awakening_output)

  # Creating .wav file if is voz is audio
  vad(2, wave_awakening_output, vad_awakening_output)

  if path.exists(f'{vad_awakening_output}'):
    data = getTextFromVoice(awake_model,wave_awakening_output, json.dumps([wake_command]))
    # Check if user command is for awaken
    if (data['text'] == wake_command):
      return True
    else:
      return False
  else:
    return False
  