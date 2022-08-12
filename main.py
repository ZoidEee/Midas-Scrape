#   Created: August 5th, 2022
#   Author: Mckenzie Turner
#   Name: Midas.Investments Report Scraper (MIRS)

import csv
import os.path

import menu3

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
keys = ["REWARD", "REWARD_BOOST", "SWAP", "DEPOSIT"]
total_amount = []


def start_up():
    desktop_directory = os.path.expanduser('~/Desktop/M.I.R.S')
    directory = os.path.exists(desktop_directory)
    file_count = len(os.listdir(desktop_directory))
    files = []

    try:
        if not directory:
            os.makedirs(desktop_directory)
            print(f"Please place the '.csv' withing {desktop_directory}")
        else:
            if file_count == 0:
                print(f"Please place the '.csv' withing {desktop_directory}\nRestart to begin")
                return
            else:
                for file in os.listdir(desktop_directory):
                    files.append(desktop_directory + '/' + file)

    except Exception as error:
        print(error)

    menu(files)


def menu(files):
    core = menu3.Menu(True)

    f_menu = core.menu("Please select a file to begin:\n", files, "\nPress, 'q' to quit now:")
    m_menu = core.menu("Please select a month to begin:\n", months, "\nPress, 'q' to quit now:")
    k_menu = core.menu("Please select a category:\n", keys, "\nPress, 'q' to quit now:")
    data_scrape(files[f_menu - 1], months[m_menu - 1], keys[k_menu - 1])


def data_scrape(file, month, key):
    with open(file, 'r') as csv_f:
        reader = csv.reader(csv_f, delimiter="\t")

        for line in enumerate(reader):
            line_number, line_date = line

            for data in iter(line_date):
                split_data = data.replace('"', '').split(',')
                data_date = split_data[0]
                data_reward_type = split_data[1]
                data_reward_amount = split_data[2]
                data_final_amount = split_data[3]
                data_reward_coin = split_data[4]

                if month in data_date and key == data_reward_type:
                    print(data_date + ' ' + data_reward_amount + ' ' + data_reward_coin)
                    total_amount.append(float(data_reward_amount))

    print(f"\nTotal = {sum(total_amount)}" + f" {key}")


start_up()
core_menu = menu3.Menu(True)
