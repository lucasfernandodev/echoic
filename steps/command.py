from utils.talk import talk
from commands.get_time import getTime;
from commands.turn_on_screen import turnOnScreen

class Command():  
  def __init__(self):
    self.commands = ['time now', 'turn on screen']

  @staticmethod
  def _timeNow():
    time = getTime()
    talk(f'No momento são {time}.')

  @staticmethod
  def _turnOnScreen():
    turnOnScreen()

  def exec(self, cmd):
    if(cmd == self.commands[0]):
      self._timeNow();
    if(cmd == self.commands[1]):
      self._turnOnScreen()