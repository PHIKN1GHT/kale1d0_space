import subprocess

subprocess.Popen(["hexo.cmd", "clean"]).wait()
subprocess.Popen(["hexo.cmd", "g"]).wait()

import os
import shutil

destination = 'phikn1ght.github.io'
source = 'public'
files = os.listdir(destination)
for file in files:
    if not file.startswith('.'):
        path = os.path.join(destination, file)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

copytree(source, destination)

subprocess.Popen(["git", "add", '.'], cwd=destination).wait()
subprocess.Popen(["git", "commit", '-m', 'Automatic build.'], cwd=destination).wait()
subprocess.Popen(["git", "push", 'origin'], cwd=destination).wait()
