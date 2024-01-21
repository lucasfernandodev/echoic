from time import localtime, strftime

def getTime():
  time = strftime("%H horas e %M minutos", localtime())
  return time