"""
    Given a list of non negative integers, arrange them such that they form the largest number.
    For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
    Note: The result may be very large, so you need to return a string instead of an integer.
"""

def find_largest(nums):
    # remove a zero element which goes to the end
    tail = ""
    while 0 in nums:
        nums.remove(0)
        tail += '0'
    # convert to a string representation
    slist = [str(i) for i in nums]
    slist.sort()
    res = ""
    for x in slist:
        print res, x
        res = max(res+x, x+res)
        print res
    print res + tail

def demo(nums):
    print map(str, nums)
    print sorted(map(str, nums), lambda x, y: [1, -1][x + y > y + x])

demo([128,12,320,32])
#find_largest([128,12,320,32])
#r = ''.join(sorted(map(str, nums), lambda x, y: [1, -1][x + y > y + x]))
