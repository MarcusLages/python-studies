#! python3
"""
mclip.py: Multi-clipboard program to practice python scripting.

:author: Marcus V S Lages
"""

import os, sys, pyperclip, csv, argparse

CSV_FILE = "prompts.csv"

def main():
    """
    Main function that runs the script. Checks for input validation
    and calls the right action.
    """
    args = parse_cmd_args()

    prompts = get_msg_prompts()
    is_in_terminal = sys.stdout.isatty()

    if args.list and is_in_terminal:
        print("Keyword\t\t| Message\n"
              "-------------------------------")
        for keyword, message in prompts.items():
            print(f"{keyword}\t\t| {message}")
        return

    if args.add:
        return

    if args.keyword in prompts:
        prompt = prompts[args.keyword]
        pyperclip.copy(prompt)

        if is_in_terminal:
            print(f"{args.keyword.title()} copied!\n"
                  f"Message: {prompt}")

    elif is_in_terminal:
        print("No messages recorded for this input.")

def parse_cmd_args():
    """
    Parses command line arguments into an object with the following
    Namespace with following attributes:\n
        list:       True if user would like to list all possible keywords
                    and messages
        add:        True if user would like to add a message to mclip\n
        keyword:    keyword to find or add a message on/to mclip\n
        full_message: full message for adding a message to mclip
    :return: parsed arguments as a Namespace object
    """
    #TODO: add version
    parser = argparse.ArgumentParser(
        description="Multi-clipboard program used to assign " \
                    "shortcuts to add phrases to the clipboard " \
                    "through just typing a keyword"
    )
    #TODO: add help for each argument and add the list and add option
    parser.add_argument("-l", "--list", action="store_true")
    parser.add_argument("-a", "--add", action="store_true")
    parser.add_argument("keyword", nargs="?")
    parser.add_argument("full_message",
                        nargs="*",
                        action="append")
    return parser.parse_args()

def get_data_from_csv(csv_filename):
    """
    Reads data from a .csv file and returns as a list of the rows with
    each row being an inner list.

    :param csv_filename: Name of the .csv file and path relative to the
                         python file
    :return:             .csv data as a list of rows
    """
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(cur_dir, csv_filename)

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
    You can access the prompts using the message label as a keyword.

    :return: map of {keyword:full message}
    """
    msg_list = get_data_from_csv(CSV_FILE)
    return msg_list_to_prompts(msg_list)


if __name__ == "__main__":
    main()