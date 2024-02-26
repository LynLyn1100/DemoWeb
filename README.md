# Django e-commerce

Một ứng dụng thương mại điện tử (web bán hàng đơn giản) được tạo bằng Django 3, SQLite và Bootstrap 4.

Ứng dụng này cũng sử dụng một số packages phần mềm khác như:

- django-crispy-forms
- django-filter
- pillow
- easy-thumbnails
- dj-database-url

Trong ứng dụng này, quản trị viên có thể quản lý sản phẩm và đơn hàng, và khách hàng có thể đăng ký, thêm sản phẩm vào giỏ hàng và sau đó đặt hàng. Khách hàng cũng có thể tạo hóa đơn cho đơn hàng của mình.

Để chạy ứng dụng này trên máy cục bộ của bạn, bạn có thể làm theo các hướng dẫn dưới đây.

Để cài đặt các phụ thuộc, bạn có thể chạy lệnh:

```shell
pip install -r requirements.txt
```

Để tạo các tập tin migrations :

```shell
python manage.py makemigrations
```

Để áp dụng các tập tin migrations đó vào cơ sở dữ liệu thực tế:

```shell
python manage.py migrate
```

Để run server :

```shell
python manage.py runserver
```

Sau khi khởi động máy chủ, hãy mở trình duyệt web của bạn và truy cập vào địa chỉ http://localhost:8000/store để truy cập vào giao diện của ứng dụng cửa hàng. Để truy cập vào module quản trị viên, hãy truy cập vào địa chỉ http://localhost:8000/admin và đăng nhập bằng thông tin đăng nhập của superuser.