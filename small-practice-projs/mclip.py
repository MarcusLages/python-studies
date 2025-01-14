#! python3
# mclip.py: Multi-clipboard program to practice python scripting.

import sys, pyperclip

# TODO: it would be cool to read this from a .txt file that is editable
PROMPTS = {
    'agree' : "Yes. Looks good to me.",
    'busy' : "Sorry, can we talk later"
}

def main():
    args = sys.argv

    if len(args) < 2:
        print("Not enough arguments.")
        sys.exit()

    message = args[1]
    if message in PROMPTS:
        prompt = PROMPTS[message]
        pyperclip.copy(prompt)
        print(f"{message.title()} copied!\nMessage: {prompt}")
    else:
        print("No messages recorded for this input.")

if __name__ == "__main__":
    main()