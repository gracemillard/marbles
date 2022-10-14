from processor.marble_processor import MarbleProcessor
from common.filter_params import FilterParams
import pandas as pd
import json


def main(collection):
    if not collection:
        raise ValueError("Empty collection, cannot proceed")

    marble_processor = MarbleProcessor()
    marble_processor.process_marbles(collection)



if __name__ == "__main__":
    print("running")
    collection= [
        {"id": 1, "color": "blue", "name": "Bob", "weight": 0.5 },
        { "id": 2, "color": "red", "name": "John Smith", "weight": 0.25 },
        { "id": 3, "color": "violet", "name": "Bob O'Bob", "weight": 0.5 },
        { "id": 4, "color": "indigo", "name": "Bob Dad-Bob", "weight": 0.75 },
        { "id": 5, "color": "yellow", "name": "John", "weight": 0.5 },
        { "id": 6, "color": "orange", "name": "Bob", "weight": 0.25 },
        { "id": 7, "color": "blue", "name": "Smith", "weight": 0.5 },
        { "id": 8, "color": "blue", "name": "Bob", "weight": 0.25 },
        { "id": 9, "color": "green", "name": "Bobb Ob", "weight": 0.75 },
        { "id": 10, "color": "blue", "name": "Bob", "weight": 0.5 }
        ]
    main(collection)