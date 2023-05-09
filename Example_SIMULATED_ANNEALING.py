import math
import random

def f(x):
    return x**2 - 5*x + 6

def anneal():
    # Khởi tạo giá trị x bằng cách chọn ngẫu nhiên trong khoảng [0, 5]
    x = random.uniform(0, 5)
    
    # Thiết lập các thông số ban đầu
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    
    while T > T_min:
        # Lặp lại nhiều lần trong mỗi vòng lặp
        for i in range(100):
            # Tìm kiếm một giá trị mới gần với giá trị hiện tại
            new_x = x + random.uniform(-0.1, 0.1) * T
            
            # Tính toán sự khác biệt giữa giá trị mới và giá trị hiện tại
            delta_e = f(new_x) - f(x)
            
            # Nếu giá trị mới tốt hơn, chấp nhận giá trị mới
            if delta_e < 0:
                x = new_x
            # Nếu giá trị mới tồi hơn, chấp nhận giá trị mới với xác suất nhất định
            #nếu delta_e > 0 trạng thái mới tốt hơn trạng thái hiện tại
            else:
                p = math.exp(-delta_e / T)
                #cho 1 cơ hội để trạng thái xấu hơn đc chấp nhận (e^Dekta_e/T)
                if random.uniform(0, 1) < p:
                    x = new_x
        
        # Giảm nhiệt độ
        T *= alpha
    
    return x

# Chạy thuật toán Simulated Annealing và hiển thị kết quả
x_min = anneal()
print("Giá trị nhỏ nhất của hàm số f(x) là:", f(x_min))
print("Giá trị x tương ứng là:", x_min)