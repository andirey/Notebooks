import re
starts_with_hash = 0

with open('input.txt', 'r') as f:
     # should be f, not file as described in text
    for line in f:              # look at each line in the file 
        if re.match("^#", line):  # use a regex to see if it starts with '#'
            starts_with_hash += 1 # if it does, add 1 to the count
            
print(starts_with_hash)           # added for output
