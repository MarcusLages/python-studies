#! python3
"""
mclip.py: Multi-clipboard program to practice python scripting.

:author: Marcus V S Lages
"""

import os, sys, pyperclip, csv

CSV_FILE = "prompts.csv"
MIN_ARGS = 2

def main():
    """
    Main function that runs the script. Checks for input validation
    and calls the right action.
    """
    args = sys.argv
    validate_arg_size(args)

    prompts = get_msg_prompts()
    message = args[1]
    is_in_terminal = sys.stdout.isatty()

    if message in prompts:
        prompt = prompts[message]
        pyperclip.copy(prompt)

        if is_in_terminal:
            print(f"{message.title()} copied!\nMessage: {prompt}")

    elif is_in_terminal:
        print("No messages recorded for this input.")

def validate_arg_size(args):
    """
    Validates the size of the arguments list so it has the min amount
    of arguments to run the script.

    CLOSES THE PROGRAM IF THERE'S NOT ENOUGH ARGUMENTS

    :param args:    terminal arguments list
    """
    if len(args) < MIN_ARGS:
        print("Not enough arguments.")
        sys.exit()

def get_data_from_csv(csv_filename):
    """
    Reads data from a .csv file and returns as a list of the rows with
    each row being an inner list.

    :param csv_filename: Name of the .csv file and path relative to the
                         python file
    :return:             .csv data as a list of rows
    """
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(cur_dir, CSV_FILE)

    with open(csv_path) as fp:
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