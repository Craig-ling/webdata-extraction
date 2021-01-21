import requests
from lxml import html
from pandas import DataFrame as df

def obtaintree(url):
    libpage = requests.get(url)
    treelib = html.fromstring(libpage.content)
    return treelib

def obtaindata(tree, htmltag):
    return tree.xpath(htmltag)

def createtuple(namedata, addrdata):
    i = 0
    f = 0
    g = 1
    lib_tuples = []
    while i < len(namedata):
        lib_tuples.append((namedata[i], addrdata[f],
                                 addrdata[g]))
        i += 1
        f += 2
        g += 2

    return lib_tuples

def writetoxl(tupdata, columns):
    frame = df(tupdata, columns = columns)
    frame.to_excel("mtl_libraries.xlsx")

def main():
    webtree = obtaintree("https://montreal.ca/lieux?mtl_content.lieux.installation.code=BIBL&orderBy=dc_title")

    lib_names = obtaindata(webtree, '//div[@class="list-group-item-title"]/text()')
    lib_address = obtaindata(webtree, '//div[@class="list-group-item-infos rm-last-child-mb"]/text()')

    data_tuple = createtuple(lib_names, lib_address)

    writetoxl(data_tuple, ['Name', 'Address', 'Borough'])

if __name__ == "__main__":
    main()

