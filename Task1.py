def progression(first_item:int, amount:int,func):
    """
    Function generates progression depends on user function, can stop generation if receive "True"
    :param first_item: First element of progression
    :param amount: Number of elements
    :param func: User function for progression
    :return: Returns any type element, depends on user function
    """
    item = first_item
    count = 0
    stop = False
    while count < amount and not stop:
        stop = yield item
        item = func(item)
        count += 1


gen = progression(1,10,lambda x: x+1)
count = 1
bound = None
for i in gen:
    print(i)
    if count == bound:
        gen.send(True)
    count +=1

