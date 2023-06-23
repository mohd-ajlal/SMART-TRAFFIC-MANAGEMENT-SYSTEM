import cv2
from vehicle_detector import VehicleDetector
import glob
import emoji
from util.dynamic_signal_switching import switch_signal
from util.dynamic_signal_switching import avg_signal_oc_time

vd = VehicleDetector()

image_folder = glob.glob("images/*.jpg")
vehicles_folder_count =0
# Load Veichle Detector

road = []

for img_path in image_folder:
    print("Img path",img_path)
    img =cv2.imread(img_path)
    
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    vehicles_folder_count+=vehicle_count

    time = int((vehicle_count*10)/(3+1))
    road.append(time)
    if(time>90):
        time = 90
    for box in vehicle_boxes:
        x,y,w,h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (255, 0, 0), 3)
        cv2.putText(img, "Timer: " + str(time), (20, 100), 0, 2, (255, 0, 0), 3)
    cv2.imshow("Cars", img)
    cv2.waitKey(0)

    print("Total current count", vehicle_count)
print(road)

denser_lane = road.index(max(road)) + 1
print("Max lane",denser_lane)

print(
    '\033[1m' +
    "------------------------------------------------------------------------------------------------------------------------------------------------------------"
)

print(
    emoji.emojize(':vertical_traffic_light:') + '\033[1m' + '\033[94m' +
    " Lane with denser traffic is : Lane " + str(denser_lane) + '\033[30m' +
    "\n")

switching_time = avg_signal_oc_time(road)


switch_signal(denser_lane, switching_time)

print(
    '\033[1m' +
    "------------------------------------------------------------------------------------------------------------------------------------------------------------"
)