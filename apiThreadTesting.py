#This pyhon function will test to see how the vsim can make an api call multiple times using a threading:
import json
import requests
import threading
from threading import Thread, Event
import os
import time
import random
from datetime import datetime
duration = time.perf_counter()

#Default location that each vehicle will be at
DEFAULT_LAT_STARTING = 30.390346000000008
DEFAULT_LONG_STARTING = -97.72559445767246
route_1 = [[-97.734955, 30.267914], [-97.736496, 30.268345], [-97.736839, 30.267427], [-97.734688, 30.266827], [-97.735077, 30.265757], [-97.735298, 30.264139], [-97.736923, 30.260164], [-97.737282, 30.257853], [-97.735046, 30.246187], [-97.735092, 30.24464], [-97.735664, 30.243183], [-97.742348, 30.231962], [-97.744484, 30.228928], [-97.747742, 30.22353], [-97.74897, 30.224411], [-97.75412, 30.226749], [-97.753044, 30.228733]]
route_2 = [[-97.711296, 30.348373], [-97.71151, 30.348476], [-97.709641, 30.35033], [-97.709167, 30.350809], [-97.710136, 30.35029], [-97.712341, 30.348577], [-97.712654, 30.348604], [-97.712715, 30.348749], [-97.714539, 30.353548], [-97.719604, 30.369637], [-97.740005, 30.381096], [-97.745453, 30.390524], [-97.746384, 30.393684], [-97.745003, 30.409201], [-97.747856, 30.422861], [-97.776642, 30.437927], [-97.788521, 30.445698], [-97.796989, 30.46892], [-97.804619, 30.484921], [-97.802254, 30.493267], [-97.804077, 30.498743], [-97.807228, 30.50198], [-97.811813, 30.503494], [-97.812706, 30.504841], [-97.82, 30.504711], [-97.831047, 30.500057], [-97.840248, 30.493916], [-97.844048, 30.497522], [-97.845604, 30.495325], [-97.846413, 30.495741], [-97.846786, 30.49514]]
route_3 = [[-97.745583, 30.271933], [-97.745239, 30.271835], [-97.747971, 30.264351], [-97.747711, 30.263622], [-97.749329, 30.259733], [-97.74353, 30.253229], [-97.736168, 30.248087], [-97.735779, 30.24799], [-97.735329, 30.245174], [-97.736061, 30.243069], [-97.736946, 30.241161], [-97.737152, 30.240694], [-97.742348, 30.231962], [-97.746643, 30.22471], [-97.750023, 30.219261], [-97.750626, 30.217573], [-97.749535, 30.216143], [-97.742958, 30.215986], [-97.710022, 30.212252], [-97.692719, 30.217714], [-97.684662, 30.221289], [-97.679741, 30.222427], [-97.675331, 30.22159], [-97.662727, 30.215014], [-97.660843, 30.213661], [-97.659782, 30.213104], [-97.659592, 30.212263], [-97.660645, 30.211428], [-97.662041, 30.211096], [-97.66259, 30.21151], [-97.665001, 30.209602], [-97.664764, 30.209044]]
vehicleID = "5e701c2eb15e7c5673d3f0b3"
vehicleID_2 = "5e7bdb2a93b142e5c8f1c123"
vehicleID_3 = "5e7bdb2c93b142e5c8f1c127"

# class MyThread(Thread):
#     def __init__(self, event):
#         Thread.__init__(self)
#         self.stopped = event

#     def run(self):
#         while not self.stopped.wait(0.5):
#             print("Thread is running..")
#             vehicleLocationExtractor(DEFAULT_COORDINATES_STRING)

# # #Running the threads:
# my_event = Event()
# thread = MyThread(my_event)
# thread.start()

# try:
#     while 1:
#         time.sleep(.1)
# except KeyboardInterrupt:
#     print ("attempting to close threads.")
#     my_event.clear()
#     #Finishing a threads:
#     thread.join()
#     print ("threads successfully closed")


# #Function to assign a status to a vehicle through a random selection
# def vehicleStatusExtractor():
#     availableStatus = ['IDLE', 'OTW', 'DONE', 'MAINT']
#     #To see how a dynamic vehicle status selection would work in this case
#     #The status will be chosen randomly for the purpose of testing. 
#     vehicleStatus = random.choice(availableStatus)
#     return vehicleStatus
    
