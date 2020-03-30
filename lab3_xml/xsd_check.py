from lxml import etree

xsd_validator = etree.XMLSchema(file="timetable.xsd")
xsd_parser = etree.XMLParser(schema=xsd_validator)
tree_2 = etree.parse('timetable.xml', xsd_parser)
