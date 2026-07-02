# Python project build as a wheel

## Manage project with `uv`
```shell
uv init  # start project
uv sync  # create venv
uv add pydantic # app dependency
uv add --dev pytest pytest-cov poethepoet ruff # dev dependency
uv build
# quality code with Ruff
uv run poe lint 
uv run poe format
# run tests
uv run poe pytest
# run app
uv run poe movieapp
# build app as a wheel
uv build
```

## Deploy and run app
In a python env compatible (os, venv, docker)
```shell
pip install projet_movie_docker-0.1.0-py3-none-any.whl
# run app script
movieapp
```

