import subprocess

def speak_festival(text):
    command = f'echo "{text}" | festival --tts'
    subprocess.run(command, shell=True, executable='/bin/bash')
