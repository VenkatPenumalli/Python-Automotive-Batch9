import xml.etree.ElementTree as ET
filepath = ET.parse(r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Day13\Medical.xml")
root = filepath.getroot()
medical_issues = []
for issue in root.findall(".//MedicalIssue"):
    if issue.text:
        medical_issues.append(issue.text.strip())
medical_issues.sort(key = str.lower)
print("Medical Issues ::",medical_issues)