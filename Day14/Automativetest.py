import xml.etree.ElementTree as ET
textfile = r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Day14\data.txt"
xmlfile = r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Day14\cars.xml"
current_car = {}
cars = []
with open(textfile,"r") as file:
    for line in file:
        line = line.strip()
        if not line:
            if current_car:
                cars.append(current_car)
                current_car = {}
            continue
        key, value = line.split("=")
        current_car[key] = value
if current_car:
    cars.append(current_car)
root = ET.Element("Cars")
for car in cars:
    car_element = ET.SubElement(root,"Car")
    for key, value in car.items():
        element = ET.SubElement(car_element, key)
        element.text = value
tree = ET.ElementTree(root)
tree.write(xmlfile,encoding="utf-8",xml_declaration=True)
print("XML file created successfully!")