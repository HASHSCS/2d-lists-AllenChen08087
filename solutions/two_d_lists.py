# TODO: Implement a function that takes a two-dimensional list and returns the number of rows and the number of columns separately
def get_row_count(two_d_list):
    return len(two_d_list)

def get_column_count(two_d_list):
    return len(two_d_list[0])

# TODO: Implement a function that returns the element at the specified row and column in a two-dimensional list
def get_element(two_d_list, row, col):
    return two_d_list[row][col]

# TODO: Implement a function that returns the sum of all numbers in a two-dimensional list
def sum_two_d_list(two_d_list):
    sum = 0
    for row in two_d_list:
        for item in row:
            sum = sum + item
    return sum

# TODO: Implement a function that prints each row of a two-dimensional list on a new line
def print_rows(two_d_list):
    for row in two_d_list:
        print(row)


# TODO: Implement a function that checks whether a given value is present in any of the sublists within a two-dimensional list
def contains_value(two_d_list, value):
    flag = False
    for row in two_d_list:
        for item in row:
            if item == value:
                flag = True
    return flag

# TODO: Implement a function that appends a new value at the end of every sublist within a two-dimensional list
def append_to_sublists(two_d_list, value):
    for i in range (0,len(two_d_list)):
        two_d_list[i].append(value)
    return two_d_list

# TODO: Implement a function that replaces all instances of old_value with new_value in a two-dimensional list
def replace_in_two_d_list(two_d_list, old_value, new_value):
    for i in range (0,len(two_d_list)):
        for j in range (0, len(two_d_list[i])):
                if two_d_list[i][j] == old_value:
                    two_d_list[i][j] = new_value
    return two_d_list
                        


# TODO: Implement a function that returns a new list containing only the first elements of each sublist in a two-dimensional list
def first_elements(two_d_list):
    result_list = []
    if len(two_d_list) > 1:
        for i in range(len(two_d_list)):
            result_list.append(two_d_list[i][0])
    return result_list

# TODO: Implement a function that returns a list of lists, where each inner list contains the elements of the original sublists that are at even indices
def even_elements_sublists(two_d_list):
    result = []
    for sublist in two_d_list:
        even_elements = sublist[::2]
        result.append(even_elements)
    return result


# TODO: Implement a function that concatenates all sublists in a two-dimensional list into a single list
def concatenate_sublists(two_d_list):
    list = []
    for row in two_d_list:
        for item in row:
            list.append(item)
    return list
