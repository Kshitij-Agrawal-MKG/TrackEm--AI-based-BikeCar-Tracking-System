from ultralytics import YOLO
import cv2
from sort.sort import *
from imgToText import *
import csv
from sendMessage import *
import smtplib
import ssl
contest_data = ssl.create_default_context()


coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('./license_plate_detector.pt')
"""CamInput = cv2.VideoCapture(1)
CamInput.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
CamInput.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)"""
CamInput = cv2.VideoCapture("./sample2.mp4")
mot_tracker = Sort()
vehicles = [2, 3, 5, 7]
sentList = list()

userid = #enter your user Id
userpasswd = # enter your password

try:
    contest_data = ssl.create_default_context()
    mail = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contest_data)
    mail.login(userid, userpasswd)
    print("Successfully logged in...")

except Exception as erroemsg:
    print(erroemsg)
    erroemsg = str(erroemsg)[14::]
    print(f"{erroemsg[:erroemsg.find('.') + 1]}")
    exit()


emailadd = open("email.csv", 'r')
db = open("db.csv", 'r')

dbreader = csv.reader(db, delimiter=',')
emailreader = csv.reader(emailadd, delimiter=',')
dbDataList = list()
emailDataList = list()
for i in dbreader:
    dbDataList.append(i)

for i in emailreader:
    #print(i)
    emailDataList.append(i[0])
#print(emailDataList)


while True:
    ret, CamFrame = CamInput.read()

    license_plates = license_plate_detector(CamFrame)[0]
    for license_plate in license_plates.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = license_plate
        #print(license_plate)

        license_plate_crop = CamFrame[int(y1):int(y2), int(x1): int(x2), :]
        license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
        _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 150, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow("License Plate", license_plate_crop)

        #read_license_plate(license_plate_crop_gray)
        numPlate = read_license_plate(license_plate_crop)
        try:
            if len(numPlate) == 10:
                for dbData in dbDataList:
                    #print(dbData)
                    if (numPlate == dbData[0]) and (numPlate not in sentList):
                        cv2.rectangle(CamFrame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 4)

                        saveImg = cv2.resize(CamFrame, (1280, 720))
                        #cv2.imshow("Vehicle", saveImg)
                        cv2.imwrite("Image.jpg", saveImg)
                        mailSend(mail, userid, emailDataList, dbData)

                        sentList.append(numPlate)
        except Exception as e:
            print(e)


        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
