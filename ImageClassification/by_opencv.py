# Import required libraries
import glob
import os
import pdf2image
import numpy as np
import cv2

def by_opencv():

    # Definition of constants    
    PDF_PATH = glob.glob("./PDFs/*.pdf")                              # Path-list for PDFs
    PDF_DIR = ["cv-result/"+path[7:len(path)-4] for path in PDF_PATH] # Path-list for dirs
    DPI = 100                                                         # Dots per inch
    SHRINKED = (int(1284/6), int(1828/6))                             # Shrinked-shape
    RG_DIFF_THRESHOLD = 20                                            # Saturation difference between R&G
    AREA_THRESHOLD = 3500                                             # Dots having saturatino difference
    FILENAME = "img_{:03d}.jpg"                                       # Preserve filename
    BI_THRES = 55                                                     # Binalization threshold
    H_LOW = 20                                                        # Mininum height
    H_HIGH = 30                                                       # Maximun height
    W_LOW = 20                                                        # Minumum width
    W_HIGH = 30                                                       # Maximum width
    CHARA_NUMBER = 20                                                 # Num of Characters


    # Make one directory per one PDF
    for path in PDF_DIR:
        os.makedirs(path, exist_ok=True)

        # Make three directories(text, diagram, image)
        os.makedirs(path + "/text/", exist_ok=True)
        os.makedirs(path + "/diagram/", exist_ok=True)
        os.makedirs(path + "/image/", exist_ok=True)

    # Iteration for each PDF
    for i, path in enumerate(PDF_PATH):
    
        # Convert PDF into data
        dataset = pdf2image.convert_from_path(path, DPI)
        
        # Iteration for each PDF page
        for j, pil_data in enumerate(dataset):
        
            # Convert data format and shrink
            cv2_data = np.asarray(pil_data)
            cv2_coar = cv2.resize(cv2_data, SHRINKED)

            # Get saturation difference between R&G in every dot
            rg_diff = np.empty(0)
            for k in range(cv2_coar.shape[0]):
                for l in range(cv2_coar.shape[1]):
                    rg_diff = np.append(rg_diff, cv2_coar[k][l][0]-cv2_coar[k][l][1])
        
            # Aggregation saturation difference
            rg_diff_abs = np.abs(rg_diff)
            rg_diff_area = np.sum(np.where(rg_diff_abs >= RG_DIFF_THRESHOLD, 1, 0))

            # Classify photos and other
            if rg_diff_area >= AREA_THRESHOLD:
                cv2.imwrite(PDF_DIR[i]+"/image/"+FILENAME.format(j+1), cv2_data)

            
            else:
                # Grayscaling and Binalization
                cv2_gray = cv2.cvtColor(cv2_data, cv2.COLOR_BGR2GRAY)
                cv2_bi = cv2.threshold(cv2_gray, BI_THRES, 255, cv2.THRESH_OTSU)[1]

                # Count characters by spacific shape Detection
                cnts = cv2.findContours(cv2_bi, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
                count = 0
                for char in cnts:
                    x, y, w, h = cv2.boundingRect(char)
                    if H_LOW <= h <= H_HIGH and W_LOW <= w <= W_HIGH: 
                        count += 1
                        cv2_data = cv2.drawContours(cv2_data, char, -1, (0,255,0), 3)
                                         
                # Claccify Diagrams and texts
                if count <= CHARA_NUMBER:
                    cv2.imwrite(PDF_DIR[i]+"/diagram/"+FILENAME.format(j+1), cv2_data)

                else:
                    cv2.imwrite(PDF_DIR[i]+"/text/"+FILENAME.format(j+1), cv2_data)         


if __name__ == "__main__":
    by_opencv()