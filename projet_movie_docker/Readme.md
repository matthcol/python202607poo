# Python application deployed with Docker

## Build container
The container is described within the Dockerfile .
```shell
docker build -t appmovie:0.1 .
```

Run the container
```shell
docker run --rm -it appmovie:0.1
```

## Manage project with `uv`

```shell
uv init  # start project
uv sync  # creer le venv
uv add pydantic # dependance appli
uv add --dev pytest pytest-cov # dependance dev
```

Generate requirements.txt from pyproject.toml without dev dependencies
```shell
uv export --no-dev --no-hashes -o requirements.txt  
```