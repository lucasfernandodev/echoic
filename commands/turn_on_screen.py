from utils.run import run

def turnOnScreen():
  run('su -c "/system/bin/input keyevent 26"')
  return "A tela está ligada agora"