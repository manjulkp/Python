contacts = {
    'number' : 4 ,
    'students' : 
        [
            {'name' : 'manjulakp1' , 'email' : "manjulakp1@gmail.com"} ,
            {'name' : 'manjulakp2' , 'email' : "manjulakp2@gmail.com"} ,
            {'name' : 'manjulakp3' , 'email' : "manjulakp3@gmail.com"}
        ]
}

for each_student in contacts.get('students'):
    print(each_student['name'])