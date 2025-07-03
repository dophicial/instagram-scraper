import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from instagram_scraper.main import main  # noqa: E402


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "project skeleton" in captured.out
