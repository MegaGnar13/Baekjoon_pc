def is_valid(st_list, SN):
    for st in st_list:
        if st['SN'] == SN:
            return True
    return False


def insert(st_list, student):
    if not (is_valid(st_list, student['SN'])):
        st_list.append(student)
        print(student)
    else:
        print('[ERROR!!!] There is a student with the same SN.')


def modify_major(st_list, modi_SN, modi_major):
    if is_valid(st_list, modi_SN):
        for st in st_list:
            if st['SN']==modi_SN:
                st['major']=modi_major
                print(st)
    else:
        print(f'[ERROR!!!] There is no student with SN {modi_SN}')


def delete(st_list, del_SN):
    cnt=0
    for st in st_list:
        if st['SN']==del_SN:
            st_list.remove(st)
            cnt+=1
    if cnt==0:
        print("[ERROR!!!] There is no student with SN",del_SN)
    else:
        print(st_list)


def manage_students(st_list):
    option = int(input('[1] Insert \t [2] Modify \t [3] Delete \t [0] Exit: '))
    while option != 0:
        if option ==1:
            S_num=int(input('[Insert] Student number: '))
            S_name=input('[Insert] Name: ')
            S_major=input('[Insert] Major: ')
            stu={}

            stu['SN']=S_num
            stu['name']=S_name
            stu['major']=S_major

            insert(st_list,stu)
            option = int(input('[1] Insert \t [2] Modify \t [3] Delete \t [0] Exit: '))

        elif option == 2:
            S_num=int(input('[Modify] Student number: '))
            S_major=input('[Modify] Major: ')

            modify_major(st_list,S_num,S_major)
            option = int(input('[1] Insert \t [2] Modify \t [3] Delete \t [0] Exit: '))
        elif option == 3:
            S_num = int(input('[Delete] Student number: '))
            delete(st_list,S_num)
            option = int(input('[1] Insert \t [2] Modify \t [3] Delete \t [0] Exit: '))
        else:
            print("Invalid value")
            option = int(input('[1] Insert \t [2] Modify \t [3] Delete \t [0] Exit: '))
    else:
        print(st_list)

    # Don't delete the code below


if __name__ == '__main__':
    s1 = {'SN': 1234, 'name': 'Kim', 'major': 'Computer'}
    s2 = {'SN': 5678, 'name': 'Yoon', 'major': 'Robot'}
    s3 = {'SN': 1004, 'name': 'Lee', 'major': 'English'}
    s4 = {'SN': 8282, 'name': 'Park', 'major': 'Math'}
    students = [s1, s2, s3, s4]

    manage_students(students)