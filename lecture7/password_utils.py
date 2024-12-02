
def read_lines_from_file(filename:str) -> list:	
    """Assumes one word per line, extracts them into a list 

    Args:
        filename (str): a fully qualified path to the txt file containing words

    Returns:
        list: python list of all words
    """
    with open(filename) as f:
        contents = f.read().splitlines()
    return contents