#Function to send a vehicle status package to the server side 
def sendingVehicleHeartbeatStatus(vehicleID, route):
    # print("")
    # # Requesting to add all vehicle from the database into the local vsim.
    # API_Call = 'https://supply.team12.softwareengineeringii.com/api/backend?vehicle-all=1'
    # # print('\tThe API http string --> ' + API_Call)
    # print("")
    # #Vehicle information received from the server databse:
    # vehilce_info = requests.get(API_Call).json()
    # print("Current registered vehicle: ")
    # vID_Array = []
    # # print(vehilce_info)
    # #Array of vehicle ID:
    # for keys in range(len(vehilce_info)):
    #     vID = vehilce_info[keys]['_id']
    #     vID_Array.append(vID) 
    # print("")
    # print("Array of vehicle id: \n", vID_Array)
    # print("")
    # print("Vehicle 1: ", str(vID_Array[0]))

    # vehicleStatus = "OTW"
    # vehicleStatus_Idle = "OK"
    vehicleStatus = 'AVAILABLE'
    # vehicleCurrentLocation = vehicleLocationExtractor()
    #URL to the heartbeat API call
    API_URL = "https://supply.team12.softwareengineeringii.com/api/heartbeat/requestbeat"
    #Preparing data package:
    #Heatbeat package:
    for i in range(len(route)):
        data = {
        "vehicle_id": vehicleID,
        "vehicle_status": vehicleStatus,
        "vehicle_position": route[i]
    }
        #Converting the dictionary into a JSON object:
        # jsonObject = json.dumps(data)
        # headers = {'content-type': 'application/json'}
        #Sending request through a POST:
        request = requests.post(API_URL, json=data)
        #Status of the request:
        print("Sending heartbeat package...")
        print(request.status_code, request.reason)
        response_code = request.status_code
        #If the post request came back successfully with a response from the database
        #The reponse will be displayed through the terminal.
        if response_code == 200:
            returnStatusPackage = json.loads(request.content)
            supplyConfirmation = str(returnStatusPackage['response'])
            # recivedRoute = str(returnStatusPackage['route'])
            print("Supply BE response: " + str(supplyConfirmation))
            print("")
            # print("Supply BE route: " + str(recivedRoute))

        #Error has occurred:
        #Error handling
        else:
            errorStatus = 'Error Code: ' + str(response_code)
            bytesStr = errorStatus.encode('utf-8')
            print(request.text)
            print(bytesStr)

        #For testing purposes:
        print("***************Debugging purposes********************")
        print("Vehicle Current Location is: " + str(route[i]))
        print("Random vehicle status " + str(vehicleStatus))
        print(route[i])
        print("")
        print("Vehicle being worked with is: " + str(vehicleID))
        time.sleep(5)

        # print("Vehicle location in the database ")
        # print("")
        # #Requesting to add all vehicle from the database into the local vsim.
        # API_Call = 'https://supply.team12.softwareengineeringii.com/api/backend?vehicle-all=1'
        # # print('\tThe API http string --> ' + API_Call)
        # # print("")
        # jsonResponse = requests.get(API_Call).json()
        # print("Current registered vehicle: ")
        # # print(jsonResponse)
        # vehicle = json.dumps(jsonResponse)
        
        # #Vehicle information from the database: 
        # for i in range(len(jsonResponse)):
        #     #vehicle variable that holds the jsonObject:
        #     vehicle = jsonResponse[i]
        #     dummy_transfer = json.dumps(vehicle)
        #     vehicle_dictionary_2 = json.loads(dummy_transfer)

        #     vehicle_id = str(vehicle["_id"])
        #     vin_number = str(vehicle["vin"])
        #     vehicle_name = str(vehicle["vehicle_name"])
        #     vehicle_type = str(vehicle["vehicle_type"])
        #     vehicle_color = str(vehicle["vehicle_color"])
        #     # status = str(vehicle["is_available"])
        #     vehicle_location = str(vehicle["vehicle_position"])
        #     vehicle_status = str(vehicle["vehicle_status"])


        #     #Dictionary to hold those information:
        #     vehicle_dictionary = {
        #         "vehicle_id": vehicle_id,
        #         "vin_number": vin_number,
        #         "vehicle_name": vehicle_name,
        #         "vehicle_type": vehicle_type,
        #         "vehicle_color": vehicle_color,
        #         # "is_available": status,
        #         "vehicle_position": vehicle_location,
        #         "vehicle_status": vehicle_status
        #     }

        #     print("vehicle " ,str(i+1), " ",  str(vehicle_dictionary))

# sendingVehicleHeartbeatStatus(vehicleID)

# #Initializae a thread:

t1 = threading.Thread(target=sendingVehicleHeartbeatStatus, args=[vehicleID, route_1])
t1.start()
t2 = threading.Thread(target=sendingVehicleHeartbeatStatus, args=[vehicleID_2, route_2])
t2.start()
t3 = threading.Thread(target=sendingVehicleHeartbeatStatus, args=[vehicleID_3, route_3])
t3.start()


t1.join()
t2.join()
t3.join()


#Every available vehicle that are waiting for an order will be stored in the warehouse. 
#This means that any vehicle that are sitting idle or not currently being deployed will be stored here. 
# def vehicleLocationExtractor(route): 
#     # vehicleLastKnownLocation = 'Final Drop-Off address'
#     # vehicleCurrentLong = 0.0  
#     # vehicleCurrentLat = 0.0
#     # #JJ Picke Research Center location.
#     # # wareHouseLocation = {"lng": DEFAULT_LONG,"lat": DEFAULT_LAT}
#     # wareHouseLocation = [DEFAULT_LONG_STARTING, DEFAULT_LAT_STARTING]
#     vehicle_updated_location = []
#     #Looping through the coordinate array list to extract location:
#     for i in range(len(route)):
#         vehicle_updated_location = route[i]
#         # time.sleep(1)
#         # print(vehicle_updated_location)
#     return vehicle_updated_location

# print(vehicleLocationExtractor(DEFAULT_COORDINATES_STRING))