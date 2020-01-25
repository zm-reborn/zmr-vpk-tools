import sys
import getopt
import os
import argparse
import glob
import subprocess
import fnmatch


def change_cwd(folder):
    print('Changing cwd to :', folder)
    os.chdir(folder)


def create_argparser():
    parser = argparse.ArgumentParser(
        description='Do stuff.',
        fromfile_prefix_chars='@')
    parser.add_argument(
        '--vpk', '-v',
        help='Path to vpk. If not set, will not generate a VPK.')
    parser.add_argument(
        '--dir', '-d',
        required=True,
        help="""Directory to turn into a vpk.
        Include/exclude will be relative to this.""")
    parser.add_argument(
        '--responsefile', '-r',
        default='response_vpk.txt',
        help="""The response filename that gets generated. The VPK executable will use this.
        response_vpk.txt by default.""")
    parser.add_argument(
        '--include', '-i',
        nargs='+',
        help='List of files to include.')
    parser.add_argument(
        '--exclude', '-e',
        nargs='+',
        help='List of files to exclude.')
    parser.add_argument(
        '--vpk_params', '-p',
        help='Optional parameters for vpk.')
    parser.add_argument(
        '--name', '-n',
        help="""Name of the vpk generated.
        If not set, directory name will be used.""")

    return parser

if __name__ == '__main__':
    parser = create_argparser()
    args = parser.parse_args()

    # Display help if we won't be doing anything useful.
    if not args.include and not args.vpk:
        parser.print_help()
        sys.exit(0)

    #
    # Here we go!
    #
    assets_dir = None
    if os.path.isdir(args.dir):
        assets_dir = args.dir
    else:
        assets_dir = os.path.dirname(args.dir)

    response_file = os.path.abspath(args.responsefile)

    if args.include:
        args.exclude = args.exclude if args.exclude else []

        numfiles = 0
        # Generate the response file
        print('Generating response file ', response_file)
        with open(response_file, 'w') as fp:
            change_cwd(assets_dir)
            firstline = True
            for inc in args.include:
                # Get the list of files
                newfiles = glob.glob(inc, recursive=True)
                # Do exclusion
                for exc in args.exclude:
                    for match in fnmatch.filter(newfiles, exc):
                        newfiles.remove(match)
                if len(newfiles):
                    # Add line breaks for the file.
                    if not firstline:
                        newfiles[0] = '\n' + newfiles[0]
                    firstline = False
                    fp.write('\n'.join(newfiles))
                numfiles = numfiles + len(newfiles)
            fp.flush()

        print('Wrote %i files to response file!' % numfiles)

    # User wants to generate the vpk.
    if args.vpk:
        if not os.path.isfile(args.vpk):
            print('%s is not a path to vpk executable!' % args.vpk)
            sys.exit(1)

        vpk_filename = args.name if args.name else os.path.basename(assets_dir)

        print('VPK file %s will be generated...' % vpk_filename)

        vpk_args = [args.vpk]
        vpk_lastargs = [
            'a',
            vpk_filename,
            '@' + response_file
        ]
        optional_args = [args.vpk_params] if args.vpk_params else []
        vpk_args = vpk_args + optional_args + vpk_lastargs

        change_cwd(assets_dir)

        print('Running vpk with args:', vpk_args)

        subprocess.run(vpk_args)

    print('Done!')
