"""
Program that just runs a zig zag line of length 20 chars.
"""
import sys
import time

def run():
    """
    Function that runs the zig zag line.
    :return: None
    """
    try:
        MAX_LINE_LENGTH = 20

        indent = " "
        indent_length = 0
        line = "********"
        line_length = len(line)
        increase_indent = True

        while True:
            print(indent * indent_length, end='')
            print(line)
            time.sleep(0.4)

            if increase_indent:
                indent_length += 1
                if(line_length + indent_length >= 20):
                    increase_indent = False
            else:
                indent_length -= 1
                if(line_length + indent_length <= 0):
                    increase_indent = True

    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    run()