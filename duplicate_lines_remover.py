import sys

if __name__ == '__main__':
    data = []
    with open(sys.argv[1], 'r') as fp:
        data = list(dict.fromkeys(fp.readlines()))
    with open(sys.argv[2], 'w') as fp:
        fp.write('\n'.join(data))
