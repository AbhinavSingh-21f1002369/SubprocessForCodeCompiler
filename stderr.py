import subprocess
p6 = subprocess.run(['ls','hello'], capture_output=True, text = True)
print(p6)
print(p6.returncode)
print(p6.stdout)
print(p6.stderr)
print(p6.args)