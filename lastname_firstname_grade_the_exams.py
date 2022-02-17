#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Tạo hàm mở file:
try:
    file = open(input("Nhập tên lớp: "), "r")
    mark_table = file.readlines()
    print("Mở thành công")
except:
    print("Không tồn tại lớp này, mời nhập lại theo cú pháp classx.txt")
    
# Báo cáo tổng số dòng được lưu trữ trong tệp:
print("Tổng số dòng dữ liệu được lưu trữ: ",len(mark_table))

# Phân tích từng dòng và đảm bảo nó là hợp lệ:
valid_mark_table = []
valid_line_num = 0
invalid_line_num = 0
for line in mark_table:
    x = line.strip().split(",")
    if len(x) == 26:
        if x[0].startswith("N") is True and x[0][1:].isdigit() is True and len(x[0]) == 9:
            valid_line_num += 1
            valid_mark_table.append(line)
        else:
            invalid_line_num += 1
            print("Dòng chứa mã học sinh không hợp lệ:\n", line)                
    else:
        if x[0].startswith("N") is True and x[0][1:].isdigit() is True and len(x[0]) == 9:
            invalid_line_num += 1
            print("Dòng có số kí tự không hợp lệ:\n", line)
        else:
            invalid_line_num += 1
            print("Dòng chứa có số kí tự không hợp lệ và mã học sinh không hợp lệ:\n", line)  
print("Tổng số dòng hợp lệ: ", valid_line_num)
print("Tổng số dòng không hợp lệ: ", invalid_line_num)

# Đáp án đúng bài thi:
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(",")

# Tạo danh sách điểm tương ứng với từng câu trả lời:
scores = []
for line in valid_mark_table:
    x = line.strip().split(",")
    for i in range(len(x) - 1):
        if x[i + 1] == answer_key[i]:
            x[i + 1] = 4
        elif x[i + 1] == '':
            x[i + 1] = 0
        else:
            x[i + 1] = -1
    scores.append(x[1:])
    
# Tính tổng điểm cho từng học sinh:
total = []
for line in scores:
    total.append(sum(line))
    
# Thống kê điểm của lớp:  
sorted_total = sorted(total)
max_score = max(total)
min_score = min(total)
mean_score = sum(total)/len(total)
range_of_score = max(total) - min(total)
y = len(sorted_total)
if y % 2 == 0:
    meadian_score = (sorted_total[int(y/2)] + sorted_total[int(y/2 + 1)])/2
else:
    meadian_score = sorted_total[int(y//2 + 1)]
print("Điểm trung bình của lớp: ", mean_score,
        "\nĐiểm trung vị của lớp: ", meadian_score,
        "\nĐiểm cao nhất của lớp: ", max_score,
        "\nĐiểm thấp nhất của lớp: ", min_score,
        "\nKhoảng điểm của lớp: ", range_of_score)

# Tạo bảng điểm:
name_id = []
for line in valid_mark_table:
    x = line.strip().split(",")
    name_id.append(x[0])
score_table = []
for i in range(len(name_id)):
    score_table.append(name_id[i] + "," + str(total[i]) + "\n")
    
# Xuất file
grade_file = input("Tên file cần xuất: ")
with open(grade_file, "w") as writefile:
    for line in score_table:
        writefile.write(line)


# In[ ]:




