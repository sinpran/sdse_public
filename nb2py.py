import sys
import os
import jupytext

this_folder = os.path.dirname(os.path.realpath(__file__))

sourcedests = [
    'lab1/python_tutorial/01_jupyter.py',   
    'lab1/python_tutorial/02_datatypes_scalars.py',   
    'lab1/python_tutorial/03_datatypes_iterables.py',   
    'lab1/python_tutorial/04_controlflow.py',   
    'lab1/python_tutorial/05_codeorg.py',   
    'lab1/python_tutorial/06_comprehensions.py',    
    'lab1/python_tutorial/07_stndlib.py',   
    'lab1/python_tutorial/08_numpy.py',    
    'lab1/python_tutorial/09_matplotlib.py'
]

for source in sourcedests:
    source_folder, source_file = os.path.split(source)
    source_filename, source_ext = os.path.splitext(source_file)
    dest_file = os.path.join(this_folder,source_folder, source_filename+'.ipynb')

    if os.path.exists(dest_file):
        print('Overwrite', os.path.join(source_folder, source_filename+'.ipynb'), '?')
        answer = input('[y/n] ')

        if answer!='y':
            continue

    ntbk = jupytext.read(os.path.join(this_folder,source))
    jupytext.write(ntbk, dest_file, fmt='notebook')
