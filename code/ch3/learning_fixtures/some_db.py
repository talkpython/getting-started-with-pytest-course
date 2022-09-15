class DB():
    def __init__(self):
        print("\n-- connect to database --")

    def close(self):
        print("\n-- disconnect from database --")

    def some_action(self):
        print("\n-- DB::some_action() --")
        return 42
