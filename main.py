def larger_abs_value(value_1, value_2):
    if value_1 < 0:
        value_1 = -value_1
    if value_2 < 0:
        value_2 = -value_2
    if value_1 > value_2:
        print(value_1)
    if value_2 > value_1:
        print(value_2)
    if value_1 == value_2:
        print('Numbers have the same absolute value.')

larger_abs_value(-400, 40)
