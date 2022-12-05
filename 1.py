def count_cals(s):
    cal_lists = s.split('\n\n')
    cal_amt = []
    cur_max = -float('inf')

    for elf_cals in cal_lists:
        tot = 0
        for cal in elf_cals.split('\n'):
            tot += float(cal)

        cal_amt.append(tot)
        cur_max = max(cur_max, tot)

    return cur_max, cal_amt

# Can't use URLLib bc it uses cookies specific to user
# Copy-paste to data file
with open('data.txt','r') as f:
    data = f.read()

# Part 1
max_cal, cals = count_cals(data)
print(max_cal)

# Part 2 
# I forget how to do top k.. I think there's an O(n) way 
# to do this, but.. eh 
cals.sort() 
print(cals[-3:])
print(sum(cals[-3:]))