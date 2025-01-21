#! python3
"""
mclip.py: Multi-clipboard program to practice python scripting.

:author: Marcus V S Lages
"""

import sys, pyperclip, csv

CSV_FILE = "example.csv"

def main():
    args = sys.argv

    if len(args) < 2:
        print("Not enough arguments.")
        sys.exit()

    prompts = get_msg_prompts()
    message = args[1]
    is_in_terminal = sys.stdin.isatty()

    if message in prompts:
        prompt = prompts[message]
        pyperclip.copy(prompt)

        if is_in_terminal:
            print(f"{message.title()} copied!\nMessage: {prompt}")

    elif is_in_terminal:
        print("No messages recorded for this input.")

def get_data_from_csv(csv_filename):
    with open(csv_filename) as fp:
        csv_reader = csv.reader(fp, delimiter=":", quotechar='"')
        data_read = [row for row in csv_reader]

    return data_read

def msg_list_to_prompts(message_list):
    """
    Generates a dictionary from a list of messages, which
    the first column of the list corresponds to the message key
    and the second column to the prompt value.

    :param message_list: 2D list with the format [message][prompt]
    :return: a dictionary which can use the message to find the prompt
    """
    if not message_list:
        return None

    prompts = {}
    for key, value in message_list:
        prompts[key] = value

    return prompts

def get_msg_prompts():
    """
    Gets all the message prompts from a .csv file as a dictionary.
    You can access the prompts using the message label as a key.
    :return:
    """
    msg_list = get_data_from_csv(CSV_FILE)
    return msg_list_to_prompts(msg_list)


if __name__ == "__main__":
    main()