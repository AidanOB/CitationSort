import xml.etree.ElementTree as xmlEt
import init

__author__ = "Aidan O'Brien"


def load_files(file_list):
    """
    This function takes the list of files and returns an object containing citations
    :param file_list: A list of filenames to be opened
    :return: List of objects converted from xml
    """
    citation_blocks = []

    for file in file_list:
        root = xmlEt.parse(file).getroot()
        citation_blocks.append(root)

    return citation_blocks


# Test line to run below
'''
loaded_blocks = load_files(init.file_list)

for file in loaded_blocks:
    for citations in file:
        print(len(citations))
        for child in citations:
            print(child.tag, child.attrib)
'''