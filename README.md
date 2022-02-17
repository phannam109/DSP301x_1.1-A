# DSP301x_1.1-A
Giới thiệu về Khoa học dữ liệu
# HƯỚNG DẪN HOÀN THÀNH DỰ ÁN

Một số biến đã được lưu trữ trong file python:

```
mark_table - Bảng lưu dữ liệu sau khi nhập file

valid_mark_table - Bảng chứa dữ liệu hợp lệ

answer_key - Đáp án đúng

scores - Danh sách điểm tương ứng với đáp án đúng

total - Danh sách tổng điểm

max_score - Điểm tối đa

min_score - Điểm thấp nhất

mean_score - Điểm trung bình

median_score - Giá trị trung vị

range_of_score - Khoảng điểm

name_id - danh sách mã sinh viên

score_table - bảng điểm 
```

## Task 1: Nhập dữ liệu của tệp

1. Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)

Các tệp dữ liệu là thông tin các câu trả lời của bài thi ở các lớp, lưu dưới định dạng _.txt_

```
N00000001,A,A,D,D,C,D,D,A,,C,D,B,C,,B,C,B,D,A,C,,A,,C,D
N00000002,,A,,D,,B,D,A,C,C,D,,A,A,A,C,B,D,C,C,A,A,B,,D
N00000003,B,A,,D,C,B,D,A,C,C,,B,A,B,A,C,B,D,A,,A,,B,D,D 
```

2. Viết một chương trình cho phép người dùng nhập tên của một tệp. 

Sử dụng `input()` để nhập tên dữ liệu mỗi lần chạy chương trình.

Sử dụng `try/except` để mở tệp được cung cấp để truy cập đọc. 

Nếu tệp tồn tại, file sẽ được mở và bạn có thể in ra một thông báo xác nhận: _Mở thành công_

Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ: _Không tồn tại lớp này, mời nhập lại theo cú pháp classx.txt_

## Task 2: Đánh giá tính hợp lệ của dữ liệu sau khi nhập

Phân tích dữ liệu có trong tệp bạn mới mở để đảm bảo rằng nó đúng định dạng. Mỗi tệp dữ liệu chứa một loạt câu trả lời của học sinh ở định dạng sau:

```N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D```

hoặc:

```N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,```

Dữ liệu hợp lệ thỏa mãn các điều kiện sau:

- Tất cả các giá trị được phân tách bằng dấu phẩy.

- Giá trị đầu tiên là số ID của sinh viên: gồm 9 kí tự bắt đầu là "N" và tiếp theo là 8 kí tự số.

- 25 giá trị tiếp theo là 25 câu trả lời: một số dòng có thể bị hỏng do ít hoặc nhiều hơn câu trả lời là 25, một số câu trả lời có thể bị bỏ trống

1. Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp:

Sử dụng hàm len() để đếm được số dòng dữ liệu:

```Tổng số dòng dữ liệu được lưu trữ:  20```

2. Phân tích từng dòng và đảm bảo nó hợp lệ:

Sử dụng hàm `len()` để xác định số kí tự hợp lệ của từng dòng là 26 và của mã sinh viên là 9 kí tự.

Sử dụng hàm `str.startswith("N")` để xác định kí tự đầu tiên của mã sinh viên là "N"

Sử dụng hàm `str.isdigit()` để xác định giá trị đấy là số (TRUE) hay chuỗi kí tự (FALSE)

Sử dụng vòng lặp `for` cùng điều kiện `if / else` để kiểm tra các dòng và tìm kiếm không hợp lệ.

Bỏ dữ liệu không hợp lệ và lưu lại dữ liệu hợp lể để sử dụng cho thống kê sau này.

Kết quả trả về có thể như sau:

```
Dòng có số kí tự không hợp lệ:
 N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A

Dòng chứa mã học sinh không hợp lệ:
 N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D

Dòng chứa mã học sinh không hợp lệ:
 NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D

Dòng có số kí tự không hợp lệ:
 N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A

Tổng số dòng hợp lệ:  21
Tổng số dòng không hợp lệ:  4
```

## Task 3: Chương trình chấm điểm bài thi

Đáp án đúng cho bài thị:

```answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"```

Tính điểm cho mỗi bài thi hợp lệ như sau:

- +4 điểm cho mỗi câu trả lời đúng
- 0 điểm cho mỗi câu trả lời bị bỏ qua
- -1 điểm cho mỗi câu trả lời sai

1. Tạo danh sách điểm thi tương ứng với các câu trả lời.

Sử dụng vòng lặp 'for' chạy qua từng dòng của dữ liệu để đối chiếu với đáp án, đưa ra điểm số tương ứng.

2. Tạo danh sách tổng điểm của các sinh viên trong mỗi lớp:

Sử dụng hàm `sum()` để tính tổng các giá trị trong mỗi dòng.

Sử dụng hàm `append()` để nhập các giá trị sau khi tính tổng vào danh sách điểm thi.

3. Thống kê điểm của lớp.

Sắp xếp danh sách điểm theo thứ tự tăng dần: dùng `sorted()` hoặc `sort()`

Điểm trung bình = Tổng điểm / Tổng số sinh viên

Giá trị trung vị = Giá trị ở giữa nếu số giá trị là số lẻ hoặc Trung bình 2 giá trị ở giữa nếu số giá trị là số chẵn.

Điểm cao nhất = Hàm `max()`.

Điểm thấp nhất = Hàm `min()`.

Miền giá trị của điểm = Điểm cao nhất - Điểm thấp nhất.

Kết quả ở dạng như sau: 

```
Điểm trung bình của lớp:  78.0 
Điểm trung vị của lớp:  76 
Điểm cao nhất của lớp:  100 
Điểm thấp nhất của lớp:  66 
Khoảng điểm của lớp:  34
```

## Task 4: Lưu trữ kết quả vào file

1. Tạo danh sách chứa thông tin mã sinh viên và điểm số tương ứng

Chạy vòng lặp qua từng dòng để lưu kết hợp mã sinh viên và điểm số tương ứng.

Danh sách trước khi lưu file ở dạng như sau:

```
'N00000021,68\n',
 'N00000022,76\n',
 'N00000024,73\n',
 ```
 
 2. Tạo file và lưu file kết quả.
 
 Sử dụng `input()` để nhập tên file cần xuất.
 
 Mờ file cần xuất ở mode "w" để có thể ghi lại với hàm `file.write`.
 
 File được lưu lại ở định dạng _.txt_ với nội dung ở dạng sau:
 
 ```
 N00000021,68
N00000022,76
N00000024,73
```

# Task 5: Sử dụng Pandas

