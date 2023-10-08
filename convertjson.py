
import json

file1 = open('publication_list.txt');
count = 0
linecnt = 0
bibtextentries = []
bibtextentry = ""
urlentries = []
urlentry = ""
while True:
    line1 = file1.readline()
    if (not line1):
        break
    if (line1[0]=="#"):
        continue
    if (len(line1)>1):
        line1 = line1[:-1]
    if (line1.find("url")>=0):
        urlentry = line1.split("=")[1].strip().strip("{}")
    if (line1[0]=="@" and linecnt!=0):
        bibtextentries.append(bibtextentry)
        urlentries.append(urlentry)
        bibtextentry=""
        urlentry = ""
        count+=1
    bibtextentry+=line1
    linecnt+=1
bibtextentries.append(bibtextentry)
urlentries.append(urlentry)
file1.close()

print(bibtextentries)
print(urlentries)

json_object = json.dumps({"citations":bibtextentries,"urls":urlentries})
with open ("publication_list.json","w") as outfile:
    outfile.write(json_object)