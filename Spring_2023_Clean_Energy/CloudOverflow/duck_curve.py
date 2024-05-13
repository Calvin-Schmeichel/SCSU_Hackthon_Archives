      #           .----.
      #.---------. | == |
      #|.-"""""-.| |----|
      #||       || | == |
      #||       || |----| Team: Cloud Overflow (Hackathon 2023)
      #|'-.....-'| |::::|   main editor: Brendan Chermack
      #`"")---(""` |___.|
     #/:::::::::::\" _  "
    #/:::=======:::\`\`\
 #`"""""""""""""`  '-'
import csv
from HouseClass import House

main_output = []

#accesses the csv file data (meaning the power grids data and from that we are going to calc total load and generation)
with open('mock_data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile)
##power state function##
def power_state(): # decides the appropriate action during specific times of the day following the duck curve
    with open('mock_data.csv', newline = '') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) > 0:
                hr = row[0]
            if ((int(hr)) < 8):
                print ((int(hr)), "can discharge")
                main_output.append([(int(hr)), "can discharge"])
            elif((int(hr)) >= 18):
                print ((int(hr)), "can discharge")
                main_output.append([(int(hr)), "can discharge"])
            elif((9) <= int(hr) < (17)):
                print ((int(hr)), "can charge")
                main_output.append([(int(hr)), "can charge"])
            elif((8) <= int(hr) < (9)):
                print ((int(hr)), "idling")
                main_output.append([(int(hr)), "idling"])
            elif((17) <= int(hr) < (18)):
                print ((int(hr)), "idling")
                main_output.append([(int(hr)), "idling"])
def can_sell_power(): #During the hr 6pm to early morning power can be sold to the grid reads from the csv file
    end_flag = False
    with open('mock_data.csv', newline = '') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) >= 1:
                megawatt = row[1] #this will get the power grids megawattage the 22000 is when we want a house to sell to the grid
                if((float(megawatt)) >= 22000):
                    end_flag = True
    return end_flag

def main():#main
    exHouse = House()#creates a house object
    if(exHouse.HomeOwnersLimit >= exHouse.CurrentChargeStatusPercentage):# as long as the the min charge limit is less than the charge percentage it will check if power can be discharged and then sold
        if(power_state()):
            print(can_sell_power())
    power_state()
    """randHouse = House()#creates a house object
    randHouse.HouseDataShuffle()#randomizes the data for the house
    print(randHouse.HomeOwnersLimit)
    print(randHouse.CurrentChargeStatusPercentage)
    if(randHouse.HomeOwnersLimit <= randHouse.CurrentChargeStatusPercentage):
        if((can_discharge())):
            print(can_sell_power())""" 
    #print(main_output)

    #return main_output
main()
