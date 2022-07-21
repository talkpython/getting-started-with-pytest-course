from pathlib import Path
from tempfile import TemporaryDirectory
import cards

def test_empty():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)

        count = db.count()
        db.close()

        assert count == 0

