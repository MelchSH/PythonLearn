
import xml.sax
"""
CD_counter = 0
class groupHandler(xml.sax.ContentHandler):

    def startElement(self, name:str ,attrs:str) -> None:
        self.current = name
        
        if self.current == "CD":
            global CD_counter
            print("-----CD DESCRIPTION-----")

    def characters(self, content: str) -> None:
        if self.current == "TITLE":
            self.title = content
        elif self.current == "ARTIST":
            self.artist = content
    
    def endElement(self, name: str) -> None:
        if self.current == "TITLE":
            print("CD NAME: {}".format(self.title))
        elif self.current == "ARTIST":
            print("ARTIST NAME: {}".format(self.artist))
        self.current = ""

handler = groupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("test.xml")
"""


import xml.dom.minidom as minidom

CD_counter = 0


domtree = minidom.parse("test.xml")

category = domtree.documentElement
cd = category.getElementsByTagName("CD")


for cds in cd:
    print("----CD {}----".format(CD_counter))
    CD_counter +=1

    print("TITLE: {}".format(cds.getElementsByTagName("TITLE")[0].childNodes[0].data))


cd[24].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue = "AAAAAAAAAAAA"
domtree.writexml(open("test.xml", "w"))









