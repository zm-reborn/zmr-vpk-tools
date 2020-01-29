import sys

if __name__ == '__main__':
    data = []
    in_name = sys.argv[1]
    with open(in_name, 'r') as fp:
        data = list(dict.fromkeys(fp.read().splitlines()))
    
    if len(data) > 0:
        out_name = sys.argv[2] if len(sys.argv) >= 3 else in_name
        with open(out_name, 'w') as fp:
            fp.write('\n'.join(data))
        print('Wrote to', out_name)
