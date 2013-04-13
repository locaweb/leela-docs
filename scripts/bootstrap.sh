#!/bin/sh

bin_virtualenv=${bin_virtualenv:-virtualenv}
root=~/pyenv/leela-documentation

if [ ! -d "$root" ]
then
  if ! command -v "$bin_virtualenv" >/dev/null
  then
    echo "cant find virtualenv [using: $bin_virtualenv]"
    echo
    echo "You may use bin_virtualenv variable to fix this:"
    echo "  $ env bin_virtualenv=/path/to/virtualenv $0"
  fi
  ${bin_virtualenv:-virtualenv} "$root"
fi

for module in bottle sphinx sphinxcontrib-blockdiag
do
  echo pip -q install $module ...
  "$root/bin/pip" -q install $module
done
exec env SPHINXBUILD="$root/bin/sphinx-build" "$root/bin/python" ./scripts/server.py
