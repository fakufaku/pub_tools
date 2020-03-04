#!/usr/bin/env python
import argparse, os, sys, re, shutil

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Extracts a list of image files used in a tex file')
    parser.add_argument('file', type=str, help='The tex file')
    parser.add_argument('-o', '--outdir', type=str, help='New folder where to move all the figures')
    args = parser.parse_args()

    if args.outdir is not None and os.path.exists(args.outdir):
        raise ValueError('The output directory already exists. Aborting.')

    with open(args.file, 'r') as f:
        lines = f.readlines()

    # list of commands that include images
    img_cmd = ['includegraphics', 'titlegraphic']

    # list of file extensions to consider
    file_ext = ['', '.jpg', '.pdf', '.png', '.eps']

    # list of directory candidates
    dirs_set = set([os.path.abspath('.')])
    dirs = ['.']

    # list of files found in the tex source
    files_tex = set([])

    for line in lines:
        line = line.strip()

        if len(line) == 0 or line[0] == '%':
            continue

        if 'graphicspath' in line:
            matches = re.findall('{([A-Za-z0-9\._\/]*)}', line)

            # check the dir is not in the list already
            # and add otherwise
            for dir in matches:
                dir_abs = os.path.abspath(dir)
                if dir_abs in dirs_set:
                    continue
                else:
                    dirs.append(dir)
                    dirs_set.add(dir)

        if any([cmd in line for cmd in img_cmd]):
            matches = re.findall('{([A-Za-z0-9\.\-_\/]*)}', line)
            for f in matches:
                files_tex.add(f)

    found_files = []

    for f in files_tex:
        for d in dirs:
            for e in file_ext:
                fn = os.path.join(d, f + e)
                if os.path.exists(fn):
                    found_files.append(fn)

                    if args.outdir is not None:

                        new_fn = os.path.join(args.outdir, f + e)
                        new_dir = os.path.split(new_fn)[0]

                        if not os.path.exists(new_dir):
                            os.makedirs(new_dir)

                        shutil.copy(fn, new_fn)                        



    for f in found_files:
        print(f)

