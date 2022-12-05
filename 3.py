with open('data.txt', 'r') as f:
    data = f.read()


def val(i):
    ascii = ord(i)
    # 'a' == 97
    if ascii >= 97:
        return ascii - 96

    # 'A' == 65
    else: 
        return ascii - 38 


##### PART 1 #####
def shared_item(items):
    tot_per = len(items)//2
    top,bottom = items[:tot_per], items[tot_per:]
    
    tvals = set([i for i in top])
    bvals = set([i for i in bottom])

    return tvals.intersection(bvals)

def get_shared_items(packs):
    vals = 0
    for pack in packs.split('\n'):
        shared = shared_item(pack)
        
        if len(shared) > 1:
            print("Hmm")

        vals += val(shared.pop())

    return vals 

print(get_shared_items(data))


##### PART 2 #####
def shared_group(groups):
    bags = [set([i for i in g]) for g in groups]
    return bags[0].intersection(*bags)

def pt2(data):
    bags = data.split('\n')
    cnt = 0
    for i in range(len(bags)//3):
        st = i*3; end = (i*3)+3
        shared = shared_group(bags[st:end])
        cnt += val(shared.pop())

    return cnt 

print(pt2(data))