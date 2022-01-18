import csv
import os


class DataLoader:

    def __init__(self, file_path=None):
        self.data = []

        # In case the user wants to load the data using the function and not this constructor
        if file_path is not None:
            self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        """Loads coordinate data from a csv file."""
        print(f'Loading data started - from {file_path}...')

        if not os.path.exists(file_path):
            raise AssertionError(f'File "{file_path}" not found!')

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Skip header of csv file
            next(csv_reader, None)

            # Load every row
            for row in csv_reader:
                self.data.append((float(row[0]), float(row[1])))

        print(f'Loading data complete - processed {len(self.data)} lines.')
