import re
f = open('Texts.txt', 'r')
start = re.compile('^\+\s+Bible')
end   = re.compile('^-')
found = False
for line in f: 
    if re.match(start, line): 
        found = True
    if re.match(end, line): 
        found = False
    if found == True: 
        print line

