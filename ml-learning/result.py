def get_result(h,e,m,sci,sst):
    total=h+e+m+sci+sst
    percentage=total/5
    return total, percentage

t,p=get_result(85,90,78,88,92)
print("Total:", t)
print("Percentage:", p)