# Easy 

def tinhGiaiThua(i):

    """ Viet 1 phan lap trinh tinh phuong giai thua cua i
    tra ve con so i! (gia su i la so nguyen duong)
    vi du: tinhGiaiThua(0) = 1, tinhGiaiThua(1) = 1, tinhGiaiThua(4) = 24 ...
    tips: for(while) loop, 
    """

    #viet o day 
    if i == 0:
        return 1
    a = 1

    for n in range(1, i+1):
        a *= n
    return a


def timSoChan(i):
    """ viet 1 phan lap tring tra ve True neu i la so chan
    tra ve false if i la so le. gia su i la so nguyen
    vidu: timSoChan(1) = False, timSoChan(2)= True, ...
    tips: % trong python se tra lai so du. e.g 1%10 = 1, 5%3 = 2
    """
    #viet o day 
    if i % 2 == 0:
        return True
    else:
        return False 

def timThuVien(a, i):
    """ Tim giai nghia cua i trong thu vien a
    vi du: timThuVien({1: "so 1", 2: "so 2"}, 2) = "so 2"
    tip: a la dict(). xin voi long coi them tren mang :P
    """
    
    return a[i]
# Intermediate

def giaiMa(i):
    """ viet 1 phuong tring giai ma 1 chuoi so thanh 1 day ki tu
        biet rang moi chu so da bi di chuyen +2. gia su i la so chuoi nguyen duong
        vidu giaiMa([106,107]) = 'hi', giaMa([101,113,112]) = 'con'
        tips: ord(i) se bien ki tu thanh so va chr(i) se bien so thanh ki tu
    """
    # viet o day
    a = ""
    for n in i:
        a += chr(n-2)
    return a

def timAnSO(a, i):
    """viet 1 phuong trinh tra ve 1 chuoi trong chuoi a
    khi ma phat hien i dau tien trong chuoi a
    vi du: timAnSO([0,1], 0) = [], timAnSo([1,23,5,7,146,5], 5) = [1,23]
    """
    # viet o day
    
    for n in range(len(a)):
        if a[n] == i:
            break
    return a[:n]

# Hard

def timSoChu(i,a=open("./test.txt","r")):
    """ viet 1 phuong trinh tra ve so chu cai i trong file a
        vi du: timChu(open("./test","r"), "la") = 3
    """
    t =0
    for h in a.readlines():
        
        for m in h.split():
            if (m == i):
                
                t+=1
    return t

def ghepChuTheoThuTu(a, b):
    """ viet 1 phuong tring tra ve tong hop cua a va b theo thu tu
    vi du: ghepChuTheoThuTu("cac", "ba") = "aabcc"
    """
    t = ""
    h = sorted(a+b)
    for i in h:
        t+= i
    return t
    
def timChu(b,c,a=open("./test.txt","r")):
    """ viet 1 phuong trinh tra ve chuoi chu bat dat dau giong b va ket thuc giong c
        vi du: timChu(open("./test","r"), "l","n") = ["lon"]
    """
    # viet o day
    import re
    d = []
    for i in a.readlines():
        
        for h in i.split():
            m = re.search("(" + b + "[a-z]*" + c + ")" , h)
            
            if (m != None and m. group() not in d):
                d.append(m.group())
    return d

class Unittest(object):
    '''class for testing not to be touched'''

    def __init__(self):
        '''class constructor'''
        pass
    
    def testTinhGiaThua():
        try:
            dapAn = [tinhGiaiThua(i) for i in [0,1,2,4,6,10]] # dap an from tinh giai thua
            if dapAn == [1,1,2, 24, 720, 3628800]: # dap an chinh xac 
                print("testTinhGiaThua: Dap an la chinh xac")
            else: # dap an sai
                print("testTinhGiaThua: dap an sai. Xinh lam lai")
        except Exception as err: # catch error 
            print("testTinhGiaThua: Phuong trinh dung khong dung")

    def testTimSoChan():
        try:
            dapAn = [timSoChan(i) for i in [0,1,2,5,8,11]] # dap an from tinh giai thua
            if dapAn == [True,False,True, False, True, False]: # dap an chinh xac 
                print("testTimSoChan: Dap an la chinh xac")
            else: # dap an sai
                print("testTimSoChan: dap an sai. Xinh lam lai")
        except Exception as err: # catch error 
            print("testTimSoChan: Phuong trinh dung khong dung")

    def testTimThuVien():
        try:
            dapAn = timThuVien({1: "ok",2:"hi", 3:"hum"}, 1) # dap an from tinh giai thua
            if dapAn == "ok": # dap an chinh xac 
                print("testTimThuVien: Dap an la chinh xac")
            else: # dap an sai
                print("testTimThuVien: dap an sai. Xinh lam lai")
        except Exception as err: # catch error 
            print("testTimThuVien: Phuong trinh dung khong dung")
    
    def testGiaiMa():
        try:
            dapAn = giaiMa([111,119,112,101,106,107,103,117]) # dap an from tinh giai thua
            if dapAn == 'munchies': # dap an chinh xac 
                print("testGiaiMa: Dap an la chinh xac")
            else: # dap an sai
                print("testGiaiMa: dap an sai. Xinh lam lai")
        except Exception as err: # catch error 
            print("testGiaiMa: Phuong trinh dung khong dung")
    def testTimAnSo():
        try:
            dapAn = timAnSO([111,119,112,101,106,107,103,117], 101) # dap an from tinh giai thua
            if dapAn == [111,119,112]: # dap an chinh xac 
                print("testTimAnSo: Dap an la chinh xac")
            else: # dap an sai
                print("testTimAnSo: dap an sai. Xinh lam lai")
        except Exception as err: # catch error 
            print("testTimAnSo: Phuong trinh dung khong dung")
            
    def testTimSoChu():
        try:
            dapAn = timSoChu("toi") # dap an from tinh giai thua
            if dapAn == 5: # dap an chinh xac 
                print("testTimSoChu: Dap an la chinh xac")
            else: # dap an sai
                print("testTimSoChu: dap an sai. Xinh lam lai")
        except Exception as err:
            print("testTimSoChu: Phuong trinh dung khong dung")
    def testGhepChuTheoThuTu():
        try:
            dapAn = ghepChuTheoThuTu("toi la toi", "toi") # dap an from tinh giai thua
            if dapAn == "  aiiilooottt": # dap an chinh xac. checked alphabet again xD 
                print("testGhepChuTheoThuTu: Dap an la chinh xac")
            else: # dap an sai
                print("testGhepChuTheoThuTu: dap an sai. Xinh lam lai")
        except Exception as err: # catch error 
            print("testGhepChuTheoThuTu: Phuong trinh dung khong dung")

    def testTimChu():
        try:
            dapAn = timChu("t", "i") # dap an from tinh giai thua
            if dapAn == ["toi", "tuoi", "tui"]: # dap an chinh xac. checked alphabet again xD 
                print("testTimChu: Dap an la chinh xac")
            else: # dap an sai
                print("testTimChu: dap an sai. Xinh lam lai")
        except Exception as err: # catch error 
            print("testTimChu: Phuong trinh dung khong dung"+repr(err))
# function main

if __name__ == "__main__":
    Unittest.testTinhGiaThua()
    Unittest.testTimSoChan()
    Unittest.testTimThuVien()
    Unittest.testGiaiMa()
    Unittest.testTimAnSo()
    Unittest.testTimSoChu()
    Unittest.testGhepChuTheoThuTu()
    Unittest.testTimChu()
    
