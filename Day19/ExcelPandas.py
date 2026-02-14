import pandas as pd
D1 = {"Venkat":"E1"}
D2 = {"E1":"P1"}
rows = []
for name, eid in D1.items():
    if eid in D2:
        rows.append({"Employee Name":name,"EID":eid,"Computer Name":D2[eid]})
df = pd.DataFrame(rows)
file_path = r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Day19\dictionarymapping.xlsx"        
df.to_excel(file_path,index = False)
print("!...Sheet Created...!",file_path)