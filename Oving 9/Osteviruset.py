cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

print(cheeses['port salut'])

infeted_cheeses = set()
#infected_hylle = set()
for key in cheeses:
    for str in cheeses[key]:
        #hel_str = str
        #str.split(",")
        str = list(str)
        str.pop(-1)
        str.pop(-1)
        str = "".join(str)
        if str == "B13" or str == "B14" or str == "B15" or str == "A234" or str == "A235" or str == "C31":
            infeted_cheeses.add(key)
            #infected_hylle.add(hel_str)
infeted_cheeses = list(infeted_cheeses)
print("Potentially infected cheeses: ", infeted_cheeses)

for key in cheeses:
    if key not in infeted_cheeses:
        for hylle in cheeses[key]:
            print(hylle, ",", key)


