import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from instagram_scraper.main import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "project skeleton" in captured.out
