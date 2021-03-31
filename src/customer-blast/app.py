"""
Use Python3 app.py
# TODO: Account for non iMessages (text)
"""

import os
import sys
import csv
import json


def get_todays_message():
    """ Pull message logs """
    with open('../data/message_logs.json', 'r') as message_logs:
        message_logs = json.load(message_logs)
        date = max(message_logs.keys())
        todays_message = message_logs[date]
        print(f'MESSAGE: {todays_message}')

    return todays_message


def get_contact_data(environment):
    """ convert CSV to DICT """

    if environment == 'PROD':
        with open('../data/contact_list.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            personas = []
            for row in reader:
                personas.append(row)

    else:
        personas = [
            {"Active": "Y", "Nickname": "Vini", "Phone": "17607990511"},
            {"Active": "Y", "Nickname": "Beth", "Phone": "17609025715"}
        ]

    return personas


def send_messages(environment):
    """ Send message using contact list"""
    todays_message = get_todays_message()
    contact_data = get_contact_data(environment)

    for contact in contact_data:
        name = contact['Nickname']
        number = contact['Phone']
        active = contact['Active']

        if active == 'Y':
            print('Sending message to {} on number {}'.format(name, number))
            message = f'Hey {name}, {todays_message}'
            script = 'send-message.applescript'
            command = f'osascript scripts/{script} {number} "{message}"'
            os.system(command)

    return True


if __name__ == "__main__":
    # Get arguments from script
    environment = sys.argv[1]
    send_messages(environment)
