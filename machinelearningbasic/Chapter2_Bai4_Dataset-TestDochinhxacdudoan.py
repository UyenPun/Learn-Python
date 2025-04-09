# Dataset: Dữ liệu mà chúng ta sử dụng trong phần này
# là một tập dữ liệu đã được sưu tầm và tổ chức dưới
# dạng bảng và được dán nhãn phân loại cụ thế mình gọi đây là dataset.
# Và bộ dữ liệu này đã có sẵn trong thư viện của sklearn.
# Để sử dụng nó các bạn cần import vào như ở dưới:

from sklearn.datasets import load_iris
iris_dataset = load_iris()

# trong đó mỗi hàng là một bông hoa Iris với các đặc trưng của nó.
print(iris_dataset.data) # hiển thị toàn bộ dữ liệu của tập Iris dataset

# hiển thị nhãn (label) của từng mẫu dữ liệu
print(iris_dataset.target)

print(len(iris_dataset.target))