import sys

base_case = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
n_list = []
input = sys.stdin.readline()
test_case_num = int(input)
for i in range(test_case_num):
    n_list.append(int(sys.stdin.readline())-1)
for i in range(test_case_num):
    print(base_case[n_list[i]])