# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 03:27:05 2020

@author: Barış Şenyerli - http://bit.ly/linkedbaris
It read the image text -if it was there- than change it name with this text.
"""

import os
import cv2
import pytesseract
from matplotlib import pyplot as plt
import text_detection as td
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # absolute need


def main(): 
    i = 1
    path  = 'C:\\Users\\YourComputer\\Desktop\\yourfolder\\'
    characters = "/><(')¢*&©^%°£$—®»£;`?¬\"|!]~,“”@é}[-.:= ’‘" # some trash characters need to go recycle
    for filename in os.listdir(path): 
        src = filename 
        img = cv2.imread( path + filename,0 )
        print( "src1:" + src )
        
        dst = td.imgToText(path + filename)
        for c in characters:
            dst = dst.translate({ord(c): None})
        dst = dst.replace( '\\', '' )
        dst = dst.replace( '\n', '_' )
        dst = dst.replace( '_', ' ',4 ) 
        
        dst = dst.lower()+'.jpg'
        
        if len(dst) < 5 :
            dst = str(i)+'.jpg'
        if len(dst) > 100 :
            dst = dst[-100:]+'.jpg'
        print(dst)
        plt.subplot(121),plt.imshow(img)
        plt.show()
        print("SRC:"+src+"\nDST:"+dst)
        print()
        try:
            os.rename(path+src, path+dst) 
        except FileExistsError:
            dst = "i was remember that"+str(i)+'.jpg'
            #os.rename(path+src, path+dst)
        except:
            print("Something else went wrong")
        
        
        i += 1

if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
