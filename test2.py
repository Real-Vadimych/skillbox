dct = {
    '1111:271': 111, 
    '1111:190': 3, 
    '1231:106': 13, 
    '1211:104': 111, 
    '1111:201': 9
}

# Initialize your new dict
new_dct = {k.split(':')[0]: {} for k in dct}
# Loop through old dict
for k, v in dct.items():
    # Set value to top > sub key in new dict
    new_dct[k.split(':')[0]][k.split(':')[1]] = v

print(new_dct)