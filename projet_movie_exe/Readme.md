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
uv run pytest
# run app
uv run poe movieapp
# build app as an exe
uv run poe build-exe
```

## Deploy and run app
In any windows host with same specifications (without Python)
```shell
movieapp.exe
```

