from itertools import combinations

def sub_lists(main_lists):
    length = len(main_lists)
    for item in range(length+1):
        for sublists in combinations(main_lists,item):
            print(list(sublists))
main_lists = [1,2,3,4,5,6]
sub_lists(main_lists)

def alphabet_positions(input_strings):
    result = []
    for char in input_strings:
        if char.isalpha():
            position = ord(char.lower())-ord('a')+1
            result.append(str(position))
        else:
            result.append(char)
    return ''.join(result)
input_strings = 'Hello India my love india'
print(alphabet_positions(input_strings))

def sum_two_numbers(a,b):
    result = sum(range(a,b+1))
    return result
a= 1
b =5
print(sum_two_numbers(a,b))

def lists_empty(main_list):
    if len(main_list) ==0 or main_list is None:
        return []
    else:
        result = sorted(main_list,reverse=True)
        return result
main_list = [10,-20,30,-40,50,-60]
print(lists_empty(main_list))

def mid_index(input_strings):
    length = len(input_strings)
    mid = length//2
    if length%2 ==0:
        result = input_strings[mid-1:mid+1]
        return result
    else:
        result = input_strings[mid]
        return result

input_strings = 'mallikarjuna ra'
print(mid_index(input_strings))

def multiplication_table(numbers):
    result = []
    for item in range(1,numbers+1):
        row = []
        for sublists in range(numbers):
            row.append(item*sublists)
        result.append(row)
    return result
print(multiplication_table(5))

def auto_combine(s1,s2):
    combine = s1+s2
    auto_combine = set(combine)
    return ''.join(auto_combine)
s1 = 'trdtyghihjk'
s2 = 'e4edrtfhjhjkjklm'
print(auto_combine(s1,s2))

def accum(input_strings):
    result = []
    for i,char in enumerate(input_strings):
        field = char.upper()+char.lower()*i
        result.append(field)
    return '_'.join(result)
input_strings = 'abcde'
print(accum(input_strings))

def short_to_long(input_strings):
    result = sorted(input_strings,key=len)
    return result
input_strings = ['malli','srinu','srikanths','srinivassd','joshvika']
print(short_to_long(input_strings))

def multiples_3_or_5(main_list):
    count = 0
    result = []
    for item in main_list:
        if item%3 ==0 or item%5 ==0:
            count+=item
    return count
main_list = [10,11,12,13,14,15,16,17,18,19,20]
print(multiples_3_or_5(main_list))

def multidimensional(main_list):
    result = []
    for item in main_list:
        if isinstance(item,list):
            result.extend(multidimensional(item))
        else:
            result.append(item)
    return result
main_list = [1,2,[3,4],5,6,[7,8,9]]
print(multidimensional(main_list))

def digital_root(numbers):
    if numbers==0:
        return numbers
    return numbers%9
numbers = 788239
print(digital_root(numbers))

def remove_vowels(inputs):
    vowels = 'aeiouAEIOU'
    result = []
    for item in inputs:
        if item not in vowels:
            result.append(item)
    return ''.join(result)
inputs = 'mallikarjuna rao'
print(remove_vowels(inputs))

def substract(a,b):
    set_b = set(b)

    result = [item for item in a if item not in set_b]
    return result
a = [1,2,3,4,5,6,7]
b = [1,2,3,4]
print(substract(a,b))

def maskify(inputs_strings):
    if not inputs_strings:
        return ''
    length = len(input_strings)

    if length <=4:
        return input_strings
    masked_part = '#'*(length-4)
    visible_part = input_strings[-4]
    return masked_part+visible_part
numb1 = '56567877857'
print(maskify(numb1))

def top_two_numbers(main_list):
    first_max = float('-inf')
    second_max = float('-inf')
    set_main = set(main_list)
    for item in set_main:
        if item > first_max:
            second_max = first_max
            first_max = item
        elif item > second_max:
            second_max = item
    return first_max,second_max
main_list = [10,20,20,30,30,40,40,50,50]
print(top_two_numbers(main_list))

def five_words(sentence):
    words = sentence.split()
    result = []
    for item in words:
        if len(item) >= 5:
            result.append(item[::-1])
        else:
            result.append(item)
    return ' '.join(result)
sentence = 'Hello worlsd this is mallikarjuna rao'
print(five_words(sentence))

def xoxo(input_strings):
    x_strings = input_strings.contains('x')
    o_strings = input_strings.contains('o')
    return x_strings,o_strings
input_strings = 'xoxoxoxo'
print(xoxo(input_strings))



