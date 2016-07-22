import init
import sys
from xml.etree.ElementTree import Element, SubElement, ElementTree, Comment, tostring, dump
__author__ = "Aidan O'Brien"


def save_citations(citations):
    """
    This function takes an object with a list of xml records and saves them in EndNote format for import
    :param citations: List of XML citations
    :return: Integer of citations successfully written to file, -1 if error
    """
    xml = Element("xml")
    comment = Comment("This citation merger was written by Aidan O'Brien")
    xml.append(comment)
    child = SubElement(xml, "records")
    count = 0
    for record in citations:
        child.append(record)
        count += 1

    file = open(init.output_file_path + "common.xml", mode='wb')
    print(tostring(xml))
    file.write(tostring(xml))
    ElementTree(xml).write(sys.stdout)
    #ElementTree(xml).write(file)

    # try:
    #
    # except():
    #     count = -1

    return count



