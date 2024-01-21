import subprocess
import time

def run(command, timeout=0):
  subprocess.run([command], shell=True);
  time.sleep(int(timeout));