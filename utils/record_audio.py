from utils.run import run

def recordAudio(output, duration, sample):
  rec=f"termux-microphone-record -d -f {output} -l {duration} -b {sample} -c 1"
  run(rec, duration)
