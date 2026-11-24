from pathlib import Path
import os, genpalette

FILE = genpalette.FILE
DITS = 4

p = genpalette.FOLDER
if not p.exists():
    exit()

dirs, pdirs, width = next(p.walk())[1], [], 0
for i, dir in enumerate(dirs):
    pdirs.append('%s - %s' % (str(i).rjust(DITS, ' '), dir))
    if len(pdirs[-1]) > width:
        width = len(pdirs[-1])

while True:
    columns = max(1, int(os.get_terminal_size().columns / width))
    for i in range(0, len(dirs), columns):
        print(''.join([e.ljust(width, ' ') for e in pdirs[i:i+columns]]))

    inp = int(input('Type a number to swap: '))

    with p.joinpath(dirs[inp] + '/' + FILE).open(mode='r') as f:
        pal = f.read()

    with Path(FILE).open(mode='w') as f:
        f.write(pal)

    p = genpalette.FOLDER