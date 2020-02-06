from os import remove, rename
origfile = open('testfile.txt', 'r')
newfile = open('tempfile.txt', 'w')

for line in origfile:
    newfile.write(line)

origfile.close()

newfile.write('Or you could watch a bad horror flick!')
newfile.write('\nand then append it to your previous file')

newfile.close()

newfile = open('tempfile.txt', 'r')

for line in newfile:
    print(line, end ="")

newfile.close()
remove('tempfile.txt')