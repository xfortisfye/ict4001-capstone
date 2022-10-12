'''
increase dataset
'''

import csv
import pandas as pd
import os

FEATURES_COL = 2
export_dir_path = os.path.join(os.getcwd(), "export")

import_csv = pd.read_csv("01_original_rand/" + "original_test_rand.csv")
export_csv_name = "pair_test_rand" + ".csv"
export_csv_path = os.path.join(os.getcwd(), "02_pair_rand", export_csv_name)

import_csv = pd.read_csv("11_original_IRDR/" + "original_test_IR.csv")
export_csv_name = "pair_test_IR" + ".csv"
export_csv_path = os.path.join(os.getcwd(), "12_pair_IRDR", export_csv_name)

import_csv = pd.read_csv("11_original_IRDR/" + "original_test_DR.csv")
export_csv_name = "pair_test_DR" + ".csv"
export_csv_path = os.path.join(os.getcwd(), "12_pair_IRDR", export_csv_name)

headerList = ['Subject', 'Sequence']
for _ in range(3):
    headerList.append(f"T2-D|0")
    for _ in range(5-1):
        headerList.append(f"T2-I|{_}+{_+1}")
        headerList.append(f"T2-PF|{_}+{_+1}")
        headerList.append(f"T2-RF|{_}+{_+1}")
        headerList.append(f"T2-NG|{_}+{_+1}")
        headerList.append(f"T2-D|{_+1}")
    headerList.append(f"T2-D|S")
    headerList.append(f"T2-I|S")
    headerList.append(f"T2-PF|S")
    headerList.append(f"T2-RF|S")
    headerList.append(f"T2-DT-S")

    headerList.append(f"T2-D|M")
    headerList.append(f"T2-I|M")
    headerList.append(f"T2-PF|M")
    headerList.append(f"T2-RF|M")
    headerList.append(f"T2-DT-M")

    headerList.append(f"T2-D|VAR")
    headerList.append(f"T2-I|VAR")
    headerList.append(f"T2-PF|VAR")
    headerList.append(f"T2-RF|VAR")
    headerList.append(f"T2-DT-VAR")

    headerList.append(f"T2-D|SD")
    headerList.append(f"T2-I|SD")
    headerList.append(f"T2-PF|SD")
    headerList.append(f"T2-RF|SD")
    headerList.append(f"T2-DT-SD")

    for _ in range(5-2):
        headerList.append(f"T3-I|{_}+{_+2}")
        headerList.append(f"T3-PF|{_}+{_+2}")
        headerList.append(f"T3-RF|{_}+{_+2}")
        headerList.append(f"T3-NG|{_}+{_+2}")

    headerList.append(f"T3-I|S")
    headerList.append(f"T3-PF|S")
    headerList.append(f"T3-RF|S")
    headerList.append(f"T3-NG|S")

    headerList.append(f"T3-I|M")
    headerList.append(f"T3-PF|M")
    headerList.append(f"T3-RF|M")
    headerList.append(f"T3-NG|M")

    headerList.append(f"T3-I|VAR")
    headerList.append(f"T3-PF|VAR")
    headerList.append(f"T3-RF|VAR")
    headerList.append(f"T3-NG|VAR")

    headerList.append(f"T3-I|SD")
    headerList.append(f"T3-PF|SD")
    headerList.append(f"T3-RF|SD")
    headerList.append(f"T3-NG|SD")

    for _ in range(5-3):
        headerList.append(f"T4-I|{_}+{_+3}")
        headerList.append(f"T4-PF|{_}+{_+3}")
        headerList.append(f"T4-RF|{_}+{_+3}")
        headerList.append(f"T4-NG|{_}+{_+3}")

    headerList.append(f"T4-I|S")
    headerList.append(f"T4-PF|S")
    headerList.append(f"T4-RF|S")
    headerList.append(f"T4-NG|S")

    headerList.append(f"T4-I|M")
    headerList.append(f"T4-PF|M")
    headerList.append(f"T4-RF|M")
    headerList.append(f"T4-NG|M")

    headerList.append(f"T4-I|VAR")
    headerList.append(f"T4-PF|VAR")
    headerList.append(f"T4-RF|VAR")
    headerList.append(f"T4-NG|VAR")

    headerList.append(f"T4-I|SD")
    headerList.append(f"T4-PF|SD")
    headerList.append(f"T4-RF|SD")
    headerList.append(f"T4-NG|SD")

    for _ in range(5-4):
        headerList.append(f"T5-I|{_}+{_+4}")
        headerList.append(f"T5-PF|{_}+{_+4}")
        headerList.append(f"T5-RF|{_}+{_+4}")
        headerList.append(f"T5-NG|{_}+{_+4}")

with open(export_csv_path, 'w', newline='') as file:
    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
    dw.writeheader()

    print(f"CSV file will be created: {export_csv_path}")

with open(export_csv_path, 'a', newline='') as file:
    writer = csv.writer(file)

    for body in range(0, 80, 10):
        for first in range(0, 10):
            for second in range(0, 10):
                if second == first:
                    pass
                else:    
                    first_row = body + first
                    placeholder = import_csv.iloc[first_row].values.tolist()
                    sec_row = body + second
                    placeholder.extend(import_csv.iloc[sec_row, FEATURES_COL:].values.tolist())
                    writer.writerow([*placeholder])
                    placeholder.clear()

    # for body in range(0, 80, 10):
    #     for first in range(0, 10):
    #         for second in range(0, 10):
    #             for third in range(0, 10):
    #                 if second == first or third == first or third == second:
    #                     pass
    #                 else:    
    #                     first_row = body + first
    #                     placeholder = import_csv.iloc[first_row].values.tolist()
    #                     sec_row = body + second
    #                     placeholder.extend(import_csv.iloc[sec_row, FEATURES_COL:].values.tolist())
    #                     third_row = body + third
    #                     placeholder.extend(import_csv.iloc[third_row, FEATURES_COL:].values.tolist())
    #                     writer.writerow([*placeholder])
    #                     placeholder.clear()

    # for body in range(0, 80, 10):
    #     for first in range(0, 3):
    #         for second in range(3, 6):
    #             for third in range(6, 9):
    #                 if second == first or third == first or third == second:
    #                     pass
    #                 else:    
    #                     first_row = body + first
    #                     placeholder = import_csv.iloc[first_row].values.tolist()
    #                     sec_row = body + second
    #                     placeholder.extend(import_csv.iloc[sec_row, FEATURES_COL:].values.tolist())
    #                     third_row = body + third
    #                     placeholder.extend(import_csv.iloc[third_row, FEATURES_COL:].values.tolist())
    #                     writer.writerow([*placeholder])
    #                     placeholder.clear()