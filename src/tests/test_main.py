import json
from tempfile import NamedTemporaryFile

from typer.testing import CliRunner

from config import SCIENTISTS, SRC_PATH
from main import app

runner = CliRunner()


def test_find_wikipedia_person_by_name():
    result = runner.invoke(app, ["find-wikipedia-person-by-name", SCIENTISTS[0]])
    assert result.exit_code == 0
    assert SCIENTISTS[0] in result.stdout


def test_find_wikipedia_people_by_name():
    result = runner.invoke(app, ["find-wikipedia-people-by-name"])
    assert result.exit_code == 0
    for scientist in SCIENTISTS:
        assert scientist in result.stdout


def test_find_wikipedia_people_from_file():
    result = runner.invoke(app, ["find-wikipedia-people-from-file"])
    assert result.exit_code == 0
    for scientist in SCIENTISTS:
        assert scientist in result.stdout

def test_find_wikipedia_people_from_non_existent_file():
    result = runner.invoke(app, ["find-wikipedia-people-from-file", "--file-path", "qwerty.json"])
    assert result.exit_code == 1

def test_find_wikipedia_people_from_non_json_file():
    result = runner.invoke(
        app, 
        ["find-wikipedia-people-from-file", "--file-path", SRC_PATH / "config.py"]
    )
    assert result.exit_code == 1

def test_find_wikipedia_people_from_wrong_json_file():
    ### NOT ARRAY CASE
    data = {}
    tfile = NamedTemporaryFile(mode="w",)
    json.dump(data, tfile)
    tfile.flush()
    result = runner.invoke(app, ["find-wikipedia-people-from-file", "--file-path", tfile.name])
    assert result.exit_code == 1

    ### EMPTY ARRAY CASE
    data = []
    tfile = NamedTemporaryFile(mode="w",)
    json.dump(data, tfile)
    tfile.flush()
    result = runner.invoke(app, ["find-wikipedia-people-from-file", "--file-path", tfile.name])
    assert result.exit_code == 1

    ### ARRAY WITH DIFFERENT TYPES CASE
    data = ["Marilyn Monroe", 31, False, None]
    tfile = NamedTemporaryFile(mode="w",)
    json.dump(data, tfile)
    tfile.flush()
    result = runner.invoke(app, ["find-wikipedia-people-from-file", "--file-path", tfile.name])
    assert result.exit_code == 1


def test_main():
    result = runner.invoke(app)
    assert result.exit_code == 0
    for scientist in SCIENTISTS:
        assert scientist in result.stdout

