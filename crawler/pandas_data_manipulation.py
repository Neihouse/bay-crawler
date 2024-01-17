```python
import pandas as pd
from crawler.config import DATA_SCHEMA

class PandasDataManipulator:
    def __init__(self):
        self.data_frame = pd.DataFrame(columns=DATA_SCHEMA)

    def add_data(self, data):
        self.data_frame = self.data_frame.append(data, ignore_index=True)

    def remove_duplicates(self):
        self.data_frame.drop_duplicates(subset=['email'], keep='first', inplace=True)

    def filter_by_source(self, source):
        return self.data_frame[self.data_frame['source'] == source]

    def save_to_csv(self, filename):
        self.data_frame.to_csv(filename, index=False)

    def load_from_csv(self, filename):
        self.data_frame = pd.read_csv(filename)

    def get_data(self):
        return self.data_frame
```