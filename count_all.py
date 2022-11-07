def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    letters = 0
    digits = 0
    for i in txt:
        if i.isalpha():
            letters+=1
        if i.isdigit():
            digits+=1
    answer = {'LETTERS':letters,'DIGITS':digits}
    return answer