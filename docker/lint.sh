#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_hashes/ tests/

black democritus_hashes/ tests/

mypy democritus_hashes/ tests/

pylint --fail-under 9 democritus_hashes/*.py

flake8 democritus_hashes/ tests/

bandit -r democritus_hashes/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_hashes/ tests/
