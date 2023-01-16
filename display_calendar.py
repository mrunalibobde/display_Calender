import calendar
def calu():
    yy=int(input("enter the year: "))
    mm=int(input("enter the month: "))
    while yy!=0 or mm!=0:
        print(calendar.month(yy,mm))
        yy=int(input("you can try again.... enter the year: "))
        mm=int(input("you can try again.... enter the month: "))
calu()


