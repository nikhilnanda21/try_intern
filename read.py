import pandas as pd
import os
import shutil

'''This file just creates a copy of the Raw file called Gen-1'''

src = 'Raw'
dest = 'Gen-1'

destination = shutil.copytree(src, dest)
