# # help
# start - to start the car
# stop - to stop the car
# quit - to exit

# asd
# I don
#  't understand that
#     start
#     Car started...Ready to go!
# stop
# Car stopped.
# quit

cmd = ""
started = False
while True:
    cmd = input("> ").lower()
    if cmd == "start":
        if started:
            print("Car is already started!")
        else:
            started = True

            print("Car started...")
    elif cmd == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif cmd == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif cmd == "quit":
        break
    else:
        print("Sorry, I don't understand that!")
