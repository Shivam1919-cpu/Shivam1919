time=int(input("give me timeaccording to 24 hr format"))
if (time>5 and time<=11):
    print("good morning")
elif(time>14 and time<=16):
    print("good afternoon")
elif(time>17 and time<=21):
    print("good evening")
elif(time>22 and time<=4):
    print("good night")
else:
    print("nothing")