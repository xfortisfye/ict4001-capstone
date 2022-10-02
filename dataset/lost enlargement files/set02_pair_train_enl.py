'''
increase dataset
'''
import time
import csv
import pandas as pd
import os
from sys import exit

export_dir_path = os.path.join(os.getcwd(), "export")
csv_name = "m2m_train" + ".csv"
csv_path = os.path.join(export_dir_path, csv_name)

small_df = pd.read_csv("dataset/" + "train.csv")

headerList = ['Subject', 'Class', 'Sequence']
for _ in range(2):
    headerList.append(f"T2-D|0")
    for _ in range(10-1):
        headerList.append(f"T2-I|{_}+{_+1}")
        headerList.append(f"T2-PF|{_}+{_+1}")
        headerList.append(f"T2-RF|{_}+{_+1}")
        headerList.append(f"T2-NG|{_}+{_+1}")
        headerList.append(f"T2-D|{_+1}")
    headerList.append(f"T2-D|S")
    headerList.append(f"T2-I|S")
    headerList.append(f"T2-PF|S")
    headerList.append(f"T2-RF|S")
    headerList.append(f"T2-NG|S")

    headerList.append(f"T2-D|M")
    headerList.append(f"T2-I|M")
    headerList.append(f"T2-PF|M")
    headerList.append(f"T2-RF|M")
    headerList.append(f"T2-NG|M")

    headerList.append(f"T2-D|VAR")
    headerList.append(f"T2-I|VAR")
    headerList.append(f"T2-PF|VAR")
    headerList.append(f"T2-RF|VAR")
    headerList.append(f"T2-NG|VAR")

    headerList.append(f"T2-D|SD")
    headerList.append(f"T2-I|SD")
    headerList.append(f"T2-PF|SD")
    headerList.append(f"T2-RF|SD")
    headerList.append(f"T2-NG|SD")

    for _ in range(10-2):
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

    for _ in range(10-3):
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

    for _ in range(10-4):
        headerList.append(f"T5-I|{_}+{_+4}")
        headerList.append(f"T5-PF|{_}+{_+4}")
        headerList.append(f"T5-RF|{_}+{_+4}")
        headerList.append(f"T5-NG|{_}+{_+4}")
    headerList.append(f"T5-I|S")
    headerList.append(f"T5-PF|S")
    headerList.append(f"T5-RF|S")
    headerList.append(f"T5-NG|S")

    headerList.append(f"T5-I|M")
    headerList.append(f"T5-PF|M")
    headerList.append(f"T5-RF|M")
    headerList.append(f"T5-NG|M")

    headerList.append(f"T5-I|VAR")
    headerList.append(f"T5-PF|VAR")
    headerList.append(f"T5-RF|VAR")
    headerList.append(f"T5-NG|VAR")

    headerList.append(f"T5-I|SD")
    headerList.append(f"T5-PF|SD")
    headerList.append(f"T5-RF|SD")
    headerList.append(f"T5-NG|SD")

    for _ in range(10-5):
        headerList.append(f"T6-I|{_}+{_+5}")
        headerList.append(f"T6-PF|{_}+{_+5}")
        headerList.append(f"T6-RF|{_}+{_+5}")
        headerList.append(f"T6-NG|{_}+{_+5}")
    headerList.append(f"T6-I|S")
    headerList.append(f"T6-PF|S")
    headerList.append(f"T6-RF|S")
    headerList.append(f"T6-NG|S")

    headerList.append(f"T6-I|M")
    headerList.append(f"T6-PF|M")
    headerList.append(f"T6-RF|M")
    headerList.append(f"T6-NG|M")

    headerList.append(f"T6-I|VAR")
    headerList.append(f"T6-PF|VAR")
    headerList.append(f"T6-RF|VAR")
    headerList.append(f"T6-NG|VAR")

    headerList.append(f"T6-I|SD")
    headerList.append(f"T6-PF|SD")
    headerList.append(f"T6-RF|SD")
    headerList.append(f"T6-NG|SD")

    for _ in range(10-6):
        headerList.append(f"T7-I|{_}+{_+6}")
        headerList.append(f"T7-PF|{_}+{_+6}")
        headerList.append(f"T7-RF|{_}+{_+6}")
        headerList.append(f"T7-NG|{_}+{_+6}")

    headerList.append(f"T7-I|S")
    headerList.append(f"T7-PF|S")
    headerList.append(f"T7-RF|S")
    headerList.append(f"T7-NG|S")

    headerList.append(f"T7-I|M")
    headerList.append(f"T7-PF|M")
    headerList.append(f"T7-RF|M")
    headerList.append(f"T7-NG|M")

    headerList.append(f"T7-I|VAR")
    headerList.append(f"T7-PF|VAR")
    headerList.append(f"T7-RF|VAR")
    headerList.append(f"T7-NG|VAR")

    headerList.append(f"T7-I|SD")
    headerList.append(f"T7-PF|SD")
    headerList.append(f"T7-RF|SD")
    headerList.append(f"T7-NG|SD")

    for _ in range(10-7):
        headerList.append(f"T8-I|{_}+{_+7}")
        headerList.append(f"T8-PF|{_}+{_+7}")
        headerList.append(f"T8-RF|{_}+{_+7}")
        headerList.append(f"T8-NG|{_}+{_+7}")

    headerList.append(f"T8-I|S")
    headerList.append(f"T8-PF|S")
    headerList.append(f"T8-RF|S")
    headerList.append(f"T8-NG|S")

    headerList.append(f"T8-I|M")
    headerList.append(f"T8-PF|M")
    headerList.append(f"T8-RF|M")
    headerList.append(f"T8-NG|M")

    headerList.append(f"T8-I|VAR")
    headerList.append(f"T8-PF|VAR")
    headerList.append(f"T8-RF|VAR")
    headerList.append(f"T8-NG|VAR")

    headerList.append(f"T8-I|SD")
    headerList.append(f"T8-PF|SD")
    headerList.append(f"T8-RF|SD")
    headerList.append(f"T8-NG|SD")


    for _ in range(10-8):
        headerList.append(f"T9-I|{_}+{_+8}")
        headerList.append(f"T9-PF|{_}+{_+8}")
        headerList.append(f"T9-RF|{_}+{_+8}")
        headerList.append(f"T9-NG|{_}+{_+8}")
        
    headerList.append(f"T9-I|S")
    headerList.append(f"T9-PF|S")
    headerList.append(f"T9-RF|S")
    headerList.append(f"T9-NG|S")

    headerList.append(f"T9-I|M")
    headerList.append(f"T9-PF|M")
    headerList.append(f"T9-RF|M")
    headerList.append(f"T9-NG|M")

    headerList.append(f"T9-I|VAR")
    headerList.append(f"T9-PF|VAR")
    headerList.append(f"T9-RF|VAR")
    headerList.append(f"T9-NG|VAR")

    headerList.append(f"T9-I|SD")
    headerList.append(f"T9-PF|SD")
    headerList.append(f"T9-RF|SD")
    headerList.append(f"T9-NG|SD")

    for _ in range(10-9):
        headerList.append(f"T10-I|{_}+{_+9}")
        headerList.append(f"T10-PF|{_}+{_+9}")
        headerList.append(f"T10-RF|{_}+{_+9}")
        headerList.append(f"T10-NG|{_}+{_+9}")

with open(csv_path, 'w', newline='') as file:
        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
        dw.writeheader()

print(f"CSV file will be created: {csv_path}")

with open(csv_path, 'a', newline='') as file:
    writer = csv.writer(file)
        
    for outer in range(0, 920, 92):
        for row in range(0, 23):
            for inside in range(23, 92):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

        for row in range(23, 46):
            # four
            for inside in range(0, 23):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

            for inside in range(46, 92):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

        for row in range(46, 69):
            # five
            for inside in range(0, 46):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

            for inside in range(69, 92):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

        for row in range(69, 92):
            # six
            for inside in range(0, 69):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()