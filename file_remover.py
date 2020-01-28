"""Removes files """


import argparse
import glob
import os
import fnmatch
import sys

import vpk_generator


def create_argparser():
    parser = argparse.ArgumentParser(
        description='Do stuff.',
        fromfile_prefix_chars='@')
    parser.add_argument(
        '--dir', '-d',
        required=True,
        help="""Directory to remove stuff from.""")
    parser.add_argument(
        '--include', '-i',
        nargs='+',
        help='List of files to include.')
    parser.add_argument(
        '--exclude', '-e',
        nargs='+',
        help='List of files to always remove. Applied on top of include list.')
    parser.add_argument(
        '--dry',
        action='store_true',
        default=False,
        help='Do a dry run.')

    return parser


def remove_file(file, dry=False):
    print('Removing file:', file)
    if not dry:
        os.remove(file)


if __name__ == '__main__':
    parser = create_argparser()
    args = parser.parse_args()

    # Can't really do anything.
    if not args.include and not args.exclude:
        parser.print_help()
        sys.exit(0)

    if args.dry:
        print('Doing a dry run...')

    folder = None
    if os.path.isdir(args.dir):
        folder = args.dir
    else:
        folder = os.path.dirname(args.dir)

    vpk_generator.change_cwd(folder)

    # Remove excluded files
    if args.exclude:
        for exc in args.exclude:
            files = glob.glob(exc, recursive=True)
            for file in files:
                remove_file(file, args.dry)

    # Remove all files not on the included list.
    if args.include:
        for root, dirs, files in os.walk('.'):
            if len(files) <= 0:
                continue
            for index, file in enumerate(files):
                files[index] = os.path.join(root[2:], file)

            valid_files = []
            for inc in args.include:
                matches = fnmatch.filter(files, inc)
                # All the matches not in the list already.
                new_matches = [x for x in matches if x not in valid_files]
                valid_files = valid_files + new_matches

            files_remove = [x for x in files if x not in valid_files]
            for file in files_remove:
                remove_file(file, args.dry)
