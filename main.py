from datetime import datetime
from datetime import date

import time, os, sys, pytz, random

def getCurrentTime():
	today = date.today()
	tanggal = today.strftime("%d/%m/%Y")
	tz_ID = pytz.timezone('Asia/Makassar')
	datetime_MK = datetime.now(tz_ID)
	waktu = datetime_MK.strftime("%H:%M:%S")
	result = tanggal + " " + waktu
	return result

def predict():
    file = open('./data.txt', 'w+')
    prediction = random.randrange(20, 1024)
    file.write("time prediction : %s" % (prediction))
    file.close()

def main():
    os.system('git commit -a -m "%s"' % (getCurrentTime()))
    os.system("git push -u origin main")

while (True):
    predict()
    main()
    time.sleep(10)