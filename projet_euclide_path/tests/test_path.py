from pathlib import Path

import pandas as pd
import pytest

# Exemple de fixture creant un fichier de data pour alimenter un test
# Le fixture tmp_path de pytest crée et nettoie un repertoire tmp
# pour chaque test l'utilisant : pas besoin de faire de teardown
@pytest.fixture
def data_movie_csv_file(tmp_path: Path):  
    data_file = tmp_path / "movies.csv"
    data = [
        ("Film 1", 2001, 90),
        ("Film 2", 2002, 91),
    ]
    df_data = pd.DataFrame(data, columns=['title', 'year', 'duration'])
    df_data.to_csv(data_file, index=False)
    return data_file

# test utilisant le jeu de données sous forme d'un fichier
def test_data(data_movie_csv_file):
    # utilisation du fichier
    df = pd.read_csv(data_movie_csv_file)
    # verification
    assert len(df) == 2