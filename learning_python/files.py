import sys

f = open(file='wasteland.txt', mode='wt', encoding='utf-8')  # opens file in write/test mode with utf-8 encoding
f.write('What are the roots that clutch, ')  # writes content
f.write('what branches grow\n')  # writes content and translates \n into \n or \r\n depending on the underlying os
f.write('Out of this stony rubbish?')  # writes string
f.close()  # closes files

g = open('wasteland.txt', mode='rt', encoding='utf-8')  # open file in read/text mode
g.read(32)  # reads the bytes/characters specified
g.read()  # the rest of the file
g.read()  # empty string
g.seek(0)  # navigate to byte location
g.readline()  # read to next line break
g.readline()  # no addtiaonl new line just goes to the end
g.readline()  # returns empty string
g.close()  # closing file

h = open('wasteland.txt', mode='at', encoding='utf-8')  # opens the file in append mode
h.writelines(
    ['Son of man, \n',
     'You cannot say, or guess, ',
     'for you know only, \n',
     'A heap of broken images, ',
     'where the sun beats\n']
)  # appends multiple lines to the open file
h.close()  # closes file


# Files are iterators


def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)  # we use this tatic instead of print() to avoid the extra whitespace printing
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])
