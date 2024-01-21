from os import path, makedirs
import shutil

def manageAudioFolder(folder_name):
  # Cria a pasta de destino
  if not path.exists(folder_name):
    makedirs(folder_name)
  else:
    shutil.rmtree("audio")
    makedirs(folder_name)