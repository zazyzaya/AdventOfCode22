from urllib.request import urlopen 

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

data = urllib.request()