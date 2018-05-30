import sys
import os
import re


def main(lines_path, conversations_path, prompts_path="prompts.txt", responses_path="responses.txt"):
    lines_path = os.path.join(lines_path)
    conversations_path = os.path.join(conversations_path)
    prompts_path = os.path.join(prompts_path)
    responses_path = os.path.join(responses_path)

    num_re = re.compile(r"^L\d+")
    #text_re = re.compile(r"(++$++)\w+

    delimiter="+++$+++"

    line_table = {}

    #Apparently the corpus uses this ISO encoding
    with open(lines_path, "r", encoding="iso-8859-1") as lines:
        for line in lines.readlines():
            bad_lines = 0
            line_num = int(num_re.search(line).group()[1:])
            line_text = line.split(delimiter)[-1].strip()
            line_table[line_num] = line_text 


if __name__ == "__main__":
    lines = os.path.join(sys.argv[1])
    conversations = os.path.join(sys.argv[2])
    main(lines, conversations)
