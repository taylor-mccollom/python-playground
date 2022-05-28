# create a class roster that is able to  list whether a student
# is present or not, and then to return the list of students in attendance
roster_list = ['Jacob', 'Daniel', 'Phteven', 'Jackie',
               'Kelly', 'Charles', 'Gregg', 'Jeffrey']

# Iterate over list and ask for a response of present or absent
# if present append to a list

def present_or_not(roster):
    attendance = []
    absent = []
    for student in roster:

        x = input(f'Is {student} absent or present? -')
        while x.lower() not in ('absent', 'present'):
            print('That is not a valid entry.')
            x = input(f'Is {student} absent or present? -')

        if x.lower() == 'present':
            print(f'{student} is present.')
            attendance.append(student)
        else:
            print(f'{student} is absent')
            absent.append(student)

    print(f'{attendance} are all in attendance.')
    print(f'{absent} are all absent.')
present_or_not(roster_list)
