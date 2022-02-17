# DSP301x_1.1-A
Giới thiệu về Khoa học dữ liệu
# HƯỚNG DẪN HOÀN THÀNH DỰ ÁN

## Task 1: Nhập dữ liệu của tệp

1. Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)

2. Viết một chương trình cho phép người dùng nhập tên của một tệp. 

Sử dụng `try/except` để mở tệp được cung cấp để truy cập đọc. 

Nếu tệp tồn tại, file sẽ được mở và bạn có thể in ra một thông báo xác nhận: _Mở thành công_

Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ: _Không tồn tại lớp này, mời nhập lại theo cú pháp classx.txt_

## Task 2: Đánh giá tính hợp lệ của dữ liệu sau khi nhập

Phân tích dữ liệu có trong tệp bạn mới mở để đảm bảo rằng nó đúng định dạng. Mỗi tệp dữ liệu chứa một loạt câu trả lời của học sinh ở định dạng sau:

_N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D_

hoặc:

_N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,_

Dữ liệu hợp lệ thỏa mãn các điều kiện sau:

- Tất cả các giá trị được phân tách bằng dấu phẩy.

- Giá trị đầu tiên là số ID của sinh viên: gồm 9 kí tự bắt đầu là "N" và tiếp theo là 8 kí tự số.

- 25 giá trị tiếp theo là 25 câu trả lời: một số dòng có thể bị hỏng do ít hoặc nhiều hơn câu trả lời là 25, một số câu trả lời có thể bị bỏ trống

1. Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp:

_Tổng số dòng dữ liệu được lưu trữ:  20_

2. Phân tích từng dòng và đảm bảo nó hợp lệ:

Sử dụng code `len` để xác định số kí tự hợp lệ của từng dòng là 26 và của mã học sinh là 9 kí tự.

