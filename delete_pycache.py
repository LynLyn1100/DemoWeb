import os
import shutil

def remove_pycache(directory):
    # Lặp qua tất cả các tệp và thư mục trong thư mục được chỉ định
    for root, dirs, files in os.walk(directory):
        # Kiểm tra xem có tệp tin `__pycache__` trong danh sách files không
        if "__pycache__" in dirs:
            # Tạo đường dẫn đầy đủ đến thư mục `__pycache__`
            pycache_dir = os.path.join(root, "__pycache__")
            # Xóa thư mục `__pycache__` và tất cả các tệp tin bên trong
            shutil.rmtree(pycache_dir)
            print(f"Deleted {pycache_dir}")

# Gọi hàm remove_pycache với đường dẫn đến thư mục mã nguồn của bạn
remove_pycache("/Github_DemoWeb")