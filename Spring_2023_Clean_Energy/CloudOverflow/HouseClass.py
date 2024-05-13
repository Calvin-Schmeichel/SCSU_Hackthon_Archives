#Mannaged by Calvin Schmeichel | Cloud Overflow | Hackathon 2023
"""
                 ⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣤⣤⣤⣀⣀⠈⠋⠉⣁⣠⣤⣤⣤⣀⡀⠀⠀
⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀  
⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀
⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀
⠀⠀⠀⠈⠙⢿⣿⣿⣿⠿⠟⠛⠻⠿⣿⣿⣿⡿⠋⠀⠀⠀

"""

#We use the random library to add variation to the house data
import random

#We are using a class system to store data realated to a home
# This also allows us to easlly scale to a bigger simulation with more 
# randomly generated homes
class House:
    #We first define the variables for the class
    def __init__(self):
        
        #Total Charge Potential means the maximum charge the house can hold in Megawatts (MW)
        self.TotalChargePotential = 0.58677
        #Current Charge Status is the current house charge amount in Megawatts (MW)
        self.CurrentChargeStatus = 0.3293
        #Current Charge Status Percentage is the current house charge in percentage %
        self.CurrentChargeStatusPercentage = int(round(((self.CurrentChargeStatus)/(self.TotalChargePotential))*100, 0))

        #The Home Owners Limit is the floor of how much the owner is willing to send to the grid
        #from ~20 - ~80 EX: 20% means they are willing to send 80% of their total charges
        self.HomeOwnersLimit = 20

    #This is the sub-class function to shuffle the static house data from above.
    # You can keep it satic for testing and call shuffle to add variation in simulation testing.
    def HouseDataShuffle(self):
        #Here we are using the random.uniform function to choose new values within a small range (~15% variation)
        self.TotalChargePotential = round((random.uniform(0.5, 0.58677)),5)                                     
        self.CurrentChargeStatus = round((random.uniform(0, self.TotalChargePotential)),5)
        self.CurrentChargeStatusPercentage = int(round(((self.CurrentChargeStatus)/(self.TotalChargePotential))*100, 0))
        self.HomeOwnersLimit = int(round((random.uniform(20, 80)),0))

    
#Main here is just used for testing (:
"""
def main():

    
    print(round((random.uniform(0.5, 0.58677)),5))

    

    print("Hello")
    WhiteHouse = House()

    #static
    print("TotalChargePotential in megawhats: ", WhiteHouse.TotalChargePotential)
    print("The Current Charge status is: ", WhiteHouse.CurrentChargeStatus)
    print("The Current Charge Status Percentage is: ", WhiteHouse.CurrentChargeStatusPercentage)
    print("The Bottom acceptable limit charge percentage the owner has set is: ", WhiteHouse.HomeOwnersLimit)

    #randomizez TotalChargePotential, CurrentChargeStatus, and HomeOwnersLimit
    WhiteHouse.HouseDataShuffle()


    print(WhiteHouse.TotalChargePotential)
    print(WhiteHouse.CurrentChargeStatus)
    print(WhiteHouse.CurrentChargeStatusPercentage)
    print(WhiteHouse.HomeOwnersLimit)




#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()

"""






