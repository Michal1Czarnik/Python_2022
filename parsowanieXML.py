#!/usr/bin/python3

from xml.dom import minidom
import xml.sax

#SAX 
parser = xml.sax.make_parser()
docSAX = parser.parse("exampleXML.xml")

#DOM 
docDOM = minidom.parse("exampleXML.xml")

#modyfikacja
name = docDOM.getElementsByTagName("name")
firstchild = name[0]
firstchild.setAttribute('isTasty', 'yes')
createXML = docDOM.toxml()
save = "exampleXMLDOMChanged.xml"
with open(save, "w") as f: 
    f.write(createXML)


