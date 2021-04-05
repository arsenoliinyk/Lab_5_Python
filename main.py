import re

if __name__ == "__main__":
    #1st method
    count = 0
    file = "D:\\PyCharm programs\\Lab_5\\access_log"

    regex = r'\[(0(8\/Mar\/2004)' \
            r'\:((0(7\:((1((1\:3[7-9])|([2-9]\:[0-5][0-9])))|' \
            r'([2-5][0-9]\:[0-5][0-9])))|' \
            r'([8-9]\:[0-5][0-9]\:[0-5][0-9]))|' \
            r'(1[0-9]\:[0-5][0-9]\:[0-5][0-9])|(2[0-3]\:[0-5][0-9]\:[0-5][0-9])))|' \
            r'(9\/Mar\/2004' \
            r'\:(([0-1][0-9]\:[0-5][0-9]\:[0-5][0-9])|' \
            r'(2[0-3]\:[0-5][0-9]\:[0-5][0-9])))|' \
            r'((10\/Mar\/2004)' \
            r'\:((0[0-9]\:[0-5][0-9]\:[0-5][0-9])|' \
            r'(1((0\:[0-5][0-9]\:[0-5][0-9])' \
            r'|(1\:(([0-3][0-9]\:[0-5][0-9]\:[0-5][0-9])|(4((0\:[0-5][0-9])|(1(([0-4][0-9])|(5[0-2])))))))))))' \
            r'\ -0800] ".*" 200' \

    with open(file, "r") as file:
        for line in file:
            for searched_number in re.finditer(regex, line):
                count += 1

    file.close()
    print("1) Successful number of requests = ", count)

    #2nd method
    regex_start = b'08/Mar/2004:07:11:37'
    regex_end = b'10/Mar/2004:11:41:52'
    CODE_STATUS = b'200'
    needed_time = False
    line_counter = 0

    file = open("D:\\PyCharm programs\\Lab_5\\access_log", 'rb')

    for line in file.readlines():
        if regex_end in line:
            needed_time = False
            break
        if regex_start in line:
            needed_time = True
        if needed_time and CODE_STATUS in line:
            line_counter += 1

    file.close()
    print("2) Successful number of requests = ", line_counter)

