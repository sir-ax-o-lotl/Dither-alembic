import sys, datetime, re
from pathlib import Path

FILE = 'palette.glsl'
FOLDER = Path('./Palettes')
TAB = '    '

def main(argv):
    global hexvalues, lines
    hexvalues = argv[1:]
    if len(hexvalues) == 0:
        print('Arguments should be hex values separated by whitespace.\n' +
              'Example: "%s 000000 FFFFFF"' % Path(__file__).name)
        exit()

    palettename = input('Type a name for the palette: ')
    palettename = palettename if palettename != '' else str(datetime.datetime.now())

    lines = ['// ' + palettename, '// Author: ', '// %s' % hexvalues, '',
            'const int colorNum = %s;' % len(hexvalues),
            'vec3 colors[colorNum] = vec3[](']

    colorBetweenLines()

    for l in lines:
        print(l)

    p = FOLDER
    if not p.exists():
        p.mkdir()

    p = p.joinpath(re.sub(r'[^a-zA-Z0-9]+', '', palettename))
    if not p.exists():
        p.mkdir()

    print(p.as_posix())

    write(p.joinpath(FILE))
    write(Path('./' + FILE))

def dehex(someInt):
    return (someInt & 255) / 255

def write(path):
    with path.open(mode='w', errors='ignore') as f:
        f.writelines('\n'.join(lines))

def colorBetweenLines():
    global hexvalues, lines
    darkest = pow(256, 3);
    lightest = -1;

    for hexcolor in hexvalues:
        i = int(hexcolor, 16)
        r,g,b = dehex(i >> 16), dehex(i >> 8), dehex(i)
        lines.append('%svec3(%s, %s, %s),' % (TAB, r,g,b))
        if i < darkest:
            darkest = i
            darkLine = lines[-1]
        if i > lightest:
            lightest = i
            lightLine = lines[-1]


    lines[-1] = str(lines[-1])[:-1]
    lines.append(');')
    lines.append('const vec3 darkColor = %s;' % darkLine[len(TAB):-1])
    lines.append('const vec3 lightColor = %s;' % lightLine[len(TAB):-1])


if __name__ == "__main__":
    main(sys.argv)