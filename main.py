"""
combi
"""
import os
import platform
import time
from sys import exit

# keyboard
from pynput.keyboard import Key, Listener
from keyboard import Keyboard
import csv
from time import sleep
import random

def main():
    startFlag = True

    while startFlag is True:
        print("What kind of dataset will you like to generate? \n"
        + "1) Exp 1: Random 10-Letters Dataset for CAPTCHA\n"
        + "2) Exp 2: Identical 10-Letters Dataset for CAPTCHA\n"
        + "3) Exp 3: Controlled dataset for Password\n"
        + "4) Exp 3: Controlled dataset for Password\n"
        + "5) Exp 4: \n"
        + "6) Exp 4: \n"
        + "7) Exp 4: ")
        case = int(input())
        
        if case == 1:
            completed = False
            name = input("What is your name? ")
            round = 25
            count = 1
            captcha = []    

            export_dir_path = prelude(name)
            
            '''
            create merge_df csv file
            '''
            merge_csv_name = "df_" + name + ".csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            if os.path.isfile(merge_csv_path) is True:
                print(f"CSV file exist at {merge_csv_path}")
            else:
                # assign header columns
                headerList = ['', 'key', 'press_time', 'release_time']
                
                # open CSV file and assign header
                with open(merge_csv_path, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Merge_DF CSV file will be created: {merge_csv_path}")

            csv_name = name + ".csv"
            csv_path = os.path.join(export_dir_path, csv_name)

            if os.path.isfile(csv_path) is True:
                print(f"CSV file exist at {csv_path}")
            else:
                # assign header columns
                headerList = ['Subject', 'Class', 'Sequence']
                headerList.append(f"T2-D|0")
                for _ in range(10-1):
                    headerList.append(f"T2-I|{_}+{_+1}")
                    headerList.append(f"T2-PF|{_}+{_+1}")
                    headerList.append(f"T2-RF|{_}+{_+1}")
                    # headerList.append(f"T2-NG|{_}+{_+1}")
                    headerList.append(f"T2-D|{_+1}")
                # headerList.append(f"T2-D|S")
                # headerList.append(f"T2-I|S")
                # headerList.append(f"T2-PF|S")
                # headerList.append(f"T2-RF|S")
                # headerList.append(f"T2-NG|S")

                # headerList.append(f"T2-D|M")
                # headerList.append(f"T2-I|M")
                # headerList.append(f"T2-PF|M")
                # headerList.append(f"T2-RF|M")
                # headerList.append(f"T2-DT-M")

                # headerList.append(f"T2-D|VAR")
                # headerList.append(f"T2-I|VAR")
                # headerList.append(f"T2-PF|VAR")
                # headerList.append(f"T2-RF|VAR")
                # headerList.append(f"T2-DT-VAR")

                # headerList.append(f"T2-D|SD")
                # headerList.append(f"T2-I|SD")
                # headerList.append(f"T2-PF|SD")
                # headerList.append(f"T2-RF|SD")
                # headerList.append(f"T2-NG|SD")

                # for _ in range(10-2):
                #     headerList.append(f"T3-I|{_}+{_+2}")
                #     headerList.append(f"T3-PF|{_}+{_+2}")
                #     headerList.append(f"T3-RF|{_}+{_+2}")
                #     headerList.append(f"T3-NG|{_}+{_+2}")

                # headerList.append(f"T3-I|S")
                # headerList.append(f"T3-PF|S")
                # headerList.append(f"T3-RF|S")
                # headerList.append(f"T3-NG|S")

                # headerList.append(f"T3-I|M")
                # headerList.append(f"T3-PF|M")
                # headerList.append(f"T3-RF|M")
                # headerList.append(f"T3-NG|M")

                # headerList.append(f"T3-I|VAR")
                # headerList.append(f"T3-PF|VAR")
                # headerList.append(f"T3-RF|VAR")
                # headerList.append(f"T3-NG|VAR")

                # headerList.append(f"T3-I|SD")
                # headerList.append(f"T3-PF|SD")
                # headerList.append(f"T3-RF|SD")
                # headerList.append(f"T3-NG|SD")

                # for _ in range(10-3):
                #     headerList.append(f"T4-I|{_}+{_+3}")
                #     headerList.append(f"T4-PF|{_}+{_+3}")
                #     headerList.append(f"T4-RF|{_}+{_+3}")
                #     headerList.append(f"T4-NG|{_}+{_+3}")

                # headerList.append(f"T4-I|S")
                # headerList.append(f"T4-PF|S")
                # headerList.append(f"T4-RF|S")
                # headerList.append(f"T4-NG|S")

                # headerList.append(f"T4-I|M")
                # headerList.append(f"T4-PF|M")
                # headerList.append(f"T4-RF|M")
                # headerList.append(f"T4-NG|M")

                # headerList.append(f"T4-I|VAR")
                # headerList.append(f"T4-PF|VAR")
                # headerList.append(f"T4-RF|VAR")
                # headerList.append(f"T4-NG|VAR")

                # headerList.append(f"T4-I|SD")
                # headerList.append(f"T4-PF|SD")
                # headerList.append(f"T4-RF|SD")
                # headerList.append(f"T4-NG|SD")

                # for _ in range(10-4):
                #     headerList.append(f"T5-I|{_}+{_+4}")
                #     headerList.append(f"T5-PF|{_}+{_+4}")
                #     headerList.append(f"T5-RF|{_}+{_+4}")
                #     headerList.append(f"T5-NG|{_}+{_+4}")
                # headerList.append(f"T5-I|S")
                # headerList.append(f"T5-PF|S")
                # headerList.append(f"T5-RF|S")
                # headerList.append(f"T5-NG|S")

                # headerList.append(f"T5-I|M")
                # headerList.append(f"T5-PF|M")
                # headerList.append(f"T5-RF|M")
                # headerList.append(f"T5-NG|M")

                # headerList.append(f"T5-I|VAR")
                # headerList.append(f"T5-PF|VAR")
                # headerList.append(f"T5-RF|VAR")
                # headerList.append(f"T5-NG|VAR")

                # headerList.append(f"T5-I|SD")
                # headerList.append(f"T5-PF|SD")
                # headerList.append(f"T5-RF|SD")
                # headerList.append(f"T5-NG|SD")

                # for _ in range(10-5):
                #     headerList.append(f"T6-I|{_}+{_+5}")
                #     headerList.append(f"T6-PF|{_}+{_+5}")
                #     headerList.append(f"T6-RF|{_}+{_+5}")
                #     headerList.append(f"T6-NG|{_}+{_+5}")
                # headerList.append(f"T6-I|S")
                # headerList.append(f"T6-PF|S")
                # headerList.append(f"T6-RF|S")
                # headerList.append(f"T6-NG|S")

                # headerList.append(f"T6-I|M")
                # headerList.append(f"T6-PF|M")
                # headerList.append(f"T6-RF|M")
                # headerList.append(f"T6-NG|M")

                # headerList.append(f"T6-I|VAR")
                # headerList.append(f"T6-PF|VAR")
                # headerList.append(f"T6-RF|VAR")
                # headerList.append(f"T6-NG|VAR")

                # headerList.append(f"T6-I|SD")
                # headerList.append(f"T6-PF|SD")
                # headerList.append(f"T6-RF|SD")
                # headerList.append(f"T6-NG|SD")

                # for _ in range(10-6):
                #     headerList.append(f"T7-I|{_}+{_+6}")
                #     headerList.append(f"T7-PF|{_}+{_+6}")
                #     headerList.append(f"T7-RF|{_}+{_+6}")
                #     headerList.append(f"T7-NG|{_}+{_+6}")

                # headerList.append(f"T7-I|S")
                # headerList.append(f"T7-PF|S")
                # headerList.append(f"T7-RF|S")
                # headerList.append(f"T7-NG|S")

                # headerList.append(f"T7-I|M")
                # headerList.append(f"T7-PF|M")
                # headerList.append(f"T7-RF|M")
                # headerList.append(f"T7-NG|M")

                # headerList.append(f"T7-I|VAR")
                # headerList.append(f"T7-PF|VAR")
                # headerList.append(f"T7-RF|VAR")
                # headerList.append(f"T7-NG|VAR")

                # headerList.append(f"T7-I|SD")
                # headerList.append(f"T7-PF|SD")
                # headerList.append(f"T7-RF|SD")
                # headerList.append(f"T7-NG|SD")

                # for _ in range(10-7):
                #     headerList.append(f"T8-I|{_}+{_+7}")
                #     headerList.append(f"T8-PF|{_}+{_+7}")
                #     headerList.append(f"T8-RF|{_}+{_+7}")
                #     headerList.append(f"T8-NG|{_}+{_+7}")

                # headerList.append(f"T8-I|S")
                # headerList.append(f"T8-PF|S")
                # headerList.append(f"T8-RF|S")
                # headerList.append(f"T8-NG|S")

                # headerList.append(f"T8-I|M")
                # headerList.append(f"T8-PF|M")
                # headerList.append(f"T8-RF|M")
                # headerList.append(f"T8-NG|M")

                # headerList.append(f"T8-I|VAR")
                # headerList.append(f"T8-PF|VAR")
                # headerList.append(f"T8-RF|VAR")
                # headerList.append(f"T8-NG|VAR")

                # headerList.append(f"T8-I|SD")
                # headerList.append(f"T8-PF|SD")
                # headerList.append(f"T8-RF|SD")
                # headerList.append(f"T8-NG|SD")

                # for _ in range(10-8):
                #     headerList.append(f"T9-I|{_}+{_+8}")
                #     headerList.append(f"T9-PF|{_}+{_+8}")
                #     headerList.append(f"T9-RF|{_}+{_+8}")
                #     headerList.append(f"T9-NG|{_}+{_+8}")
                    
                # headerList.append(f"T9-I|S")
                # headerList.append(f"T9-PF|S")
                # headerList.append(f"T9-RF|S")
                # headerList.append(f"T9-NG|S")

                # headerList.append(f"T9-I|M")
                # headerList.append(f"T9-PF|M")
                # headerList.append(f"T9-RF|M")
                # headerList.append(f"T9-NG|M")

                # headerList.append(f"T9-I|VAR")
                # headerList.append(f"T9-PF|VAR")
                # headerList.append(f"T9-RF|VAR")
                # headerList.append(f"T9-NG|VAR")

                # headerList.append(f"T9-I|SD")
                # headerList.append(f"T9-PF|SD")
                # headerList.append(f"T9-RF|SD")
                # headerList.append(f"T9-NG|SD")

                # for _ in range(10-9):
                #     headerList.append(f"T10-I|{_}+{_+9}")
                #     headerList.append(f"T10-PF|{_}+{_+9}")
                #     headerList.append(f"T10-RF|{_}+{_+9}")
                #     headerList.append(f"T10-NG|{_}+{_+9}")
                
                # open CSV file and assign header
                with open(csv_path, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"CSV file will be created: {csv_path}")

            with open("captcha/three.txt", "r") as file:
                three = list(map(str, file.read().split()))

            with open("captcha/four.txt", "r") as file:
                four = list(map(str, file.read().split()))

            with open("captcha/five.txt", "r") as file:
                five = list(map(str, file.read().split()))

            with open("captcha/six.txt", "r") as file:
                six = list(map(str, file.read().split()))

            time.sleep(0.1)

            for _ in range(round):
                captcha.append(random.choice(three) + " " + random.choice(six))
                captcha.append(random.choice(four) + " " + random.choice(five))
                captcha.append(random.choice(five) + " " + random.choice(four))
                captcha.append(random.choice(six) + " " + random.choice(three))
            
            random.shuffle(captcha)
            maxCount = len(captcha)

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_csv(csv_path)
            keyboard.set_export(export_dir_path)
            listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
            listener.start()

            for _ in captcha:
                completed = False
                while completed is False:
                    basePwdInput = input(f"Please type \"{_}\": ")
                    sleep(1)
                    if basePwdInput == _:
                        press_df = keyboard.get_press_df()
                        release_df = keyboard.get_release_df()
                        
                        press_df.reset_index(inplace=True, drop=True)
                        release_df.reset_index(inplace=True, drop=True)
                        press_df.drop(press_df[press_df['key']=='key.enter'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.caps_lock'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift_r'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.enter'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.caps_lock'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift_r'].index, inplace=True)
                        
                        if len(press_df.index.values) == len(_) and len(release_df.index.values) == len(_):
                            print(f"Thank you. {maxCount - count} times left. ")
                            keyboard.export_to_csv_1(_)
                            count = count + 1
                            keyboard.reset()
                            completed = True
                        else:
                            keyboard.reset()
                            print(f"Invalid. Please key in {_} without any backspace or errors. ")
                    else:
                        keyboard.reset()
                        print("Password is incorrect. Please retry. ")

        elif case == 2:
            completed = False
            name = input("What is your name? ")
            round = 2
            count = 1
            captcha = []    

            export_dir_path = prelude(name)

            '''
            create merge_df csv file
            '''
            merge_csv_name = "df_" + name + ".csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            if os.path.isfile(merge_csv_path) is True:
                print(f"CSV file exist at {merge_csv_path}")
            else:
                # assign header columns
                headerList = ['', 'key', 'press_time', 'release_time']
                
                # open CSV file and assign header
                with open(merge_csv_path, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Merge_DF CSV file will be created: {merge_csv_path}")

            csv_name_original = "original_" + name + ".csv"
            csv_path_original = os.path.join(export_dir_path, csv_name_original)

            csv_name_single = "single_" + name + ".csv"
            csv_path_single = os.path.join(export_dir_path, csv_name_single)

            if os.path.isfile(csv_path_original) is True:
                print(f"CSV file exist at {csv_path_original}")
            else:
                # assign header columns
                headerList = ['Subject', 'Class', 'Sequence']
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
                
                # open CSV file and assign header
                with open(csv_path_original, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"CSV file will be created: {csv_path_original}")

                if os.path.isfile(csv_path_single) is True:
                    print(f"CSV file exist at {csv_path_single}")
                else:
                    # assign header columns
                    headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Class', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
                    
                    # open CSV file and assign header
                    with open(csv_path_single, 'w', newline='') as file:
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                        dw.writeheader()

                    print(f"CSV file will be created: {csv_path_single}")

            with open("captcha/three_fixed.txt", "r") as file:
                three_f = list(map(str, file.read().split()))

            with open("captcha/four_fixed.txt", "r") as file:
                four_f = list(map(str, file.read().split()))

            with open("captcha/five_fixed.txt", "r") as file:
                five_f = list(map(str, file.read().split()))

            with open("captcha/six_fixed.txt", "r") as file:
                six_f = list(map(str, file.read().split()))

            with open("captcha/three_rand.txt", "r") as file:
                three_r = list(map(str, file.read().split()))

            with open("captcha/four_rand.txt", "r") as file:
                four_r = list(map(str, file.read().split()))

            with open("captcha/five_rand.txt", "r") as file:
                five_r = list(map(str, file.read().split()))

            with open("captcha/six_rand.txt", "r") as file:
                six_r = list(map(str, file.read().split()))

            time.sleep(0.1)
            
            for _ in range(0, len(three_f), 2):
                captcha.append(three_f[_] + " " + three_f[_+1])
                captcha.append(four_f[_] + " " + four_f[_+1])
                captcha.append(five_f[_] + " " + five_f[_+1])
                captcha.append(six_f[_] + " " + six_f[_+1])

            for _ in range(round):
                captcha.append(random.choice(three_r) + " " + random.choice(six_r))
                captcha.append(random.choice(four_r) + " " + random.choice(five_r))
                captcha.append(random.choice(five_r) + " " + random.choice(four_r))
                captcha.append(random.choice(six_r) + " " + random.choice(three_r))
            
            maxCount = len(captcha)

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_csv(csv_path_original)
            keyboard.set_csv_single(csv_path_single)
            keyboard.set_export(export_dir_path)
            listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
            listener.start()

            for _ in captcha:
                completed = False
                while completed is False:
                    basePwdInput = input(f"Please type \"{_}\": ")
                    sleep(1)
                    if basePwdInput == _:
                        press_df = keyboard.get_press_df()
                        release_df = keyboard.get_release_df()
                        
                        press_df.reset_index(inplace=True, drop=True)
                        release_df.reset_index(inplace=True, drop=True)
                        press_df.drop(press_df[press_df['key']=='key.enter'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.caps_lock'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift_r'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.enter'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.caps_lock'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift_r'].index, inplace=True)
                        
                        if len(press_df.index.values) == len(_) and len(release_df.index.values) == len(_):
                            print(f"Thank you. {maxCount - count} times left. ")
                            keyboard.export_to_csv_2(_)
                            count = count + 1
                            keyboard.reset()
                            completed = True
                        else:
                            keyboard.reset()
                            print(f"Invalid. Please key in {_} without any backspace or errors. ")
                    else:
                        keyboard.reset()
                        print("Password is incorrect. Please retry. ")

        elif case == 3:
            completed = False
            name = input("What is your name? ")
            round = 10
            count = 1
            captcha = []    

            export_dir_path = prelude(name)
            
            '''
            create merge_df csv file
            '''
            merge_csv_name = "df_rand_" + name + ".csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            if os.path.isfile(merge_csv_path) is True:
                print(f"CSV file exist at {merge_csv_path}")
            else:
                # assign header columns
                headerList = ['', 'key', 'press_time', 'release_time']
                
                # open CSV file and assign header
                with open(merge_csv_path, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Merge_DF CSV file will be created: {merge_csv_path}")

            csv_name_original = "original_rand_" + name + ".csv"
            csv_path_original = os.path.join(export_dir_path, csv_name_original)

            csv_name_single = "single_rand_" + name + ".csv"
            csv_path_single = os.path.join(export_dir_path, csv_name_single)

            if os.path.isfile(csv_path_original) is True:
                print(f"CSV file exist at {csv_path_original}")
            else:
                # assign header columns
                headerList = ['Subject', 'Sequence']
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
                headerList.append(f"T2-NG|S")

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
                headerList.append(f"T2-NG|SD")

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
                
                # open CSV file and assign header
                with open(csv_path_original, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"CSV file will be created: {csv_path_original}")

                if os.path.isfile(csv_path_single) is True:
                    print(f"CSV file exist at {csv_path_single}")
                else:
                    # assign header columns
                    headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
                    
                    # open CSV file and assign header
                    with open(csv_path_single, 'w', newline='') as file:
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                        dw.writeheader()

                    print(f"CSV file will be created: {csv_path_single}")

            with open("captcha/five.txt", "r") as file:
                main_rand_five = list(map(str, file.read().split()))

            with open("captcha/five_let_fixed.txt", "r") as file:
                fixed_five = list(map(str, file.read().split()))

            with open("captcha/five_let_rand.txt", "r") as file:
                random_five = list(map(str, file.read().split()))

            time.sleep(0.1)

            for _ in range(0, 110):
                captcha.append(random.choice(main_rand_five))

            maxCount = len(captcha)

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_csv(csv_path_original)
            keyboard.set_csv_single(csv_path_single)
            keyboard.set_export(export_dir_path)
            listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
            listener.start()

            for _ in captcha:
                completed = False
                while completed is False:
                    basePwdInput = input(f"Please type \"{_}\": ")
                    sleep(1)
                    if basePwdInput == _:
                        press_df = keyboard.get_press_df()
                        release_df = keyboard.get_release_df()
                        
                        press_df.reset_index(inplace=True, drop=True)
                        release_df.reset_index(inplace=True, drop=True)
                        press_df.drop(press_df[press_df['key']=='key.enter'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.caps_lock'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift_r'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.enter'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.caps_lock'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift_r'].index, inplace=True)
                        
                        if len(press_df.index.values) == len(_) and len(release_df.index.values) == len(_):
                            print(f"Thank you. {maxCount - count} times left. ")
                            keyboard.export_to_csv_3(_)
                            count = count + 1
                            keyboard.reset()
                            completed = True
                        else:
                            keyboard.reset()
                            print(f"Invalid. Please key in {_} without any backspace or errors. ")
                    else:
                        keyboard.reset()
                        print("Password is incorrect. Please retry. ")
                        
        elif case == 4:
            completed = False
            name = input("What is your name? ")
            round = 10
            count = 1
            captcha = []    

            export_dir_path = prelude(name)
            
            '''
            create merge_df csv file
            '''
            merge_csv_name = "df_IUDU_" + name + ".csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            if os.path.isfile(merge_csv_path) is True:
                print(f"CSV file exist at {merge_csv_path}")
            else:
                # assign header columns
                headerList = ['', 'key', 'press_time', 'release_time']
                
                # open CSV file and assign header
                with open(merge_csv_path, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Merge_DF CSV file will be created: {merge_csv_path}")

            csv_name_original = "original_IUDU_" + name + ".csv"
            csv_path_original = os.path.join(export_dir_path, csv_name_original)

            csv_name_single = "single_IUDU_" + name + ".csv"
            csv_path_single = os.path.join(export_dir_path, csv_name_single)

            if os.path.isfile(csv_path_original) is True:
                print(f"CSV file exist at {csv_path_original}")
            else:
                # assign header columns
                headerList = ['Subject', 'Sequence']
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
                headerList.append(f"T2-NG|S")

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
                headerList.append(f"T2-NG|SD")

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
                
                # open CSV file and assign header
                with open(csv_path_original, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"CSV file will be created: {csv_path_original}")

                if os.path.isfile(csv_path_single) is True:
                    print(f"CSV file exist at {csv_path_single}")
                else:
                    # assign header columns
                    headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
                    
                    # open CSV file and assign header
                    with open(csv_path_single, 'w', newline='') as file:
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                        dw.writeheader()

                    print(f"CSV file will be created: {csv_path_single}")

            with open("captcha/five.txt", "r") as file:
                main_rand_five = list(map(str, file.read().split()))

            with open("captcha/five_let_fixed.txt", "r") as file:
                fixed_five = list(map(str, file.read().split()))

            with open("captcha/five_let_rand.txt", "r") as file:
                random_five = list(map(str, file.read().split()))

            time.sleep(0.1)

            for _ in range(0, len(fixed_five)):
                captcha.append(fixed_five[_])

            for _ in range(round):
                captcha.append(random.choice(random_five))

            maxCount = len(captcha)

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_csv(csv_path_original)
            keyboard.set_csv_single(csv_path_single)
            keyboard.set_export(export_dir_path)
            listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
            listener.start()

            for _ in captcha:
                completed = False
                while completed is False:
                    basePwdInput = input(f"Please type \"{_}\": ")
                    sleep(1)
                    if basePwdInput == _:
                        press_df = keyboard.get_press_df()
                        release_df = keyboard.get_release_df()
                        
                        press_df.reset_index(inplace=True, drop=True)
                        release_df.reset_index(inplace=True, drop=True)
                        press_df.drop(press_df[press_df['key']=='key.enter'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.caps_lock'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift_r'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.enter'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.caps_lock'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift_r'].index, inplace=True)
                        
                        if len(press_df.index.values) == len(_) and len(release_df.index.values) == len(_):
                            print(f"Thank you. {maxCount - count} times left. ")
                            keyboard.export_to_csv_3(_)
                            count = count + 1
                            keyboard.reset()
                            completed = True
                        else:
                            keyboard.reset()
                            print(f"Invalid. Please key in {_} without any backspace or errors. ")
                    else:
                        keyboard.reset()
                        print("Password is incorrect. Please retry. ")

        elif case == 5:
            completed = False
            name = input("What is your name? ")
            passwordFlag = False
            while passwordFlag is False:
                password = input("What is your desired password? 8 alphanumeric numbers only and avoid common password: ")
                if len(password) == 8:
                    passwordFlag = True

            maxCount = 105
            count = 1

            export_dir_path = prelude(name)
            maxPwdLen = len(password)
            
            '''
            create merge_df csv file
            '''
            merge_csv_name = "df_own_" + name + ".csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            csv_name_full = "full_own_" + name + ".csv"
            csv_path_full = os.path.join(export_dir_path, csv_name_full)

            csv_name_nostat = "nostat_own_" + name + ".csv"
            csv_path_nostat = os.path.join(export_dir_path, csv_name_nostat)

            csv_name_bare = "bare_own_" + name + ".csv"
            csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            csv_name_single = "single_own_" + name + ".csv"
            csv_path_single = os.path.join(export_dir_path, csv_name_single)

            if os.path.isfile(merge_csv_path) is True:
                print(f"CSV file exist at {merge_csv_path}")
            else:
                # assign header columns
                headerList = ['', 'key', 'press_time', 'release_time']
                
                # open CSV file and assign header
                with open(merge_csv_path, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Merge_DF CSV file will be created: {merge_csv_path}")

            if os.path.isfile(csv_path_full) is True:
                print(f"CSV file exist at {csv_path_full}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
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
                headerList.append(f"T2-NG|SD")

                for _ in range(maxPwdLen-2):
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

                for _ in range(maxPwdLen-3):
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

                for _ in range(maxPwdLen-4):
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

                for _ in range(maxPwdLen-5):
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

                for _ in range(maxPwdLen-6):
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

                for _ in range(maxPwdLen-7):
                    headerList.append(f"T8-I|{_}+{_+7}")
                    headerList.append(f"T8-PF|{_}+{_+7}")
                    headerList.append(f"T8-RF|{_}+{_+7}")
                    headerList.append(f"T8-NG|{_}+{_+7}")
                
                # open CSV file and assign header
                with open(csv_path_full, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Full CSV file will be created: {csv_path_full}")

                ###########################################

            if os.path.isfile(csv_path_nostat) is True:
                print(f"CSV file exist at {csv_path_nostat}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
                    headerList.append(f"T2-I|{_}+{_+1}")
                    headerList.append(f"T2-PF|{_}+{_+1}")
                    headerList.append(f"T2-RF|{_}+{_+1}")
                    headerList.append(f"T2-NG|{_}+{_+1}")
                    headerList.append(f"T2-D|{_+1}")

                for _ in range(maxPwdLen-2):
                    headerList.append(f"T3-I|{_}+{_+2}")
                    headerList.append(f"T3-PF|{_}+{_+2}")
                    headerList.append(f"T3-RF|{_}+{_+2}")
                    headerList.append(f"T3-NG|{_}+{_+2}")

                for _ in range(maxPwdLen-3):
                    headerList.append(f"T4-I|{_}+{_+3}")
                    headerList.append(f"T4-PF|{_}+{_+3}")
                    headerList.append(f"T4-RF|{_}+{_+3}")
                    headerList.append(f"T4-NG|{_}+{_+3}")

                for _ in range(maxPwdLen-4):
                    headerList.append(f"T5-I|{_}+{_+4}")
                    headerList.append(f"T5-PF|{_}+{_+4}")
                    headerList.append(f"T5-RF|{_}+{_+4}")
                    headerList.append(f"T5-NG|{_}+{_+4}")

                for _ in range(maxPwdLen-5):
                    headerList.append(f"T6-I|{_}+{_+5}")
                    headerList.append(f"T6-PF|{_}+{_+5}")
                    headerList.append(f"T6-RF|{_}+{_+5}")
                    headerList.append(f"T6-NG|{_}+{_+5}")

                for _ in range(maxPwdLen-6):
                    headerList.append(f"T7-I|{_}+{_+6}")
                    headerList.append(f"T7-PF|{_}+{_+6}")
                    headerList.append(f"T7-RF|{_}+{_+6}")
                    headerList.append(f"T7-NG|{_}+{_+6}")

                for _ in range(maxPwdLen-7):
                    headerList.append(f"T8-I|{_}+{_+7}")
                    headerList.append(f"T8-PF|{_}+{_+7}")
                    headerList.append(f"T8-RF|{_}+{_+7}")
                    headerList.append(f"T8-NG|{_}+{_+7}")
                
                # open CSV file and assign header
                with open(csv_path_nostat, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Nostat CSV file will be created: {csv_path_nostat}")

                ###########################################

            if os.path.isfile(csv_path_bare) is True:
                print(f"CSV file exist at {csv_path_bare}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
                    headerList.append(f"T2-I|{_}+{_+1}")
                    headerList.append(f"T2-PF|{_}+{_+1}")
                    headerList.append(f"T2-RF|{_}+{_+1}")
                    headerList.append(f"T2-NG|{_}+{_+1}")
                    headerList.append(f"T2-D|{_+1}")
                
                # open CSV file and assign header
                with open(csv_path_bare, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Bare CSV file will be created: {csv_path_bare}")

                ###########################################

                if os.path.isfile(csv_path_single) is True:
                    print(f"CSV file exist at {csv_path_single}")
                else:
                    # assign header columns
                    headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
                    
                    # open CSV file and assign header
                    with open(csv_path_single, 'w', newline='') as file:
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                        dw.writeheader()

                    print(f"Single CSV file will be created: {csv_path_single}")

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_merge_csv(merge_csv_path)
            keyboard.set_csv(csv_path_full)
            keyboard.set_csv_nostat(csv_path_nostat)
            keyboard.set_csv_bare(csv_path_bare)
            keyboard.set_csv_single(csv_path_single)
            keyboard.set_export(export_dir_path)
            listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
            listener.start()

            invalidCount = 0
            incorrectCount = 0

            for _ in range(0, maxCount):
                completed = False
                while completed is False:
                    basePwdInput = input(f"Please type \"{password}\": ")
                    sleep(1)
                    if basePwdInput == password:
                        press_df = keyboard.get_press_df()
                        release_df = keyboard.get_release_df()
                        
                        press_df.reset_index(inplace=True, drop=True)
                        release_df.reset_index(inplace=True, drop=True)
                        press_df.drop(press_df[press_df['key']=='key.enter'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.caps_lock'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift_r'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.enter'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.caps_lock'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift_r'].index, inplace=True)
                        
                        if len(press_df.index.values) == len(password) and len(release_df.index.values) == len(password):
                            print(f"Thank you. {maxCount - count} times left. ")
                            keyboard.export_to_csv_4(password)
                            count = count + 1
                            keyboard.reset()
                            completed = True
                        else:
                            keyboard.reset()
                            print(f"Invalid. Please key in {password} without any backspace or errors. ")
                            invalidCount = invalidCount + 1
                    else:
                        keyboard.reset()
                        print("Password is incorrect. Please retry. ")
                        incorrectCount = incorrectCount + 1

            error_name = "error_own_" + name + ".txt"
            error_path = os.path.join(export_dir_path, error_name) 

            if os.path.isfile(error_path) is True:
                print(f"Error file exist at {error_path}")
            else:
                # open CSV file and assign header
                with open(error_path, 'w', newline='') as file:
                    file.write(f"Incorrect Count: {invalidCount}\n")
                    file.write(f"Invalid Count: {incorrectCount}\n")
                    totalCount = invalidCount + incorrectCount
                    file.write(f"Total Wrong Count: {totalCount}\n")
                    accuracy = (105 / (totalCount + 105)) * 100
                    file.write(f"Accuracy: {accuracy}\n")

                print(f"Error file will be created: {error_path}")

        elif case == 6:
            completed = False
            name = input("What is your name? ")
            password = "dEcisi0n"

            maxCount = 105
            count = 1

            export_dir_path = prelude(name)
            maxPwdLen = len(password)
            
            '''
            create merge_df csv file
            '''
            merge_csv_name = "df_same_" + name + ".csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            csv_name_full = "full_same_" + name + ".csv"
            csv_path_full = os.path.join(export_dir_path, csv_name_full)

            csv_name_nostat = "nostat_same_" + name + ".csv"
            csv_path_nostat = os.path.join(export_dir_path, csv_name_nostat)

            csv_name_bare = "bare_same_" + name + ".csv"
            csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            csv_name_single = "single_same_" + name + ".csv"
            csv_path_single = os.path.join(export_dir_path, csv_name_single)

            if os.path.isfile(merge_csv_path) is True:
                print(f"CSV file exist at {merge_csv_path}")
            else:
                # assign header columns
                headerList = ['', 'key', 'press_time', 'release_time']
                
                # open CSV file and assign header
                with open(merge_csv_path, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Merge_DF CSV file will be created: {merge_csv_path}")

            if os.path.isfile(csv_path_full) is True:
                print(f"CSV file exist at {csv_path_full}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
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
                headerList.append(f"T2-NG|SD")

                for _ in range(maxPwdLen-2):
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

                for _ in range(maxPwdLen-3):
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

                for _ in range(maxPwdLen-4):
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

                for _ in range(maxPwdLen-5):
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

                for _ in range(maxPwdLen-6):
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

                for _ in range(maxPwdLen-7):
                    headerList.append(f"T8-I|{_}+{_+7}")
                    headerList.append(f"T8-PF|{_}+{_+7}")
                    headerList.append(f"T8-RF|{_}+{_+7}")
                    headerList.append(f"T8-NG|{_}+{_+7}")
                
                # open CSV file and assign header
                with open(csv_path_full, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Full CSV file will be created: {csv_path_full}")

                ###########################################

            if os.path.isfile(csv_path_nostat) is True:
                print(f"CSV file exist at {csv_path_nostat}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
                    headerList.append(f"T2-I|{_}+{_+1}")
                    headerList.append(f"T2-PF|{_}+{_+1}")
                    headerList.append(f"T2-RF|{_}+{_+1}")
                    headerList.append(f"T2-NG|{_}+{_+1}")
                    headerList.append(f"T2-D|{_+1}")

                for _ in range(maxPwdLen-2):
                    headerList.append(f"T3-I|{_}+{_+2}")
                    headerList.append(f"T3-PF|{_}+{_+2}")
                    headerList.append(f"T3-RF|{_}+{_+2}")
                    headerList.append(f"T3-NG|{_}+{_+2}")

                for _ in range(maxPwdLen-3):
                    headerList.append(f"T4-I|{_}+{_+3}")
                    headerList.append(f"T4-PF|{_}+{_+3}")
                    headerList.append(f"T4-RF|{_}+{_+3}")
                    headerList.append(f"T4-NG|{_}+{_+3}")

                for _ in range(maxPwdLen-4):
                    headerList.append(f"T5-I|{_}+{_+4}")
                    headerList.append(f"T5-PF|{_}+{_+4}")
                    headerList.append(f"T5-RF|{_}+{_+4}")
                    headerList.append(f"T5-NG|{_}+{_+4}")

                for _ in range(maxPwdLen-5):
                    headerList.append(f"T6-I|{_}+{_+5}")
                    headerList.append(f"T6-PF|{_}+{_+5}")
                    headerList.append(f"T6-RF|{_}+{_+5}")
                    headerList.append(f"T6-NG|{_}+{_+5}")

                for _ in range(maxPwdLen-6):
                    headerList.append(f"T7-I|{_}+{_+6}")
                    headerList.append(f"T7-PF|{_}+{_+6}")
                    headerList.append(f"T7-RF|{_}+{_+6}")
                    headerList.append(f"T7-NG|{_}+{_+6}")

                for _ in range(maxPwdLen-7):
                    headerList.append(f"T8-I|{_}+{_+7}")
                    headerList.append(f"T8-PF|{_}+{_+7}")
                    headerList.append(f"T8-RF|{_}+{_+7}")
                    headerList.append(f"T8-NG|{_}+{_+7}")
                
                # open CSV file and assign header
                with open(csv_path_nostat, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Nostat CSV file will be created: {csv_path_nostat}")

                ###########################################

            if os.path.isfile(csv_path_bare) is True:
                print(f"CSV file exist at {csv_path_bare}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
                    headerList.append(f"T2-I|{_}+{_+1}")
                    headerList.append(f"T2-PF|{_}+{_+1}")
                    headerList.append(f"T2-RF|{_}+{_+1}")
                    headerList.append(f"T2-NG|{_}+{_+1}")
                    headerList.append(f"T2-D|{_+1}")
                
                # open CSV file and assign header
                with open(csv_path_bare, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Bare CSV file will be created: {csv_path_bare}")

                ###########################################

                if os.path.isfile(csv_path_single) is True:
                    print(f"CSV file exist at {csv_path_single}")
                else:
                    # assign header columns
                    headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
                    
                    # open CSV file and assign header
                    with open(csv_path_single, 'w', newline='') as file:
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                        dw.writeheader()

                    print(f"Single CSV file will be created: {csv_path_single}")

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_merge_csv(merge_csv_path)
            keyboard.set_csv(csv_path_full)
            keyboard.set_csv_nostat(csv_path_nostat)
            keyboard.set_csv_bare(csv_path_bare)
            keyboard.set_csv_single(csv_path_single)
            keyboard.set_export(export_dir_path)
            listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
            listener.start()

            invalidCount = 0
            incorrectCount = 0

            for _ in range(0, maxCount):
                completed = False
                while completed is False:
                    basePwdInput = input(f"Please type \"{password}\": ")
                    sleep(1)
                    if basePwdInput == password:
                        press_df = keyboard.get_press_df()
                        release_df = keyboard.get_release_df()
                        
                        press_df.reset_index(inplace=True, drop=True)
                        release_df.reset_index(inplace=True, drop=True)
                        press_df.drop(press_df[press_df['key']=='key.enter'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.caps_lock'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift'].index, inplace=True)
                        press_df.drop(press_df[press_df['key']=='key.shift_r'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.enter'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.caps_lock'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift'].index, inplace=True)
                        release_df.drop(release_df[release_df['key']=='key.shift_r'].index, inplace=True)
                        
                        if len(press_df.index.values) == len(password) and len(release_df.index.values) == len(password):
                            print(f"Thank you. {maxCount - count} times left. ")
                            keyboard.export_to_csv_4(password)
                            count = count + 1
                            keyboard.reset()
                            completed = True
                        else:
                            keyboard.reset()
                            print(f"Invalid. Please key in {password} without any backspace or errors. ")
                            invalidCount = invalidCount + 1
                    else:
                        keyboard.reset()
                        print("Password is incorrect. Please retry. ")
                        incorrectCount = incorrectCount + 1
            
            error_name = "error_same_" + name + ".txt"
            error_path = os.path.join(export_dir_path, error_name) 

            if os.path.isfile(error_path) is True:
                print(f"Error file exist at {error_path}")
            else:
                # open CSV file and assign header
                with open(error_path, 'w', newline='') as file:
                    file.write(f"Incorrect Count: {invalidCount}\n")
                    file.write(f"Invalid Count: {incorrectCount}\n")
                    totalCount = invalidCount + incorrectCount
                    file.write(f"Total Wrong Count: {totalCount}\n")
                    accuracy = (105 / (totalCount + 105)) * 100
                    file.write(f"Accuracy: {accuracy}\n")

                print(f"Error file will be created: {error_path}")

        elif case == 7:
            completed = False
            name = input("What is your name? ")

            maxCount = 60
            count = 1

            export_dir_path = prelude(name)
            maxPwdLen = 8
            '''
            create merge_df csv file
            '''
            merge_csv_name = "df_combi_" + name + ".csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            csv_name_original = "original_combi_" + name + ".csv"
            csv_path_original = os.path.join(export_dir_path, csv_name_original)

            csv_name_nostat = "nostat_combi_" + name + ".csv"
            csv_path_nostat = os.path.join(export_dir_path, csv_name_nostat)

            csv_name_bare = "bare_combi_" + name + ".csv"
            csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            csv_name_single = "single_combi_" + name + ".csv"
            csv_path_single = os.path.join(export_dir_path, csv_name_single)

            if os.path.isfile(merge_csv_path) is True:
                print(f"CSV file exist at {merge_csv_path}")
            else:
                # assign header columns
                headerList = ['', 'key', 'press_time', 'release_time']
                
                # open CSV file and assign header
                with open(merge_csv_path, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Merge_DF CSV file will be created: {merge_csv_path}")

            if os.path.isfile(csv_path_original) is True:
                print(f"CSV file exist at {csv_path_original}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
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
                headerList.append(f"T2-NG|SD")

                for _ in range(maxPwdLen-2):
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

                for _ in range(maxPwdLen-3):
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

                for _ in range(maxPwdLen-4):
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

                for _ in range(maxPwdLen-5):
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

                for _ in range(maxPwdLen-6):
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

                for _ in range(maxPwdLen-7):
                    headerList.append(f"T8-I|{_}+{_+7}")
                    headerList.append(f"T8-PF|{_}+{_+7}")
                    headerList.append(f"T8-RF|{_}+{_+7}")
                    headerList.append(f"T8-NG|{_}+{_+7}")
                
                # open CSV file and assign header
                with open(csv_path_original, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Full CSV file will be created: {csv_path_original}")

                ###########################################

            if os.path.isfile(csv_path_nostat) is True:
                print(f"CSV file exist at {csv_path_nostat}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
                    headerList.append(f"T2-I|{_}+{_+1}")
                    headerList.append(f"T2-PF|{_}+{_+1}")
                    headerList.append(f"T2-RF|{_}+{_+1}")
                    headerList.append(f"T2-NG|{_}+{_+1}")
                    headerList.append(f"T2-D|{_+1}")

                for _ in range(maxPwdLen-2):
                    headerList.append(f"T3-I|{_}+{_+2}")
                    headerList.append(f"T3-PF|{_}+{_+2}")
                    headerList.append(f"T3-RF|{_}+{_+2}")
                    headerList.append(f"T3-NG|{_}+{_+2}")

                for _ in range(maxPwdLen-3):
                    headerList.append(f"T4-I|{_}+{_+3}")
                    headerList.append(f"T4-PF|{_}+{_+3}")
                    headerList.append(f"T4-RF|{_}+{_+3}")
                    headerList.append(f"T4-NG|{_}+{_+3}")

                for _ in range(maxPwdLen-4):
                    headerList.append(f"T5-I|{_}+{_+4}")
                    headerList.append(f"T5-PF|{_}+{_+4}")
                    headerList.append(f"T5-RF|{_}+{_+4}")
                    headerList.append(f"T5-NG|{_}+{_+4}")

                for _ in range(maxPwdLen-5):
                    headerList.append(f"T6-I|{_}+{_+5}")
                    headerList.append(f"T6-PF|{_}+{_+5}")
                    headerList.append(f"T6-RF|{_}+{_+5}")
                    headerList.append(f"T6-NG|{_}+{_+5}")

                for _ in range(maxPwdLen-6):
                    headerList.append(f"T7-I|{_}+{_+6}")
                    headerList.append(f"T7-PF|{_}+{_+6}")
                    headerList.append(f"T7-RF|{_}+{_+6}")
                    headerList.append(f"T7-NG|{_}+{_+6}")

                for _ in range(maxPwdLen-7):
                    headerList.append(f"T8-I|{_}+{_+7}")
                    headerList.append(f"T8-PF|{_}+{_+7}")
                    headerList.append(f"T8-RF|{_}+{_+7}")
                    headerList.append(f"T8-NG|{_}+{_+7}")
                
                # open CSV file and assign header
                with open(csv_path_nostat, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Nostat CSV file will be created: {csv_path_nostat}")

                ###########################################

            if os.path.isfile(csv_path_bare) is True:
                print(f"CSV file exist at {csv_path_bare}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"T2-D|0")
                for _ in range(maxPwdLen-1):
                    headerList.append(f"T2-I|{_}+{_+1}")
                    headerList.append(f"T2-PF|{_}+{_+1}")
                    headerList.append(f"T2-RF|{_}+{_+1}")
                    headerList.append(f"T2-NG|{_}+{_+1}")
                    headerList.append(f"T2-D|{_+1}")
                
                # open CSV file and assign header
                with open(csv_path_bare, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Bare CSV file will be created: {csv_path_bare}")

                ###########################################

                if os.path.isfile(csv_path_single) is True:
                    print(f"CSV file exist at {csv_path_single}")
                else:
                    # assign header columns
                    headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
                    
                    # open CSV file and assign header
                    with open(csv_path_single, 'w', newline='') as file:
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                        dw.writeheader()

                    print(f"Single CSV file will be created: {csv_path_single}")

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_merge_csv(merge_csv_path)
            keyboard.set_csv(csv_path_original)
            keyboard.set_csv_nostat(csv_path_nostat)
            keyboard.set_csv_bare(csv_path_bare)
            keyboard.set_csv_single(csv_path_single)
            keyboard.set_export(export_dir_path)
            listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
            listener.start()

            invalidCount = 0
            incorrectCount = 0

            # andy, azfar, bryce, chris, cy, gerald, ken, qk, sz, vale, ye, ys
            password_list = ["C05mical", "play4pay", "4cHkh1dL", "a1rcr2ft", "wang1234", "Andy1234", "Kennth12", "Andyb1tc", "andy1234", "memories", "HiAndy12", "tw1nkle6"]

            for password in password_list:
                for x in range(0, 1):
                    completed = False
                    while completed is False:
                        basePwdInput = input(f"Please type \"{password}\": ")
                        sleep(1)
                        if basePwdInput == password:
                            press_df = keyboard.get_press_df()
                            release_df = keyboard.get_release_df()
                            
                            press_df.reset_index(inplace=True, drop=True)
                            release_df.reset_index(inplace=True, drop=True)
                            press_df.drop(press_df[press_df['key']=='key.enter'].index, inplace=True)
                            press_df.drop(press_df[press_df['key']=='key.caps_lock'].index, inplace=True)
                            press_df.drop(press_df[press_df['key']=='key.shift'].index, inplace=True)
                            press_df.drop(press_df[press_df['key']=='key.shift_r'].index, inplace=True)
                            release_df.drop(release_df[release_df['key']=='key.enter'].index, inplace=True)
                            release_df.drop(release_df[release_df['key']=='key.caps_lock'].index, inplace=True)
                            release_df.drop(release_df[release_df['key']=='key.shift'].index, inplace=True)
                            release_df.drop(release_df[release_df['key']=='key.shift_r'].index, inplace=True)
                            
                            if len(press_df.index.values) == len(password) and len(release_df.index.values) == len(password):
                                print(f"Thank you. {maxCount - count} times left. ")
                                keyboard.export_to_csv_4(password)
                                count = count + 1
                                keyboard.reset()
                                completed = True
                            else:
                                keyboard.reset()
                                print(f"Invalid. Please key in {password} without any backspace or errors. ")
                                invalidCount = invalidCount + 1
                        else:
                            keyboard.reset()
                            print("Password is incorrect. Please retry. ")
                            incorrectCount = incorrectCount + 1

            error_name = "error_combi_" + name + ".txt"
            error_path = os.path.join(export_dir_path, error_name) 

            if os.path.isfile(error_path) is True:
                print(f"Error file exist at {error_path}")
            else:
                # open CSV file and assign header
                with open(error_path, 'w', newline='') as file:
                    file.write(f"Incorrect Count: {invalidCount}\n")
                    file.write(f"Invalid Count: {incorrectCount}\n")
                    totalCount = invalidCount + incorrectCount
                    file.write(f"Total Wrong Count: {totalCount}\n")
                    accuracy = (60 / (totalCount + 60)) * 100
                    file.write(f"Accuracy: {accuracy}\n")

                print(f"Error file will be created: {error_path}")
        else:
            print("Please select the appropriate case number.")

def prelude(name):
    export_dir_name = "export"
    '''
    obtain information about system
    '''
    current_path = os.getcwd()

    print(f"OS Name: {os.name}")
    print(f"Operating System: {platform.system()}")
    print(f"Release Version: {platform.release()}")
    print(f"Current Path: {os.getcwd()}")

    try:
        print(f"Display found as {os.environ['DISPLAY']}")
    except:
        os.environ['DISPLAY'] = ':0'
        print("Display NOT FOUND and has been set to zero")
    finally:
        print("...Program started.")

    '''
    export directory
    '''
    export_dir_path = os.path.join(current_path, export_dir_name)

    if os.path.isdir(export_dir_path) is True:
        print(f"Export directory exists at: {export_dir_path}")
        pass
    else:
        try:
            os.mkdir(export_dir_path, 666)
            print(f"Export directory have been created at: {export_dir_path}")
        except:
            print("Error: Export Directory not created")

    '''
    generate info file
    '''
    info_name = "info_" + name + ".txt"
    info_path = os.path.join(export_dir_path, info_name) 

    if os.path.isfile(info_path) is True:
        print(f"Info file exist at {info_path}")
    else:
        # open CSV file and assign header
        with open(info_path, 'w', newline='') as file:
            file.write(f"Name: {name}\n")
            file.write(f"OS: {os.name}\n")
            file.write(f"Platform system: {platform.system()}\n")
            file.write(f"Platform release: {platform.release()}\n")

        print(f"Info file will be created: {info_path}")

    return export_dir_path

## split up into prelude of info, two different excel/for loop after that [set1/2/3 - set4].

if __name__ == "__main__":
    main()

    # generate ui file
    # pyuic5 mainwindow.ui -o mainwindowui.py
    # generate resource file
    # pyrcc5 resources.qrc -o resources.py
    # create app
    # pyinstaller -F -w main.py
    # pyinstaller --onefile main.py
    # pyinstaller main.py --onefile --hidden-import=pynput.keyboard._xorg -n combi
