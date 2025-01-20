import pandas as pd

df=pd.read_csv('/Users/s.eromonsei/Downloads/crr_forecast_load.csv')

# # df.to_xml(path_or_buffer=r'/Users/s.eromonsei/stageGitHub/my_sandbox/Engineering/DataEngineering/ETL_pipeline/xml_ingestion/my_crr.xml',
# #           namespaces={"xsi:CRRHistoricalForecast": "http://www.w3.org/2002/XMLSchema-instance","schemaLocation":["http://crr.caiso.org/download/xml", "https://FSAPJBOS9:11107/crr/download/xml/mui/historicalForecast.xsd"],"CRRHistoricalForecast":"http://crr.caiso.org/historicalForecast/xml"},
# #           prefix="CRRHistoricalForecast",
# #           root_name='historicalForecastData',
# #           #elem_cols=['shape','degrees','sides'],
# #           index=False,
# #           row_name='itemHistoricalForecastData',
# #          parser='etree')


# import xml.etree.ElementTree as ET
# from xml.dom import minidom

# def pretty_print(root):
#     """Pretty print the XML tree"""
#     rough_string = ET.tostring(root, 'utf-8')
#     reparsed = minidom.parseString(rough_string)
#     print(reparsed.toprettyxml(indent="  "))

# # Register namespaces
# ET.register_namespace('CRRHistoricalForecast', "http://crr.caiso.org/XXX/xml")
# ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")

# # Define namespaces in a dictionary for easy reference
# namespaces = {
#     'CRRHistoricalForecast': "http://crr.caiso.org/XXX/xml",
#     'xsi': "http://www.w3.org/2001/XMLSchema-instance",
# }

# # Define the root element properly with namespace
# root = ET.Element("{http://crr.caiso.org/XXX/xml}historicalForecastData", {
#     "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://XXX.org/download/xml https://FSAPJBOS9:11107/crr/download/xml/mui/XXX.xsd",
# })

# # The rest of your element creation remains the same

# # Create the child elements
# items = ET.SubElement(root, "{http://crr.caiso.org/XXX/xml}items")
# item = ET.SubElement(items, "{http://crr.caiso.org/XXX/xml}itemHistoricalForecastData")

# # Populate the item with data
# for key , value in df.iterrows():
#     ET.SubElement(item, "{http://crr.caiso.org/XXX/xml}{}".format(key)).text = str(value)


# pretty_print(root)
# tree = ET.ElementTree(root)
# tree.write("/Users/s.eromonsei/stageGitHub/my_sandbox/Engineering/DataEngineering/ETL_pipeline/xml_ingestion/CRRHistoricalForecast.xml", xml_declaration=True, encoding="utf-8", method="xml")

# print("XML file 'CRRHistoricalForecast.xml' has been created.")


import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Assuming 'df' is your DataFrame loaded from the CSV file
# df = pd.read_csv('/Users/s.eromonsei/Downloads/crr_forecast_load.csv')

def pretty_print(element):
    """Pretty print the XML tree"""
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    print(reparsed.toprettyxml(indent="  "))

# Register namespaces
namespace = "http://crr.caiso.org/XXX/xml"
ET.register_namespace('CRRHistoricalForecast', namespace)

# Register namespaces
ET.register_namespace('CRRHistoricalForecast', "http://crr.caiso.org/XXX/xml")
ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")

# Define the root element properly with namespace
root = ET.Element("{http://crr.caiso.org/XXX/xml}historicalForecastData", {
    "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://XXX.org/download/xml https://FSAPJBOS9:11107/crr/download/xml/mui/XXX.xsd",
})

# Create the 'items' container element
items = ET.SubElement(root, "{http://crr.caiso.org/XXX/xml}items")

# Iterate over DataFrame rows
for _, row in df.iterrows():
    # Create a new 'itemHistoricalForecastData' element for each row
    item = ET.SubElement(items, "{http://crr.caiso.org/XXX/xml}itemHistoricalForecastData")
    for col_name, value in row.items():
        # # Create a sub-element for each column in the row, setting its text to the column's value
        # ET.SubElement(item, "{http://crr.caiso.org/XXX/xml}{}".format(col_name)).text = str(value)
        tag = ET.QName(namespace, col_name)  # Using QName to handle namespace
        ET.SubElement(item, tag).text = str(value)

pretty_print(root)

# Save the XML to a file
tree = ET.ElementTree(root)
tree.write("/Users/s.eromonsei/stageGitHub/my_sandbox/Engineering/DataEngineering/ETL_pipeline/xml_ingestion/CRRHistoricalForecast.xml", xml_declaration=True, encoding="utf-8", method="xml")

print("XML file 'CRRHistoricalForecast.xml' has been created.")
