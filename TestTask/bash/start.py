import os

dir = os.path.dirname(os.path.abspath(__file__))

for _, _, files in os.walk(dir):
    for f in files:
            os.system(f"chmod ugo+x {os.path.join(dir, f)}")
