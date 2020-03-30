from lxml import etree

dtd_parser = etree.XMLParser(dtd_validation=True)
tree_1 = etree.parse('timetable.xml', dtd_parser)
