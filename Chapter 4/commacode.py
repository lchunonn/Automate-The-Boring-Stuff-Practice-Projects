def commacode(lst):
    string = ''
    for i in range(len(lst)):
        if i == len(lst) - 1:
            string += 'and ' + lst[i]
        else:
            string += lst[i] + ', '
    print(string)

spam = ['apples', 'bananas', 'tofu', 'cats']

commacode(spam)