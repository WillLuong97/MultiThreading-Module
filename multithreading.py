import logging
import threading
import time
import math
import concurrent.futures

# Move through the route at a certain mph
def traverse (route, mph, name):
    logging.info("Traverse Thread %s: starting", name)
    # Convert mph into mps
    mps = mph_to_mps(mph)
    
    # Make sure route is long enough
    if len(route) <= 1:
        raise Exception("Route is too short! Length of route is:", len(route))
    
    # Start route
    print ("Starting at", route[0])
    # loop through each route coordinate
    for index in range(len(route) - 1):
        start_coordinates = route[index]
        end_coordinates = route[index+1]
        
        # get distance between coordinates, convert it into meters to use with meters per second
        dist_remaining = calculate_distance (start_coordinates, end_coordinates) * 1000
               
        # 1 tick is 1 second
        # figure out how many ticks can fit inside the distance
        ticks_in_dist = int(dist_remaining) // int(mps)
        
        # if a tick can fit inside the distance
        if ticks_in_dist != 0:
            # the rate to travel to end coordinates from start coordinates
            lat_rate = (end_coordinates[0] - start_coordinates[0]) / float(ticks_in_dist)
            lon_rate = (end_coordinates[1] - start_coordinates[1]) / float(ticks_in_dist)
            
            # travel the distance and report current position
            for tick in range (ticks_in_dist):
                dist_remaining -= mps
                current_position = [start_coordinates[0] + lat_rate*tick, start_coordinates[1] + lon_rate*tick]
                print ("current position", current_position, "distance remaining:", dist_remaining)
                time.sleep(1)
        # if not, just report position
        else:
            current_position = [start_coordinates[0] + lat_rate*tick, start_coordinates[1] + lon_rate*tick]
            print ("current position", current_position, "distance remaining:", dist_remaining)
            time.sleep(1)
            
        # report that the vehicle arrived
        print ("Arrived at ", route[index+1])
        
    print ("Done moving!")
    logging.info("Traverse Thread %s: finishing", name)

# Convert Miles per hour to meters per second
def mph_to_mps(mph):
    return mph * 0.44704

# https://kite.com/python/answers/how-to-find-the-distance-between-two-lat-long-coordinates-in-python
# output the distance between two coordinates in kilometers
def calculate_distance (latlong1, latlong2):
    R = 6373.0 # radius of the Earth in km
    
    # coordinates
    lat1 = math.radians(latlong1[0])
    lon1 = math.radians(latlong1[1])
    lat2 = math.radians(latlong2[0])
    lon2 = math.radians(latlong2[1])
    
    # change in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    
if __name__ == "__main__":
    route = [
        [-97.753044,30.228733],
        [-97.75412,30.226749],
        [-97.760239,30.229656],
        [-97.76342,30.223763],
        [-97.764214,30.223803],
        [-97.76947,30.226734],
        [-97.783638,30.22826],
        [-97.793266,30.23254],
        [-97.798042,30.236332],
        [-97.803467,30.247017],
        [-97.80275,30.249693],
        [-97.802299,30.252073],
        [-97.798698,30.257648],
        [-97.774544,30.270313]
    ]
    
    torchy_route = [
        [
            -97.753044,
            30.228733
        ],
        [
            -97.75412,
            30.226749
        ],
        [
            -97.760239,
            30.229656
        ],
        [
            -97.757233,
            30.234423
        ],
        [
            -97.753075,
            30.239384
        ],
        [
            -97.75251,
            30.241926
        ],
        [
            -97.75132,
            30.245169
        ],
        [
            -97.751663,
            30.24527
        ]
    ]
    
    airport_route = [
        [
            -97.753044,
            30.228733
        ],
        [
            -97.753677,
            30.229412
        ],
        [
            -97.751083,
            30.231468
        ],
        [
            -97.747032,
            30.229643
        ],
        [
            -97.745102,
            30.227922
        ],
        [
            -97.746178,
            30.225496
        ],
        [
            -97.746643,
            30.22471
        ],
        [
            -97.750023,
            30.219261
        ],
        [
            -97.750626,
            30.217573
        ],
        [
            -97.749535,
            30.216143
        ],
        [
            -97.742958,
            30.215986
        ],
        [
            -97.710022,
            30.212252
        ],
        [
            -97.692719,
            30.217714
        ],
        [
            -97.684662,
            30.221289
        ],
        [
            -97.679741,
            30.222427
        ],
        [
            -97.675331,
            30.22159
        ],
        [
            -97.662727,
            30.215014
        ],
        [
            -97.660843,
            30.213661
        ],
        [
            -97.659782,
            30.213104
        ],
        [
            -97.659592,
            30.212263
        ],
        [
            -97.660645,
            30.211428
        ],
        [
            -97.662041,
            30.211096
        ],
        [
            -97.66259,
            30.21151
        ],
        [
            -97.665001,
            30.209602
        ],
        [
            -97.664764,
            30.209044
        ]
    ]
    
    routes = [route, torchy_route, airport_route]
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    
    #threading:
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for index in range(3):
            executor.submit(traverse, routes[index], 240, index)
