from xml.etree import ElementTree
import collections
import os

Course = collections.namedtuple('Course', 'title room building')

def main():
    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'xml_data', 'reed.xml')

    with open(file) as fin:
        xml_text = fin.read()

    dom = ElementTree.fromstring(xml_text)

    course_nodes = dom.findall('course')

    courses = [
        Course(
            n.find('title').text,
            n.find('place/room').text,
            n.find('place/building').text
        )
        for n in course_nodes
    ]
    # for n in course_nodes:
    #     c = Course(
    #         n.find('title').text,
    #         n.find('place/room').text,
    #         n.find('place/building').text
    #     )
    #     courses.append(c)

    building = input("What building are you in? ")
    room = input("What room are you next to? ")

    # List comprehension, 'Give me c.title(name of course) for some c in all courses if it's building and room
    room_courses = [
        c.title
        for c in courses
        if c.building == building and c.room == room
    ]

    for c in room_courses:
        print('* ' + c)


if __name__ == '__main__':
    main()
