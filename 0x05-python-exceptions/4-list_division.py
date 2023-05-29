#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                raise TypeError("wrong type")

            if element_2 == 0:
                raise ZeroDivisionError("division by 0")

            result = element_1 / element_2

        except IndexError:
            print("out of range")
            result = 0

        except ZeroDivisionError:
            print("division by 0")
            result = 0

        except TypeError:
            print("wrong type")
            result = 0

        finally:
            result_list.append(result)

    return (result_list)
