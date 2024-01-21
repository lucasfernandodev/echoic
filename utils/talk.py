from utils.run import run

def talk(phrase):
  command = f'speak -v pt-BR "{phrase}" -s 130 -g 8';
  run(command);
