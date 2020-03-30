from lxml import etree
from io import StringIO

fin = open('timetable.xml', 'r', encoding='utf-8')
dom = etree.parse(StringIO(fin.read()))

xslt = etree.parse('timetable_txt.xslt')
transform = etree.XSLT(xslt)
newdom = transform(dom)

fout = open("timetable.txt", 'w')
fout.write(str(newdom))
