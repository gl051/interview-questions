"""
    Problem:
    http://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/
"""

def count_triplete(alist, val):
    """
        Per each element (base) we build all the triplete possibile, you get the
        second element (pvt) and then look for all other third element. Since we
        are interested into the sum of the triplete we don't need to go back building
        triplete when moving the PVT ahead.
        2 1 5 7
        2 1 5, 2 1 7, 2 5 7, (no 2 5 1 for the sum), 1 5 7, (no 1 2 5)
    """
    print 'input ', alist
    count = 0
    for base in range(len(alist)-2):
        for pvt in range(base+1, len(alist)):
            if pvt + 1 < len(alist):
                if (alist[base] + alist[pvt] + alist[pvt+1]) < val:
                    count += 1
                    print alist[base], alist[pvt], alist[pvt+1]
            if pvt + 2 < len(alist):
                if (alist[base] + alist[pvt] + alist[pvt+2]) < val:
                    count += 1
                    print alist[base], alist[pvt], alist[pvt+2]
            if pvt + 3 < len(alist):
                if (alist[base] + alist[pvt] +alist[pvt+3]) < val:
                    count += 1
                    print alist[base], alist[pvt], alist[pvt+3]
    print 'Counted {} with sum lesss than {}'.format(count, val)

def count_triplete2(alist, val):
    """
        To improve perfomances you can first sort the list and working as
        before but stopping building triplete for a given base when the you
        meet the first sum >= value
    """
    slist = sorted(alist)
    count = 0
    for base in range(len(slist) -2):
        for pvt in range(base+1, len(slist)):
            tmp_sum = 0
            if pvt + 1 < len(alist):
                tmp_sum = alist[base] + alist[pvt] + alist[pvt+1]
                if tmp_sum < val:
                    count += 1
                    print alist[base], alist[pvt], alist[pvt+1]
                else:
                    break
            if pvt + 2 < len(alist):
                tmp_sum = alist[base] + alist[pvt] + alist[pvt+2]
                if tmp_sum < val:
                    count += 1
                    print alist[base], alist[pvt], alist[pvt+2]
                else:
                    break
            if pvt + 3 < len(alist):
                tmp_sum = alist[base] + alist[pvt] + alist[pvt+3]
                if tmp_sum < val:
                    count += 1
                    print alist[base], alist[pvt], alist[pvt+3]
                else:
                    break
    print 'Counted {} with sum lesss than {}'.format(count, val)



#count_triplete([-2, 0, 1, 3], 2)
count_triplete2([-2, 0, 1, 3, 9, 34, 67, 23, 55], 2)
