from steps.manage_audio_folder import manageAudioFolder
from steps.is_awake import isAwake
from steps.receive_command import receiveCommand
from steps.command import Command

def main():

  cmd = Command()
  allowed_commands = cmd.commands

  manageAudioFolder("audio") # Cria/Remove a pasta com os audios

  isAwakeCommand = isAwake("models/model-minimal/")
  if(isAwakeCommand == True):
    command = receiveCommand("models/en-us", allowed_commands)
    print(command)
    if(command != False):
      cmd.exec(command)
  else:
    main()

  

if __name__ == "__main__":
    main()
