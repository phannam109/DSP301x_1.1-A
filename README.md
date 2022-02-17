# DSP301x_1.1-A
Giới thiệu về Khoa học dữ liệu
# HƯỚNG DẪN HOÀN THÀNH DỰ ÁN
## Task 1: Nhập dữ liệu của tệp
1. Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)
2. Viết một chương trình cho phép người dùng nhập tên của một tệp. 
Sử dụng try/except để mở tệp được cung cấp để truy cập đọc. Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ:
try:
    file = open(input("Nhập tên lớp: "), "r")
    mark_table = file.readlines()
    print("Mở thành công")
except:
    print("Không tồn tại lớp này, mời nhập lại theo cú pháp classx.txt")
