import pathlib 
from tempfile import TemporaryDirectory
import cards

def test_card():
    with TemporaryDirectory() as db_dir:
   
        # set up database
        db_path = pathlib.Path(db_dir)
        cards_db = cards.CardsDB(db_path)
        # make sure it's empty
        assert cards_db.count() == 0
    
        # add a card
        c = cards.Card("something")
        card_id = cards_db.add_card(c)
        # count should be 1
        assert cards_db.count() == 1
        # check summary and state
        assert cards_db.get_card(card_id).summary == "something"
        assert cards_db.get_card(card_id).state == "todo"
     
        # start 
        cards_db.start(card_id)
        assert cards_db.get_card(card_id).state == "in prog"
      
        # finish
        cards_db.finish(card_id)
        assert cards_db.get_card(card_id).state == "done"
       
        # delete
        cards_db.delete_card(card_id)
        # count should be 0
        assert cards_db.count() == 0
        