def reverse(x):
    if x>=0:
        str_x=str(x)[::-1]
        int_x=int(str_x)
        if int_x>2**31-1:
            return 0
        else:
            return int_x
    else:
        str_x=str(x)[1::]
        str_x=str_x[::-1]
        int_x=int(str_x)
        if -int_x<-2**31:
            int_x=0
        return -int_x



print(reverse(1534236469))
