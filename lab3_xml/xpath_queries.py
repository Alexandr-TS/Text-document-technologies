from lxml import etree
from io import StringIO

fin = open('timetable.xml', 'r', encoding="utf-8")
tree = etree.parse(StringIO(fin.read()))


print ("a) Все занятия на этой неделе:")
response = tree.xpath('/Timetable/Day/Class')
for clas in response:
    print(etree.tostring(clas, encoding=str))
enter = input()

print ("b) Все аудитории:")
r = set(tree.xpath('//ClassRoom/text()'))
print(r)
enter = input()


print ("c) Практики:")
response = tree.xpath('/Timetable/Day/Class[Type="Практика"]')
for clas in response:
    print(etree.tostring(clas, encoding=str))
enter = input()


classroom = 407
print ("d) Лекции в {}:".format(str(classroom)))
response = tree.xpath('/Timetable/Day/Class[Type="Лекция" and ClassRoom={}]'.format(str(classroom)))
for clas in response:
    print(etree.tostring(clas, encoding=str))
enter = input()


classroom = 239 
print ("e) Преподаватели с практиками в {}:".format(str(classroom)))
response = set(tree.xpath('/Timetable/Day/Class[Type="Практика" and ClassRoom={}]/Teacher/text()'.format(str(classroom))))
for teacher in response:
    print(teacher)
enter = input()


print ("f) Последнее занятие каждого дня:") 
response = tree.xpath('/Timetable/Day/Class[position()=last()]')
for clas in response:
    print(etree.tostring(clas, encoding=str))
enter = input()


print ("g) Всего занятий за неделю:") 
response = int(tree.xpath('count(/Timetable/Day/Class)'))
print (response)

