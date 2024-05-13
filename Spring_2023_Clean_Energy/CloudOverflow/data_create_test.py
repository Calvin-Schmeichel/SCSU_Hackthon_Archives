
      #           .----.
      #.---------. | == |
      #|.-"""""-.| |----|
      #||       || | == |
      #||       || |----|
      #|'-.....-'| |::::|
      #`"")---(""` |___.|
     #/:::::::::::\" _  "
    #/:::=======:::\`\`\
 #`"""""""""""""`  '-'
"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀
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
import random
import time
import csv
import datetime

#mock data is 24 hours, spaced out by one minute of approximate duck curve megawatts
filename = 'mock_data.csv'
#Fields are time in minuites from midnight ad megawatts in the grid
fields = ['Time','MW_MegaWatts']
 
def create_list_from_csv(filename):
    chat_context_list = []
    # read csv file and save to a list that can readily be used by python
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            chat_context_list.append(row)
    return chat_context_list

def write_to_csv(a_list, filename):
    chat_context_list = create_list_from_csv(filename)
    # writing changed list of dictionaries to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # writing headers (field names)
        writer.writeheader()
        # writing data rows
        writer.writerows(a_list)
    #return true false depending if was able to write to file or not, could also just not return anything if feeling like being lazy

#Time starts at 0 munutes from midnight
Time = 0
#megawatts is the same until 8:30 am, starts out at 22000
MW_MegaWatts = 22000

#Originally a while 
while Time <= 24:
    """if Time%14.4 == 0:
        print(Time/144)"""
            
    
    chat_context_list = create_list_from_csv(filename)
    if 0 <= Time < 9:
        MW_MegaWatts = 22000
    elif 9 <= Time < 13:
        MW_MegaWatts -= 1512
    elif 13 <= Time < 18:
        MW_MegaWatts += 1836

        
        
    chat_context_list.append({'Time':Time, 'MW_MegaWatts':MW_MegaWatts})
    write_to_csv(chat_context_list, filename)
    #time.sleep(1)
    Time += 1
    