#The urls might not exist. That depends on the formule1.nl website. I am not a copyright holder. The urls are public and they are used as an example in this script. 


import requests
import time

widthrange = range(1501,6502)
heightrange = range(600,3002)
for width in widthrange:
    for height in heightrange:
        image = 'https://www.formule1.nl/app/uploads/2018/01/75mon25-'+str(width)+'x'+str(height)+'.jpg'        
        request = requests.get(image)
        if request.status_code == 200:
            print(image)

#width = '1500'
#height = '600'

'''
https://www.formule1.nl/app/uploads/2018/01/9-Panis-2-3660x2367.jpg
https://www.formule1.nl/app/uploads/2018/01/9-Panis-3-600x395.jpg
https://www.formule1.nl/app/uploads/2018/01/9-Panis-3.jpg
https://www.formule1.nl/app/uploads/2018/01/teh0317fe12-428x280.jpg
https://www.formule1.nl/app/uploads/2018/01/75mon25-1500x600.jpg
https://www.formule1.nl/app/uploads/2018/01/29-Sauber-2-e1517215557809-1500x600.jpg
https://www.formule1.nl/app/uploads/2018/01/29-Sauber-6-600x400.jpg
https://www.formule1.nl/app/uploads/2018/01/75aut18-429x280.jpg
https://www.formule1.nl/app/uploads/2018/01/75mon30-400x612.jpg

'''

