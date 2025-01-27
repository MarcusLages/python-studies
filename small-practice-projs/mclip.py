#! python3
"""
mclip.py: Multi-clipboard program to practice python scripting.

:author: Marcus V S Lages
"""

import os, sys, pyperclip, csv, argparse

MCLIP_VERSION = "0.8-alpha"
CSV_FILE = "prompts.csv"

def main():
    """
    Main function that runs the script. Checks for input validation
    and calls the right action.
    """
    args = parse_cmd_args()
    is_in_terminal = sys.stdout.isatty()

    if args.list and is_in_terminal:
        display_msg_list()
        return

    if args.add:
        message = " ".join(args.message)
        new_entry = (args.keyword, message)
        add_to_msg_list(new_entry)
        return

    get_msg_to_clipboard(args.keyword)

def parse_cmd_args():
    """
    Parses command line arguments into an object with the following
    Namespace with following attributes:\n
        list:       True if user would like to list all possible keywords
                    and messages
        add:        True if user would like to add a message to mclip\n
        keyword:    keyword to find or add a message on/to mclip\n
        message: full message for adding a message to mclip
    :return: parsed arguments as a Namespace object
    """
    parser = argparse.ArgumentParser(
        description="Multi-clipboard program used to assign " \
                    "shortcuts to add phrases to the clipboard " \
                    "through just typing a keyword"
    )
    parser.add_argument("-v", "--version",
                        action="version",
                        version=f"%(prog)s {MCLIP_VERSION}")
    parser.add_argument("-l", "--list",
                        action="store_true",
                        help="displays a list with all the available "
                             "keywords and messages")
    parser.add_argument("-a", "--add",
                        action="store_true",
                        help="adds a keyword-message to the available "
                             "list. Uses [keyword] and [message]")
    parser.add_argument("keyword",
                        nargs="?",
                        help="used to retrieve a message or add a "
                             "message with [-a]/[--a]")
    parser.add_argument("message",
                        nargs="*",
                        help="used with [-a][--a] to add a "
                             "keyword-message to the list of available "
                             " messages")
    return parser.parse_args()

def display_msg_list():
    """
    Lists/displays all combinations of keyword and messages from the
    stored .csv file.
    """
    prompts = get_msg_prompts()

    print("Keyword\t\t| Message\n"
          "-------------------------------")
    for keyword, message in prompts.items():
        print(f"{keyword}\t\t| {message}")

def add_to_msg_list(new_entry):
    """
    Adds a new entry of keyword-message to the list.

    :param new_entry: tuple (or list) with (keyword, list)
    """
    csv_path = get_csv_path(CSV_FILE)
    is_in_terminal = sys.stdout.isatty()

    with open(csv_path, mode="a", newline="") as file:
        file_writer = csv.writer(file, delimiter=":")
        file_writer.writerow(new_entry)

    if is_in_terminal:
        keyword, message = new_entry
        print(f"{keyword.title()} written!\n"
              f"Message: {message}")

def get_msg_to_clipboard(keyword):
    """
    Gets the message correspondent to the keyword and adds it to
    the clipboard.

    :param keyword: used to access the message
    """
    prompts = get_msg_prompts()
    is_in_terminal = sys.stdout.isatty()

    if keyword in prompts:
        prompt = prompts[keyword]
        pyperclip.copy(prompt)

        if is_in_terminal:
            print(f"{keyword.title()} copied!\n"
                  f"Message: {prompt}")

    elif is_in_terminal:
        print("No messages recorded for this input.")

def get_data_from_csv(csv_path):
    """
    Reads data from a .csv file and returns as a list of the rows with
    each row being an inner list.

    :param csv_path:    Pathname of the .csv file
    :precondition:      .csv file must be separated by colon (:)
    :precondition:      Pathname relative to the python file or
                        absolute path
    :return: .csv data as a list of rows
    """
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

def get_csv_path(csv_filename):
    """
    Gets the absolute path from the python program to the .csv
    file. Necessary so the program can be ran from any folder.

    :param csv_filename: filepath of the .csv file
    :precondition:       csv_filename must be relative to the
                         python file
    :return: absolute path from python program to the .csv file
    """
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cur_dir, csv_filename)

def get_msg_prompts(csv_filename=CSV_FILE):
    """
    Gets all the message prompts from a .csv file as a dictionary.
    You can access the prompts using the message label as a keyword.

    :param csv_filename: .csv file where the message prompts will be
                         extracted
    :return: map of {keyword:full message}
    """
    csv_path = get_csv_path(csv_filename)
    msg_list = get_data_from_csv(csv_path)
    return msg_list_to_prompts(msg_list)


if __name__ == "__main__":
    main()