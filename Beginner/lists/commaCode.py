'''
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''

def comma_code(words):
    if not words:
        return ''
    result = ''
    for i, item in enumerate(words):
        if len(words) == 1:
            result = str(item)
        elif i == len(words) - 1:
            result += 'and ' + str(item)
        else:
            result += str(item) + ', '
    return result


spam = []
#spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))