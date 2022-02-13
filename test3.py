dct = {
    '1111:271': 111, 
    '1111:190': 3, 
    '1231:106': 13, 
    '1211:104': 111, 
    '1111:201': 9
}

items_count2  = {}
for k, v in dct.items():  
  t = items_count2.get(k.split(':')[0],{})
  t[k.split(':')[1]] = v
  items_count2[k.split(':')[0]] = t

print(items_count2)