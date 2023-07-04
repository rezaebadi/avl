
class Student(object):
    def __init__(self, firstName , lastName , fatherName , birthday , nationalCode , id , phone ,mobileNumber , address):
        self.firstName=firstName
        self.lastName=lastName
        self.fatherName=fatherName
        self.birthday=birthday
        self.nationalCode=nationalCode
        self.id=id
        self.phone=phone
        self.mobileNumber=mobileNumber
        self.address=address
        self.l = None
        self.r = None
        self.h = 1


class AVLTree(object):
    global root
    def insert(self, root,key):
        if not root:
            return key
        elif key.nationalCode < root.nationalCode:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)

        root.h = 1 + max(self.getHeight(root.l),
                         self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and key.nationalCode < root.l.nationalCode:
            return self.rRotate(root)

        if b < -1 and key.nationalCode > root.r.nationalCode:
            return self.lRotate(root)

        if b > 1 and key.nationalCode > root.l.nationalCode:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key.nationalCode < root.r.nationalCode:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def lRotate(self, node):

        node_right = node.r
        left_of_node_right = node_right.l

        node_right.l = node
        node.r = left_of_node_right

        node.h = 1 + max(self.getHeight(node.l),
                         self.getHeight(node.r))
        node_right.h = 1 + max(self.getHeight(node_right.l),
                      self.getHeight(node_right.r))

        return node_right

    def rRotate(self, node):

        node_left = node.l
        right_of_node_left = node_left.r

        node_left.r = node
        node.l = right_of_node_left

        node.h = 1 + max(self.getHeight(node.l),
                         self.getHeight(node.r))
        node_left.h = 1 + max(self.getHeight(node_left.l),
                      self.getHeight(node_left.r))

        return node_left

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def printOneStudent(self,node):
        print(node.firstName+" "+node.lastName+"\nfather:"+node.fatherName+"\nnational code:"+node.nationalCode,"\nID:",node.id,"\nbirthday:",node.birthday,
              "\nphone:",node.phone,"\nmobile number:",node.mobileNumber,"\naddress:",node.address)

    def preOrder(self, root):

        if not root:
            return

        print(self.printOneStudent(root))
        self.preOrder(root.l)
        self.preOrder(root.r)


    def inOrder(self, root):

        if not root:
            return

        self.preOrder(root.l)
        print(self.printOneStudent(root))
        self.preOrder(root.r)

    def search(self,root,code):
        while(root != None):
            if(root.nationalCode==code):
                return root
            elif(code<root.nationalCode):
                root=root.l
            elif(code>root.nationalCode):
                root=root.r
        return None

    def save(self, root, save_file):
        if not root:
            return
        save_file.write(root.firstName + "\n")
        save_file.write(root.lastName + "\n")
        save_file.write(root.fatherName + "\n")
        save_file.write(root.birthday + "\n")
        save_file.write(root.nationalCode + "\n")
        save_file.write(root.id + "\n")
        save_file.write(root.mobileNumber + "\n")
        save_file.write(root.phone + "\n")
        save_file.write(root.address + "\n")
        self.save(root.l, save_file)
        self.save(root.r, save_file)

    def edit(self,root,code):
        continue3="y"
        while(continue3!="n"):
            self.printOneStudent(self.search(root, code))
            changeKey = input("which part do you want change?\n1.first name\n2.last name \n3.father name\n4.birthday\n"
                              "5.id\n6.phone\n7.mobile number\n8.address\n")

            if (changeKey == "1" or changeKey == "first name"):
                while (True):
                    new_first_name = input("enter new first name:\n")
                    try:
                        str(new_first_name)
                    except:
                        print("enter string values")
                        continue
                    if (len(new_first_name) < 2):
                        print("The number of digits is small")
                        continue
                    break
                self.search(root, code).firstName = new_first_name

            if (changeKey == "2" or changeKey == "last name"):
                while (True):
                    new_last_name = input("enter new last name:\n")
                    try:
                        str(new_last_name)
                    except:
                        print("enter string values")
                        continue
                    if (len(new_last_name) < 2):
                        print("The number of digits is small")
                        continue
                    break
                self.search(root, code).lastName = new_last_name

            if (changeKey == "3" or changeKey == "father name"):
                while (True):
                    new_father_name = input("enter new father name:\n")
                    try:
                        str(new_father_name)
                    except:
                        print("enter string values")
                        continue
                    if (len(new_father_name) < 2):
                        print("The number of digits is small")
                        continue
                    break
                self.search(root, code).fatherName = new_father_name

            if (changeKey == "4" or changeKey == "birthday"):
                while (True):
                    print("please enter by form 13**/**/**")
                    new_birthday = input("enter new birthday:\n")
                    try:
                        str(new_birthday)
                    except:
                        print("enter integer values")
                        continue
                    if (new_birthday[0] != "1" or new_birthday[1] != "3" or new_birthday[4] != "/" or new_birthday[7] != "/"):
                        print("please enter valid value")
                        continue
                    if ((new_birthday[5] == "1" and new_birthday[6] > "2") or new_birthday[5] > "2"):
                        print("please enter correct value for month")
                        continue
                    if (new_birthday[8] > "3" or (new_birthday[8] == "3" and new_birthday[9] > "1")):
                        print("please enter correct value for day")
                        continue
                    break
                self.search(root, code).birthday = new_birthday

            if (changeKey == "5" or changeKey == "id"):
                while (True):
                    new_id = input("enter new id\n:")
                    try:
                        int(new_id)
                    except:
                        print("enter integer values")
                        continue
                    if (len(new_id) > 3 or len(new_id) < 0):
                        print("please enter valid value")
                        continue
                    break
                self.search(root, code).id = new_id

            if (changeKey == "6" or changeKey == "phone"):
                while (True):
                    new_phone = input("enter new number:\n")
                    try:
                        int(new_phone)
                    except:
                        print("enter just integer values")
                        continue
                    if (len(new_phone) > 8 or len(new_phone) < 0):
                        print("please enter valid value")
                        continue
                    break
                self.search(root, code).phone = new_phone

            if (changeKey == "7" or changeKey == "mobile number"):
                while (True):
                    new_mobile_number = input("enter new mobile number:\n")
                    try:
                        int(new_mobile_number)
                    except:
                        print("enter just integer values")
                        continue
                    if (len(new_mobile_number) != 11):
                        print("The number of digits is small")
                        continue
                    if (new_mobile_number[0] != "0" or new_mobile_number[1] != "9"):
                        print("the mobile number is not correct!")
                        continue
                    break
                self.search(root, code).mobileNumber = new_mobile_number

            if (changeKey == "8" or changeKey == "adress"):
                while (True):
                    new_address = input("enter new address:\n")
                    try:
                        str(new_address)
                    except:
                        print("enter just integer values")
                        continue
                    break
                self.search(root, code).address = new_address
            continue3=(input("do you want edit another field?\ny or n:\n") or "n")


students=[]#include all studnets national code
Tree = AVLTree()
root = None

def check_code(code):
    for i in students:
        if (code == i):
            return True

def addStudent():
    global Tree
    global root
    while(True):
        firstName = input("firstname:\n")
        try:
            str(firstName)
        except:
            print("enter string values")
            continue
        if(len(firstName)<2):
            print("The number of digits is small")
            continue
        break

    while(True):
        lastName = input("lastname:\n")
        try:
            str(lastName)
        except:
            print("enter string values")
            continue
        if(len(lastName)<2):
            print("The number of digits is small")
            continue
        break

    while(True):
        fatherName = input("fathername:\n")
        try:
            str(fatherName)
        except:
            print("enter string values")
            continue
        if(len(fatherName)<2):
            print("The number of digits is small")
            continue
        break


    while(True):
        print("please enter by form 13**/**/**")
        birthday = input("birthday:\n")
        try:
            str(birthday)
        except:
            print("enter integer values")
            continue
        if (birthday[0]!="1" or birthday[1]!="3" or birthday[4]!="/" or birthday[7]!="/"):
            print("please enter valid value")
            continue
        if((birthday[5]=="1" and birthday[6]>"2") or birthday[5]>"2"):
            print("please enter correct value for month")
            continue
        if(birthday[8]>"3" or (birthday[8]=="3" and birthday[9]>"1")):
            print("please enter correct value for day")
            continue
        break

    while(True):
        nationalCode = input("nationcode:\n")
        try:
            int(nationalCode)
        except:
            print("enter integer values")
            continue
        if (len(nationalCode) != 10):
            print("please enter valid value")
            continue
        if(check_code(nationalCode)):
            print("your national code is wrong")
            continue
        break

    students.append(nationalCode)


    while(True):
        id = input("id:\nif you don't have id please enter 0\n")
        try:
            int(id)
        except:
            print("enter integer values")
            continue
        if (len(id)>3 or len(id)<0 ):
            print("please enter valid value")
            continue
        break


    while(True):
        phone = input("phone:\n")
        try:
            int(phone)
        except:
            print("enter just integer values")
            continue
        if (len(phone)>8 or len(phone)<0 ):
            print("your phone number is wrong\n please correct it\n")
            continue
        break
    while(True):
        mobileNumber = input("mobile number:\n")
        try:
            int(mobileNumber)
        except:
            print("enter just integer values")
            continue
        if (len(mobileNumber)!=11):
            print("The number of digits is small")
            continue
        if(mobileNumber[0]!="0" or mobileNumber[1]!="9"):
            print("the mobile number is not correct!")
            continue
        break

    while(True):
        address = input("address:\n")
        try:
            str(address)
        except:
            print("enter just integer values")
            continue
        break

    temp = Student(firstName, lastName, fatherName, birthday, nationalCode, id, phone, mobileNumber, address)
    root = Tree.insert(root, temp)


#start
#read information from file
file=open('data.txt','r')
while(1):
    fname = file.readline().splitlines()
    if(fname.__len__()==0):
        break
    fname=fname[0]
    lname = file.readline().splitlines()[0]
    faname = file.readline().splitlines()[0]
    bd = file.readline().splitlines()[0]
    nc = file.readline().splitlines()[0]
    students.append(nc)
    id = file.readline().splitlines()[0]
    ph = file.readline().splitlines()[0]
    mo = file.readline().splitlines()[0]
    ad = file.readline().splitlines()[0]
    temp2=Student(fname, lname, faname, bd, nc, id, mo,ph , ad)
    root=Tree.insert(root,temp2)
file.close()


#the menue
print("HELLO,WELLCOME\n")
while(1):
    print("1.add new student\n2.edit student\n3.search student\n4.show information\n5.quit")
    choose = input("How can I do for you?please enter it\n")
    if (choose == "1" or choose == "add new student"):
        continue1 = "y"
        while (continue1 != "n"):
            addStudent()
            continue1 = input("do you want add another student?\ny or n:\n") or "n"


    if (choose == "2" or choose == "edit student"):
        code=input("please enter student's nation code that you want change it:\n")
        print(Tree.search(root,code) )
        if (Tree.search(root,code) == None):
            print("there isn't any student whit this nation code \n")
        else:
            Tree.edit(root,code)


    if (choose == "3" or choose == "search studemt"):
        continue2= "y"
        while(continue2 != "n"):
            wanted_code = input("please enter the national code:\n")
            if (Tree.search(root,wanted_code) == None):
                print("there isn't any student whit this nation code \n")
            else:
                Tree.printOneStudent(Tree.search(root, wanted_code))
            continue2=input("do you want search another student?\ny or n:\n")


    if (choose == "4" or choose == "show information"):
        print(f"number of all students is {len(students)}\n")
        Tree.inOrder(root)


    if (choose == "5" or choose == "quit"):
        file=open("data.txt","w")
        Tree.save(root,file)
        print("good bye!")
        file.close()
        exit()
