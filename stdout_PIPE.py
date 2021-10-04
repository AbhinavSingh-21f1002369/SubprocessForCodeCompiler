import subprocess

with open('logs.txt', 'w') as f:
    p5 = subprocess.run('ls', stdout = f, text = True)
    # default is p5 = subprocess.run('ls', stdout = subprocess.PIPE, text = True)