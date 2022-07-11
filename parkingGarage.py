# Start Your Code here

class parkingGarage():
    
    # updated to intialize w/o any parameters- the parking spaces/tickets are a set number
    def __init__(self):
        self.tickets = [20]
        self.parkingSpaces = [20]
        self.currentTicket = {'paid' : False}
        self.bank = []
        
        
        pass

    def takeTicket(self):
        pass

    def payForParking(self):
        pass

    def leaveGarage(self):
        # if paid- we let them loose and reset
        if self.currentTicket == True:
            self.currentTicket = False
            print('Thank You, Have a wonderful life!')
        # Else we're gonna get that money
        elif self.currentTicket == False:
            x = input('Gimme all your money, how much you got???')
            if isinstance(x, int):
                self.currentTicket['paid'] = False
                self.parkingSpaces += 1
                self.tickets += 1
                self.bank += x
                print('That works, have a great day!')
            else:
                # Just trying to have some fun with error handling
                y = input("Don't make me bust a kneecap, give me a number. . . ")
                self.currentTicket['paid'] = False
                self.parkingSpaces += 1
                self.tickets += 1
                self.bank += y
                print('That works, have a great day!')


