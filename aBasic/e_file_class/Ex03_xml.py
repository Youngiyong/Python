import xml.etree.ElementTree as et

#[참고] 위치 인자와 키워드인자 구별

tree = et.ElementTree(file='./data/temp.xml')
root = tree.getroot()
print('root:', root)
print('root tag:', root.tag)

for child in root:
    # print(child.tag)
    for twochild in child:
        print(twochild.tag,':',twochild.text)