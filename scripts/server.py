# -*- coding: utf-8 -*-

import sys; _stdout = sys.stdout; _stderr = sys.stderr;
import time
import bottle
import os.path
import hashlib
import threading
import subprocess

bottle.debug(True)

srcroot     = os.path.join(os.path.dirname(__file__), "..")
sphinxbuild = os.environ.get("SPHINXBUILD", "sphinx-build")
devnull     = open(os.devnull, "w")

def monitor(test, run):
  while (True):
    updates = False
    for (root, _, files) in os.walk(srcroot):
      for f in files:
        updates = test(os.path.join(root, f)) or updates
    if (updates):
      run()
    time.sleep(1)

def test_md5():
  state = {}
  def f(filename):
    now = time.time()

    for k in list(state.keys()):
      if (now - state[k][1] > 300):
        del(state[k])

    if (not filename.endswith(".rst")):
      return(False)

    o_digest = state.get(filename, [None])[0]
    try:
      with file(filename, "r") as fh:
        n_digest = hashlib.md5(fh.read()).digest()
    except IOError:
      return(False)

    state[filename] = [n_digest, now]
    return(o_digest != n_digest)
  return(f)

def system(*args):
  rc = subprocess.Popen(args, stdout=devnull, stderr=devnull).wait()
  _stdout.write("> %s: %s\n" % (" ".join(args), {0: "success"}.get(rc, "failure")))

@bottle.route("/")
def main():
  return(bottle.redirect("/index.html"))

@bottle.route("/<path:path>")
def doc(path):
  rootdir = os.path.join(srcroot, "build", "html")
  return(bottle.static_file(path, root=rootdir))

t = threading.Thread(target=monitor, args=(test_md5(), lambda: system("make", "SPHINXBUILD=" + sphinxbuild, "clean", "html")))
t.setDaemon(True)
t.start()
bottle.run(host="0.0.0.0", port=4080)
