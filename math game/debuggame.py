userName = 'Carol'
f = open('userScores.txt', 'r')
for l in f:
    content = l.split(', ')
    print('position 0 is -', content[0])
    if content[0] == userName:
        print(content[0])
        print('success - ', content[1])
