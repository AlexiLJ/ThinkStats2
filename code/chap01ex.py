"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ex():
    df = nsfg.ReadFemPreg()
    num = df.pregnum.value_counts().sort_index()
    
    return num 

print(ex())

def val_ex():
    df = nsfg.ReadFemPreg()
    pr_map = nsfg.MakePregMap(df)

    for index, pregnum in df.pregnum.items():
        caseid = df.caseid[index]
        indicies = pr_map[caseid]
        if len(indicies) != pregnum:
            print(caseid, len(indices), pregnum)
            return False
    return True 

   
    #print(case_id)

 
    #return df.pr_num #df.outcome[indices].values
print(val_ex())


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


# if __name__ == '__main__':
#     main(*sys.argv)
