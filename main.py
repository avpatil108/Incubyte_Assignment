# import pytest

def test():
    assert(add("")==0)

    assert (add("25") == 25)
    assert (add("1,1005") == 1)
    assert (add("2,5,7,1,5,10") == 30)
    assert (add("1,2,a,b")==6)
    print("All test passed")

def add(numStr):
    if len(numStr)==0:
        print(0)
        return 0
    elif len(numStr)==1:
        print(int(numStr))
        return int(numStr)
    elif len(numStr)>=2:
        result=0
        nums=numStr.split(",")
        for i in nums:
            if i.isalpha():
                temp = ord(i)
                temp=temp-96
                i=str(temp)
            if int(i)>1000:
                i="0"
            result+=int(i)
        print(result)
        return result


test()