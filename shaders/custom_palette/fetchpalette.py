import sys, urllib.request, json, re, genpalette
from pathlib import Path

FILE = genpalette.FILE
APIEXT = '.json'

try:
    link = '%s' % sys.argv[1]
except IndexError:
    print('First argument should be a link to the site lospec')

with urllib.request.urlopen(link + APIEXT) as dat:
    map = json.loads(dat.read().decode(encoding='utf-8', errors='ignore'))

print(map)

genpalette.lines = ['// ' + map['name'], '// Author: ' + map['author'], '// ' + link, '',
         'const int colorNum = %s;' % len(map['colors']),
         'vec3 colors[colorNum] = vec3[](']

genpalette.hexvalues = map['colors']
genpalette.colorBetweenLines()

for l in genpalette.lines:
    print(l)

p = genpalette.FOLDER
if not p.exists():
    p.mkdir()

p = p.joinpath(re.sub(r'[^a-zA-Z0-9]+', '', map['name']))
if not p.exists():
    p.mkdir()

genpalette.write(p.joinpath(FILE))
genpalette.write(Path('./' + FILE))
