#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mine_list = []
    numbs1 = my_list_1[i]
    numbs2 = my_list_2[i]

    for d in range(list_length):
        try:
            result = numbs1 / numbs2
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            mine_list.append(result)
    return (mine_list)
