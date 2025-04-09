# thu vien tinh toan tren mang
import numpy as np

a = np.array([[1, 3, 4, 5, 3, 8], [2, 4, 5, 6, 4, 9]])
print(a)

print(a.ndim) # in ra so chieu cua mang (hàng - cột)

print(a[0])
print(a[0][:4]) # lay tu vi tri 0 den (vi tri 4 ma tru 1)
print(a[0][2:4]) # [4, 5]