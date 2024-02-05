import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f=open('data.csv')
    a=csv.reader(f)
    l=[]
    for i in a:
        l.append(i)
    return l[0]
print(get_first_column('data.csv'))    
# Read the csv file