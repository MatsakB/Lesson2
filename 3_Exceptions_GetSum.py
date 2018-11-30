def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        print ('bye')

print(get_summ('h', 6))