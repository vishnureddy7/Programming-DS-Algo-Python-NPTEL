#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs08/progassignment?action=submit&name=109

import sys

def sort_key(checkout):
    key = list(map(int,checkout[1].split('-')));
    key.append(borrowers[checkout[0][0]]);
    key.append(checkout[0][1]);
    return tuple(key);

current = 'Books';
books = dict();
borrowers = dict();
checkouts = dict();
while(True):
    line = input();
    if(line == 'Books'):
        current = 'Books';
        continue;
    elif(line == 'Borrowers'):
        current = 'Borrowers'
        continue;
    elif(line == 'Checkouts'):
        current = 'Checkouts';
        continue;
    elif(line == 'EndOfInput'):
        break;
    elif(current == 'Books'):
        acc_no,title = line.split('~');
        books[acc_no] = title;
    elif(current == 'Borrowers'):
        usr,name = line.split('~');
        borrowers[usr] = name;
    elif(current == 'Checkouts'):
        usr,acc_no,due_date = line.split('~');
        checkouts[(usr,acc_no)] = due_date;

checkouts = sorted(checkouts.items(), key=sort_key);

for checkout in checkouts:
    line = checkout[1]+'~'+borrowers[checkout[0][0]]+'~'+\
           checkout[0][1]+'~'+books[checkout[0][1]]
    print(line);
