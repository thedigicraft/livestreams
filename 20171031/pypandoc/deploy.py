#!/usr/bin/env python

import os
import pypandoc

# Save directory names to variables:
source_dir = 'source'
result_dir = 'results'
template_dir = 'templates'

# Open and read the header document into a variable:
fp = open(template_dir+'/header.html', "r")
header = fp.read()
fp.close()

# Open and read the navigation document into a variable:
fp = open(template_dir+'/navigation.html', "r")
navigation = fp.read()
fp.close()

# Open and read the footer document into a variable:
fp = open(template_dir+'/footer.html', "r")
footer = fp.read()
fp.close()

# Scan the source dir for markdown files:
for file in os.listdir(source_dir):

    # Save the file paths to variables:
    source_file = source_dir+'/'+file
    output_file = result_dir+'/'+file.replace('.md','.html')

    # Convert the source file:
    pypandoc.convert_file(source_file,'html', outputfile=output_file)

    # Open and read the new converted file into a variable:
    fp = open(output_file, "r+")
    source = fp.read()

    # Move to the start of the file:
    fp.seek(0)

    # Concat the header, nav, content(source), and footer strings:
    page = header+navigation+source+footer

    # Write new page string to file:
    fp.write(page)

    fp.close()
