import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f=open("data.csv")
    data=csv.reader(f)
    return list(data)
print(find_number_of_columns('data.csv'))

# Read the csv file