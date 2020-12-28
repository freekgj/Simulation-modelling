def random_number_generator(seed):
    """Generates a sequince of random numbers
       If seed is 412 it gives 122 random numbers back"""
    list_with_numbers = []
    next_number = seed
    while len(list_with_numbers) == len(set(list_with_numbers)):
        next_number*=(next_number)
        if len(str(next_number)) % 2 == 0:
            next_number = str(next_number).zfill(len(str(next_number))+1)
        else:
            next_number = str(next_number)
        index = (int((len(str(next_number))-1) / 2))
        next_number = int(next_number[index-1 : index+2])
        list_with_numbers.append(str(next_number))
    random_numbers = ''.join(str(x) for x in list_with_numbers)
    return int(random_numbers)