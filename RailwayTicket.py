class Account():
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def checkpassword(self,password):
      return self.password == password
    
class traininfo():
    def __init__(self,train_num,destination,avl_seats,source):
        self.train_num = train_num
        self.destination = destination
        self.avl_seats = avl_seats
        self.source = source

    def displayinfo(self):
        print("---------------")
        print(f"train_num:{self.train_num}")
        print(f"train_destination :{self.destination}")
        print(f"train_avl seats : {self.avl_seats}")
        print(f"train_source : {self.source}")       
        print("-----------------")

class Passenger():
    def __init__(self,p_name,p_age,p_mobile_number):
        self.p_name = p_name
        self.p_age = p_age
        self.p_mobile_number = p_mobile_number

    def  displayinfo(self):
        print("--------------")
        print(f"p_name:{self.p_name}")
        print(f"p_age:{self.p_age}")
        print(f"p_mobile_number : {self.p_mobile_number}")       
        print("-----------------")

        
accounts = []
loginaccount = None
while True:
    print("1.creat an account:\n 2.login")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        username = input("enter name")
        password = input("enter password")
        accounts.append(Account(username,password))
        print("Account created succesfully")
    elif choice == 2:
        username = input("enter username:")
        password = input("enter password:")    
        for i in accounts:
            if i.username == username and i.checkpassword(password):
              loginaccount = i
              print(f"{username}is login sussessfully")

            break
        if loginaccount is None:
            print("invalid username and password")
        else:
            print("login successfull")
            break
    else:
        print("enter valid details")
#if loginaccount is not None:
trains =[traininfo(123456,"hyd",130,"peddavaram"),
            traininfo(122556,"vij",150,"nandhigama")]



while True:
    user_input = input("Enter 1 to see Train Details , Enter 2 to Exit \n")
    if int(user_input) == 1:
        for train in trains:
           train.displayinfo()
        train_number = int(input("enter tarin Number:"))
        for i in range(len(trains)):
            if train_number == trains[i].train_num:
                print("Available ticket for this Train is:",trains[i].avl_seats)

                tickets = int(input("enter number of tickets to purchase:"))
                if  tickets <= trains[i].avl_seats:
                    passenger_name = input("Enter passenger name:")
                    passenger_age  = int(input("Enter your age:"))
                    passenger_number = int(input("enter your mobile number:"))

                    p = Passenger(passenger_name,passenger_age,passenger_number)
                    print(tickets,"have been booked :")
                    p.displayinfo()
                    trains[i].avl_seats = trains[i].avl_seats-tickets
                    print(trains[i].avl_seats,"availble seats")
                else:
                    print("sufficient tickets are not avilable:")

    elif int(user_input) == 2:
        break

    else:
        print("invalid input:")
        

            


                    





         

          
