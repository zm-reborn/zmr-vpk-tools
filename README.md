# VPK Tools
Generating [VPK](https://developer.valvesoftware.com/wiki/VPK)s with [pattern matching](https://www.gnu.org/software/findutils/manual/html_node/find_html/Shell-Pattern-Matching.html).

## Requirements:
- Python 3



Examples in `zmr/assets_css.bat`

See `python3 vpk_generator.py --help` for more commands.

## Building your own VPKs:
If you have a folder you want to pack, it's as easy as:
`python3 vpk_generator.py --vpk <path_to_vpk_exe> --dir <content_dir> --include **`

The point of this tool is that you want to use pattern matching. These are relative to the directory.
You can use this:
`--include materials/* models/*` or `--include @include_list.txt`
To pack all materials and models, or load the list from a file.

You can also exclude files:
`--exclude materials/**/*.vmt models/**/*.phy` or `--exclude @exclude_list.txt`
To exclude all .vmt and .phy files, or load the list from a file.

## Generating just a response file:
`python3 vpk_generator.py --dir <content_dir> --include ** --responsefile <filename>`

## Building ZMR VPKs:
- Place the content you want to be packed somewhere.
- Configure and run `zmr/assets_css.bat` **Modify `VPK_EXE` & `CONTENT_DIR` variables in these scripts!**
