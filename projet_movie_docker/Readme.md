docker build -t appmovie:0.1 .

docker run --rm -it appmovie:0.1



uv init  # start project
uv sync  # creer le venv
uv add pydantic # dependance appli
uv add --dev pytest pytest-cov # dependance dev
uv export --no-dev --no-hashes -o requirements.txt
