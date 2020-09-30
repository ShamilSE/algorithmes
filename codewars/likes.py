def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    for name in names:
        if len(names) == 1:
            return ''.join(name + ' likes this')
        if len(names) == 2:
            return ''.join(names[0] + ' and ' + names[1] + ' likes this')
        if len(names) == 3:
            return ''.join(names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')
        if len(names) >= 4:
            return ''.join(names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this')


print (likes(['Shamil', 'Daniil']))