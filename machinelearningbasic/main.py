from sklearn import  tree

mytree = tree.DecisionTreeClassifier() # init cây quyết định

dac_trung = [[1, 3, 3, 7],
             [5, 2, 4, 6],
             [1, 2, 4, 6],
             [5, 4, 4, 3],
             [1, 4, 4, 7],
             [3, 2, 3, 7],
             [3, 3, 3, 6],
             [5, 2, 2, 7]
            ]

nhan = [0, 1, 1, 0, 0, 0, 0, 1]

result = mytree.fit(dac_trung, nhan) #tranning

kq1 = result.predict([[1, 4, 3, 6]]) # du doan
kq2 = result.predict([[1, 4, 3, 7]])
print(kq1)
print(kq2)

# Bước 1: thu thập dữ liệu
# Bước 2: xử lý dữ liệu
# Bước 3: training model (xây dựng model)
# Bước 4: dự đoán kết quả
# Bước 5: đánh giá xem model có hiệu quả không
