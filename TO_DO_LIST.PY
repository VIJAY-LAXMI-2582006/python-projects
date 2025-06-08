#make to do list....
to_list=[]
while True:
    print("TO_DO_LIST")
    print("1:add work")
    print("2: show list")
    print("3: delete work")
    print("4: exit... ")
    print("----------------------------")
    #entering choice..
    a=input("enter your choice(1/2/3/4): ")
    #adding new task..
    if a =="1":
        # asking user to enter number of task want to save..
        b=int(input("enter number of works you want to add: "))
        print("-------------------------------------")
        for j in range(b):
            # adding task..
            l=to_list.append(input("enter your task: "))
        print("work has been added to your list..")
        print("--------------------------------")
    # showing task ....
    elif a=="2":
        if to_list:
            print("your list:")
            print("-----------------")
            for i in range(len(to_list)):
                print("[]",i+1,to_list[i])
        else:
            print("your list in empty...add something to it: ")
        print("-------------------")
    #deleting a task  
    elif a=="3":
        print("select which work you want to delete from your following list..")
        for i in range(len(to_list)):
            print("[]",i+1,to_list[i])
        print("--------------------------------")
            # asking user to enter number of task want to delete...
        c=int(input("enter number of works you want to delete: "))
        print("--------------------------------")
        for k in range(c):
            # deleting tasks...
            to_list.remove(input("enter the work want to dlete: "))
        # showing final list..
        print("your final list: ")
        for i in range(len(to_list)):
                print("[]",i+1,to_list[i])
        print("--------------------------------")
    #exit...
    elif a=="4":
        print("exit....")
        print("--------------------------------")
    #invalid choice..
    else:
        print("invalid choice...")
        print("--------------------------------")
    
