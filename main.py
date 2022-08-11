#   Created: August 5th, 2022
#   Author: Mckenzie Turner
#   Name: Midas.Investments Report Scraper (MIRS)

import csv
import menu3

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
keys = ["REWARD", "REWARD_BOOST", "SWAP"]
total_amount = []


def data_scrape(month, key):
    with open('report.csv', 'r') as csv_f:
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

                if month in data_date:
                    if data_reward_type == key:
                        print(data_date + ' ' + data_reward_amount + ' ' + data_reward_coin)
                        total_amount.append(float(data_reward_amount))

    print(f"\nTotal = {sum(total_amount)}" + f" {key}")


core_menu = menu3.Menu(True)
menu_initialize = core_menu.menu("Please select a month to begin: ", months, "Press, 'q' to quit now: ")
reader_menu_ini = core_menu.menu("Please select a category: ", keys, "Press, 'q' to quit now: ")
data_scrape(months[menu_initialize - 1], keys[reader_menu_ini - 1])
