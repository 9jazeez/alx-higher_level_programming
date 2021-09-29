#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for i in range(list_length):
            try:
                a = my_list_1[i] / my_list_2[i]
                new_list.append(a)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
            except IndexError:
                print("out of range")
                new_list.append(0)
    except:
        print("Wrong type")
        new_list.append(0)

    finally:
        return (new_list)
