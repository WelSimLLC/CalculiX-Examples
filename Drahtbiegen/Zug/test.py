#!/usr/bin/python
import os
import multiprocessing
import shutil

# Move new files and folders to 'Refs'
def move(old_snap):
    new_snap = os.listdir(os.curdir)
    if not os.path.exists('Refs'):
        os.mkdir('Refs')
    for f in new_snap:
        if not f in old_snap:
            fname = os.path.basename(f)
            new_name = os.path.join(os.curdir, 'Refs', fname)
            if os.path.isfile(new_name):
                os.remove(new_name)
            if os.path.isdir(new_name):
                shutil.rmtree(new_name)
            os.rename(f, new_name)

if __name__ == '__main__':

    # Enable multithreading for ccx
    os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

    # Explicitly move to example's directory
    os.chdir(os.path.dirname(__file__))

    # Run the example
    snap = os.listdir(os.curdir)
    # TODO
    # os.system('../../Scripts/param.py par.pre.fbd')
    # os.system('cgx -b pre.fbd')
    # os.system('cgx -b vpre.fbd')
    # os.system('cgx -b plots.fbd')
    # os.system('cgx -b 2D.fbd')
    # os.system('cgx -b Zug-post.fbd')
    # os.system('cgx -b expansion.fbd')
    # os.system('cgx -b expansion2.fbd')
    # os.system('cgx -b expansion3.fbd')
    move(snap)
