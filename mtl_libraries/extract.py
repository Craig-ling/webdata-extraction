import requests
from lxml import html
from pandas import DataFrame as df

libpage = requests.get("https://montreal.ca/lieux?mtl_content.lieux.installation.code=BIBL&orderBy=dc_title")
treelib = html.fromstring(libpage.content)
lib_names = treelib.xpath('//div[@class="list-group-item-title"]/text()')
lib_address = treelib.xpath('//div[@class="list-group-item-infos rm-last-child-mb"]/text()')

i = 0
f = 0
g = 1
lib_tuples = []

while i < len(lib_names):
    lib_tuples.append((lib_names[i], lib_address[f],
                             lib_address[g]))
    i += 1
    f += 2
    g += 2

print(lib_tuples)

frame = df(lib_tuples, columns = ['Name', 'Address', 'Borough'])
print(frame)
frame.to_excel("mtl_libraries.xlsx")

