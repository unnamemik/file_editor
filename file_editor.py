"""
Files to change: ./source (line 14)

String pattern to edit: pattern (line 17)
Data source list: payload (line 18)
Result string: new_str (line 33)

Result directory: ./result (line 37)
"""
import os
import re
from data import payload

directory = "./source"
files = os.listdir(directory)

pattern = 'pro'
payload = payload.keys()


def edit_data(source_str, new_str):
    result = re.search(pattern, source_str)
    if result:
        new_date = new_str + pattern
        start, stop = result.span()
        source_str = source_str[:start] + new_date + source_str[stop:]
    return source_str


def file_editor(data):
    for file in files:
        for item in data:
            new_str = item + '.'
            with open(f'./source/{file}', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    with open(f'./result/{new_str}{file}', 'a') as n:
                        n.write(edit_data(line, new_str))


if __name__ == '__main__':
    file_editor(payload)
    print('Finish')
