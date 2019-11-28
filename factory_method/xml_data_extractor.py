from xml.etree import ElementTree


class XMLDataExtactor:

    def __init__(self, filepath):
        self.tree = ElementTree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
