def mapper(sequence, func):
    """
    Returns sum of elements of sequence and function
    :param sequence:User sequense
    :param func: User function
    :return: Sum of elements of sequence depends on user sequence snd user function
    """
    result = []
    for i in sequence:
        result.append(func(i))
    return sum(result)


lst = [1, 3, 5, 6, 76, 87, 8, 98]

print(mapper(lst,lambda x: x ** 2))



