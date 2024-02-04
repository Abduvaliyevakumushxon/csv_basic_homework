#Define function,Get coloumn names from a csv file
import csv
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    f=open("data.csv")
    data=csv.reader(f)
    return len(list(data)[0])
print(get_column_names('data.csv'))
    
# Read the csv file