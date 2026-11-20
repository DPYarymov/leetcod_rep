while True:
    namber = input(str('Введите римское число : \n'))
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = []

    for i in namber:
        roman_list.append(i)

    arabian_list = []

    for i in roman_list:
        arabian_list.append(my_dict[i])

    arabian_list.reverse()
    a = 0
    previous_element = None

    for current_element in arabian_list:
      if previous_element is not None:
        if current_element >= previous_element:
            a += current_element
        else:
            a -= current_element
      else:
          a += current_element
      previous_element = current_element

    print(a)
