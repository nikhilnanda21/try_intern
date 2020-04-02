import pandas as pd
import numpy as np
import csv
'''This file does the actual manipulation of the .txt files'''

# Loop through both the years
for i in [2018, 2019]:
    # Base path
    path_r_0 = 'Raw/[IN-023C]/'
    path_w_0 = 'Gen-1/[IN-023C]/'

    # Separate paths for each year
    if i==2018:
        path_r_1 = path_r_0 + '2018/2018-12/'
        path_w_1 = path_w_0 + '2018/2018-12/'
    else:
        path_r_1 = path_r_0 + '2019/2019-01/'
        path_w_1 = path_w_0 + '2019/2019-01/'

    # Path for each of the subdirectories
    for j in ['Inverter_1,I1', 'Inverter_2,I2', 'MFM,MFM1', 'WMS,WMS']:
        path_r_2 = path_r_1 + j.split(',')[0] + '/[IN-023C]-' + j.split(',')[1]
        path_w_2 = path_w_1 + j.split(',')[0] + '/[IN-023C]-' + j.split(',')[1]

        # Path for each .txt file
        for k in range(1, 32):
            if i==2018:
                if k<10:
                    path_r_3 = path_r_2 + '-2018-12-0' + str(k) + '.txt'
                    path_w_3 = path_w_2 + '-2018-12-0' + str(k) + '.txt'
                else:
                    path_r_3 = path_r_2 + '-2018-12-' + str(k) + '.txt'
                    path_w_3 = path_w_2 + '-2018-12-' + str(k) + '.txt'
            else:
                if k<10:
                    path_r_3 = path_r_2 + '-2019-01-0' + str(k) + '.txt'
                    path_w_3 = path_w_2 + '-2019-01-0' + str(k) + '.txt'
                else:
                    path_r_3 = path_r_2 + '-2019-01-' + str(k) + '.txt'
                    path_w_3 = path_w_2 + '-2019-01-' + str(k) + '.txt'

            # Path for the required text files
            # print(path_r_3)
            # print(path_w_3)

            # Inverters text file manipulation
            if j.split(',')[1] == 'I1' or j.split(',')[1] == 'I2':
                df = pd.read_table(path_r_3)
                cols = df.columns.tolist()

                cols.insert(0, cols.pop(cols.index('i32')))
                df = df.reindex(columns= cols)
                df.rename(columns={'i32':'Timestamp'}, inplace=True)

                df["i1"].fillna("NA", inplace = True)

                f = open(path_w_3, "w")
                f.write(df.to_csv(sep=' ', index=False, na_rep="NULL", float_format="%.0f", quoting=csv.QUOTE_NONE, escapechar=" "))
                f.close()
            # MFM text file manipulation
            elif j.split(',')[1] == 'MFM1':
                df = pd.read_table(path_r_3)
                cols = df.columns.tolist()

                cols.insert(0, cols.pop(cols.index('m63')))
                df = df.reindex(columns= cols)
                df.rename(columns={'m63':'Timestamp'}, inplace=True)

                df["m1"].fillna("NA", inplace = True)

                f = open(path_w_3, "w")
                f.write(df.to_csv(sep=' ', index=False, na_rep="NULL", float_format="%.0f", quoting=csv.QUOTE_NONE, escapechar=" "))
                f.close()
            # WMS text file manipulation
            else:
                df = pd.read_table(path_r_3)
                cols = df.columns.tolist()

                cols.insert(0, cols.pop(cols.index('w23')))
                df = df.reindex(columns= cols)
                df.rename(columns={'w23':'Timestamp'}, inplace=True)

                df["w1"].fillna("NA", inplace = True)

                f = open(path_w_3, "w")
                f.write(df.to_csv(sep=' ', index=False, na_rep="NULL", float_format="%.0f", quoting=csv.QUOTE_NONE, escapechar=" "))
                f.close()
