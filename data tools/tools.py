import pandas as pd

def csv_to_json(filename):
    df = pd.read_csv(filename)

    new_filename = filename.split('.')[0] + '.json'

    df.to_json(new_filename,orient='records')