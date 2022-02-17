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

Sử dụng hàm len() để đếm được số dòng dữ liệu:

_Tổng số dòng dữ liệu được lưu trữ:  20_

2. Phân tích từng dòng và đảm bảo nó hợp lệ:

Sử dụng hàm `len()` để xác định số kí tự hợp lệ của từng dòng là 26 và của mã sinh viên là 9 kí tự.

Sử dụng hàm `str.startswith("N") để xác định kí tự đầu tiên của mã sinh viên là "N"

Sử dụng hàm 'str.isdigit()` để xác định giá trị đấy là số (TRUE) hay chuỗi kí tự (FALSE)

Sử dụng vòng lặp `for` cùng điều kiện `if / else` để kiểm tra các dòng và tìm kiếm không hợp lệ.

Bỏ dữ liệu không hợp lệ và lưu lại dữ liệu hợp lể để sử dụng cho thống kê sau này.

Kết quả đạt được theo dạng sau:

> Dòng có số kí tự không hợp lệ:

 N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A

Dòng chứa mã học sinh không hợp lệ:

 N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D

Dòng chứa mã học sinh không hợp lệ:

 NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D

Dòng có số kí tự không hợp lệ:

 N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A

Tổng số dòng hợp lệ:  21

Tổng số dòng không hợp lệ:  4

