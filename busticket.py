print("---------------------------------------------------------------\n")
print("Bus Ticketing System\n")

seats = 80

BusSeats = { "row1" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row2" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row3" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row4" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row5" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row6" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row7" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row8" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row9" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row10" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row11" : { 1 : "| |" , 2 : "| |", 3 : "| |", 4 : "| |", 5 : "| |", 6 : "| |", 7 : "| |" },
             "row12" : { 1 : "| |" , 2 : "| |", 3 : "| |" } }



def reservation():
    global seats
    booking = 0
    while booking < 1 and seats != 0:
        print("---------------------------------------------------------------")
        booking = int(input("\nEnter the Number of Seats to reserve ( -1 to exit ): "))
        print("")
        if booking == -1:
            break
        if booking > 7:
            print("Sorry, You cannot reserve more than 7 seats at a time!\n")
            booking = 0
            continue
        if SeatsAvailability(booking):
            booking = 0
        else:
            break

def SeatsAvailability(NumOfSeats):
    global seats

    if ((seats - NumOfSeats) > 0) or ((seats - NumOfSeats) == 0):
        seats = seats - NumOfSeats
        SeatsAllocation(NumOfSeats)
        print("\nBooking Successfull!")
        print("\nAvailable Seats = " + str(seats))
        return True
    else:
        print("Seats are not available!")
        return False

def SeatsAllocation(booking):

    global BusSeats

    for key,value in BusSeats.items():
        RSval = ReserveCount(value)

        if ( booking <= ((RSval - 7) * (-1))) or (RSval == 0):
            for reserver in range(booking):
                BusSeats[key][reserver+RSval+1] = "|R|"
                Ticket(key,reserver+RSval+1)
            break

    print("")
    for row in BusSeats.values():
        for seat in row.values():
            print(seat, end=" ")
        print("")

def ReserveCount(row):
    global BusSeats
    count = 0

    for seat in row.values():
        if seat == "|R|":
            count +=1
    return count

def Ticket(row,seat):
    r = int(row[3:])
    place = (r * 7) - ( 7 - seat)

    print ("SEAT NUMBER: " + str(place) + " is allocated!" )


reservation()

print("\nNumber of Seats: " + str(seats))
