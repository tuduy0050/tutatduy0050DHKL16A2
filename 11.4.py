# List number 1
lst = []
while True:
    x = int(input("Nhập giá trị: "))
    tt = int(input("Có tiếp tục nhập giá trị?\n1: Có || Khác: Không \n"))
    lst.append(x)
    total = 0
    for giatri in lst:
        total += giatri
    if tt != 1:
        a = int(input("Nhập giá trị cần tìm x: "))
        print("List:",lst)
        print("Tổng các giá trị trong List:",total)
        print("Số",a,"xuất hiện",lst.count(x),"lần trong List")
        if a < giatri in lst:
            print("Số",a,"Không lớn hơn tất cả các số trong List")
            newlst = [num for num in lst if num > a]
            print("Các số không lớn hơn",a,"trong List:",newlst)
        else:
            print("Số",a,"Lớn hơn tất cả các số trong List")
        break
