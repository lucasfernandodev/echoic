from utils.run import run;

def mp3ToWav(sample, input, output,filter=False):
	if(filter == True):
		command_for_converte = f'ffmpeg -i {input} -af "highpass=f=200, lowpass=f=3000,volume=5, afftdn" -loglevel quiet -ar {sample} -ac 1 -acodec pcm_s16le -f wav {output} -y'
		run(command_for_converte)
	else:
		command_for_converte = f'ffmpeg -i {input} -loglevel quiet -ar {sample} -acodec pcm_s16le -ac 1 -f wav {output} -y'
		run(command_for_converte)