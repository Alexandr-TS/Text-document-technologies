from lxml import etree
from io import StringIO

fin = open('timetable.xml', 'r', encoding='utf-8')
dom = etree.parse(StringIO(fin.read()))

xslt = etree.parse('timetable_html.xslt')
transform = etree.XSLT(xslt)
newdom = transform(dom)

fout = open("timetable.html", 'w', encoding='utf-8')
fout.write(str(newdom))
