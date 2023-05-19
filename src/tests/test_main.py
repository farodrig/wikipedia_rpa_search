from typer.testing import CliRunner

from main import app, SCIENTISTS

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

def test_main():
    result = runner.invoke(app)
    assert result.exit_code == 0
    for scientist in SCIENTISTS:
        assert scientist in result.stdout

