#!/usr/bin/env python
"""To generate the fields mapping config to ease editing.
A file named "fields_mapping.py" will be generated.
This script will let you confirm if finds an existing "fields_mapping.py"
in the same directory.

To make the generated mapping Dict have the same fields order, 
ordereddict is required.
"""
OUT_FILE_NAME = "fields_mapping.py"
LINE_END = "\r\n"   

def space_word(word):
    """make the Camel like words to Space seperated words
    """
    import string
    return "".join([x if word.index(x) == 0 
        or x in string.ascii_lowercase else " " + x
        for x in word])

def gen_mapping(infile):
    """Generate a mapping file based on infile csv
    """
    fh = open(infile)
    cont = fh.read()
    fh.close()
    row = cont.split(LINE_END)[0]

    from ordereddict import OrderedDict
    out = OrderedDict()
    for x in row.split(","):
        #y = space_word(x)
        out.update({ x : x})

    ret = """# coding: utf-8
'''
mapping from Google Contact standard field name to
our customized fields name. 
Edit it to make it fit your fields.

About Mapping:
-----------------
MAPPING = {
    "Goolge_Field" : "Our Field",
    ...
}

So we need to check and edit the left side of the dict(i.e Key)
to make the right side(i.e Value) match the left as possible.
'''
"""
    from django.utils import simplejson
    ret += "MAPPING = " + simplejson.dumps(out, indent=4)
    outfile = open(OUT_FILE_NAME, "w")
    outfile.write(ret)

def main():
    import optparse
    usage = """\
    python gen_fields_mapping.py --infile=FILE
    """
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-i', '--infile', default=None, metavar='infile',
        help="Input CSV file")
    (options, args) = parser.parse_args()
    if args:
        parser.print_help()
        parser.exit(msg='\nUnexpected arguments: %s\n' % ' '.join(args))
    infile = options.infile
    if infile is None:
        parser.exit(msg='\nNeed the Infile argument.\n')
    if infile.split(".")[-1] != "csv":
        parser.exit(msg='\nNeed a CSV file as the Infile argument.\n')
    import os
    if os.path.exists(OUT_FILE_NAME):
        parser.exit(msg='\nFile with name %s already exists in this directory.\n' % OUT_FILE_NAME)
    gen_mapping(infile)


if __name__ == "__main__":
    main()
