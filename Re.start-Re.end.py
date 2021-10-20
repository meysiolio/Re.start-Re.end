import re

string = input()
substring = input()

result = list(re.finditer('(?=' + substring + ')', string))
if result:
    for i in result:
        print(f'({i.start()}, {i.start() + len(substring) - 1})')
else:
    print('(-1, -1)')