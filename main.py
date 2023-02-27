import os

#size of BUFFER defined.
buffer=int(10)

#simaphore value initilized.
mutex=int(1)
full=int(0)
empty=int(10)
item=[]

#producer
def producer():
    global mutex, full,empty, item
    if mutex !=0 and full !=10:
        mutex-=1
        empty-=1
        item.append(input("enter the data item :- "))
        print(f"item-- {item} --will be produced.\n")
        full+=1
        mutex+=1
    else:
        print("buffer is FULL!\n")    

#consumer
def consumer():
    global mutex, full,empty, item
    if mutex !=0 and empty !=10:
        mutex-=1
        full-=1
        x=item.pop(0)
        print(f"item-- {x} --will be consumed.\n")
        empty+=1
        mutex+=1
    else:
        print("buffer is EMPTY!\n")    


#producer_consumer_ function_started.
print(".....producer_consumer_problem.....")
print(" 1.producer\n 2.consumer\n 3.exit\n")

#producer_consumer_loop
while True:

    try:
        choice=int(input("enter the choice(1,2,3) :- "))
        if choice == 1:
            producer()

        elif choice == 2:
            consumer()

        elif choice == 3:
            exit(0)  

        else:
            pass 

    except Exception as e:
        print(e)
        print("invalid choice!")

       








