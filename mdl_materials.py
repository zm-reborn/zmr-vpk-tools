"""Prints model's /possible/ materials to a file."""


import argparse
import os
import sys


def get_mat_paths(mats, lowercase=False):
    ret = []
    for p in mats['paths']:
        for tex in mats['textures']:
            s = os.path.join(
                'materials',
                os.path.join(p, tex))
            if lowercase:
                s = s.lower()
            ret.append(s)
    return ret


def int_from_file(fp):
    return int.from_bytes(fp.read(4), 'little')


def read_string_from_file(fp):
    bs = bytearray()
    while True:
        b = fp.read(1)[0]
        if not b:
            break
        bs.append(b)
    return bs.decode('utf-8')


def get_mdl_data(file):
    ret = {
        'textures': [],
        'paths': []
    }

    with open(file, 'rb') as fp:
        # Check magic number
        if fp.read(4).decode('utf-8') != 'IDST':
            raise Exception('Not an mdl file!')

        # Texture names
        fp.seek(204)
        texture_count = int_from_file(fp)
        texture_offset = int_from_file(fp)

        fp.seek(texture_offset)

        for i in range(0, texture_count):
            pos = texture_offset + (i * 64)
            fp.seek(pos)

            name_offset = int_from_file(fp)
            fp.seek(pos + name_offset)

            ret['textures'].append(read_string_from_file(fp))

        # Texture paths
        fp.seek(212)
        texturedir_count = int_from_file(fp)
        texturedir_offset = int_from_file(fp)

        fp.seek(texturedir_offset)

        for i in range(0, texturedir_count):
            pos = texturedir_offset + (i * 4)
            fp.seek(pos)

            name_offset = int_from_file(fp)
            fp.seek(name_offset)

            ret['paths'].append(read_string_from_file(fp))

    return ret


def create_argparser():
    parser = argparse.ArgumentParser(
        description="Get model's material and texture info.",
        fromfile_prefix_chars='@')
    parser.add_argument(
        'mdls',
        nargs='+',
        help="""List of models.""")
    parser.add_argument(
        '--output', '-o',
        default='mats.txt',
        help="""Output file. mats.txt by default.""")
    parser.add_argument(
        '--dir', '-d',
        default=os.getcwd(),
        help="""Directory to set.""")
    parser.add_argument(
        '--lowercase',
        action='store_true',
        default=False,
        help='Lowercase the texture names')

    return parser


if __name__ == '__main__':
    parser = create_argparser()
    args = parser.parse_args()

    with open(args.output, 'w') as fp:
        os.chdir(args.dir)
        firstline = True
        for mdlpath in args.mdls:
            if not firstline:
                fp.write('\n')
            firstline = False
            fp.write(
                '\n'.join(
                    get_mat_paths(
                        get_mdl_data(mdlpath),
                        args.lowercase)))
