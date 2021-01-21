import requests
from lxml import html
from pandas import DataFrame as df

# Opens a request to scan the web page at provided URL.
# Then returns a tree object representing the HTML structure.
def obtaintree(url):
    libpage = requests.get(url)
    treelib = html.fromstring(libpage.content)
    return treelib

# Returns a list of each item sharing the HTML
# tag provided with the tree structure.
def obtaindata(tree, htmltag):
    return tree.xpath(htmltag)

# Receives lists consisting of name and address data for
# each library. Returns a tuple pairing the street address
# and borough with each library name.
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

# This function receives a tuple and list as input. Writes the
# data from the tuple into an xlsx (Excel) file.
def writetoxl(tupdata, incolumns):
    frame = df(tupdata, columns = incolumns)
    # Uncomment the below line to print the Data Frame.
    #print(frame)
    frame.to_excel("mtl_libraries.xlsx")

def main():
    webtree = obtaintree("https://montreal.ca/lieux?mtl_content.lieux.installation.code=BIBL&orderBy=dc_title")

    lib_names = obtaindata(webtree, '//div[@class="list-group-item-title"]/text()')
    lib_address = obtaindata(webtree, '//div[@class="list-group-item-infos rm-last-child-mb"]/text()')

    data_tuple = createtuple(lib_names, lib_address)

    writetoxl(data_tuple, ['Name', 'Address', 'Borough'])

if __name__ == "__main__":
    main()

