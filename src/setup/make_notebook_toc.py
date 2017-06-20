#!/usr/bin/env python

# Makefile python script to generate table of contents for
# notebook directory

# script will generate a table of contents for any notebooks
# found in the notebooks directory.  Each notebook will
# be sought for markdown cells and create links to them
# in a hierarchical form.

# Rules:
# - each notebook gets its own section
# - any markdown cell with a h1 heading (e.g. #) will
#   have it's content posted to the README; this heading
#   will NOT be added to the TOC
# - any markdown cell with an h2 (or deeper) heading will
#   be added to the TOC in a hierarchical way


import sys, os, json, re

# GLOBALS
assert len(sys.argv) == 2, "You must supply the notebook dir!"
dir = sys.argv[1]


# GET LIST OF NOTEBOOKS
nbs = []
for root, dirnames, filenames in os.walk(dir):
    if any('.ipynb' in f for f in filenames) and '.ipynb_checkpoints' not in root: 
        nbs.extend([os.path.join(root, l) for l in filenames if '.ipynb' in l])

# PARSE EACH NOTEBOOK
for f in sorted(nbs):

    print "**[%s](/%s)**" %(f.split('/')[-1], f)
    print "---"
    print ""
    with open(f) as data_file:    
        cells = json.load(data_file)['cells']
        file_intro = ''
        toc = []
     
        # CHECK EACH CELL AND FIND 'MARDOWN' TYPE
        for cell in cells:
            if cell['cell_type'] == 'markdown':
                source = cell['source']

                level = source[0].count('#') # assume heading string on first line
                if level == 1: 
                    file_intro = ''.join(source[1:])
                elif level > 1:
                    header = re.sub(r'#+', '', source[0]).strip()
                    toc.append('  ' * (level - 2) + "* [%s](/%s)" %(header, f)) # unfortunately anchor links don't work in the rendered notebooks

        print file_intro
        if len(toc):
            print " "
            print "**TOC:**"
            print '\n'.join(toc)

    print ""

