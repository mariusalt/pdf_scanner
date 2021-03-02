from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
import csv

pdf_names=[]
direc = [r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 1 (22.07. 1430)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 2 (23.07. 1430)\Daten\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 3 (10.08. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 4 (10.08. 1330)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 5 (12.08. 1330)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 6 (12.08. 1630)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 7 (13.08. 1330)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 8 (13.08. 1630)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 9 (14.08. 1330)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 10 (18.08. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 11 (26.08. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 12 (28.09. 1300)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 13 (31.09. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 14 (03.09. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 15 (02.11. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 16 (03.11. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 17 (04.11. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 18 (05.11. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 19 (06.11. 1000)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 20 (18.11. 1400)\Quittungen",
r"C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\Session 21 (19.11. 1400)\Quittungen",
]


for f,ses in enumerate(direc):
    pdf_names=[]
    for path in os.listdir(ses):
        pdf_names.append(os.path.join(ses, path))
    ff=f+1

    print(pdf_names)
    #pdf_names=['C:\\Users\\mat\\Desktop\\Policy tools as commitment devices\\Experiment\\Session 21 (19.11. 1400)\\Quittungen\\Pät_2.pdf']
    eidi=["id"]
    fund=["project"]
    name1=["name1"]
    name2=["name2"]
    pay={"ID":"payoff"}
    for pdf in pdf_names[0:len(pdf_names)]:
        name=str(pdf)
        print(name[name.find("Session"):name.find("\Quittungen")])
        PDF_file = name
        
        ''' 
        Part #1 : Converting PDF to images 
        '''
        
        # # Store all the pages of the PDF in a variable 
        # pages = convert_from_path(PDF_file, 500) 
        
        # # Counter to store images of each page of PDF to image 
        # image_counter = 1
        
        # # Iterate through all the pages stored above 
        # for page in pages: 
        
        #     # Declaring filename for each page of PDF as JPG 
        #     # For each page, filename will be: 
        #     # PDF page 1 -> page_1.jpg 
        #     # PDF page 2 -> page_2.jpg 
        #     # PDF page 3 -> page_3.jpg 
        #     # .... 
        #     # PDF page n -> page_n.jpg 
        #     filename = PDF_file[-9:-4]+".jpg"
            
        #     # Save the image of the page in system 
        #     page.save(r'C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\JPegs\S'+str(ff)+"\\"+filename, 'JPEG') 
        
        #     # Increment the counter to update filename 
        #     image_counter = image_counter + 1
        

        # ''' 
        # Part #2 - Recognizing text from the images using OCR 
        # '''
        # # Variable to get count of total number of pages 
        # filelimit = image_counter-1
        
        # # Creating a text file to write the output 
        # # outfile = "out_text.txt"
        
        # # # Open the file in append mode so that  
        # # # All contents of all images are added to the same file 
        # # f = open(outfile, "a") 
        

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # Iterate from 1 to total number of pages 
        for i in range(1, 2): 
        
            # Set filename to recognize text from 
            # Again, these files will be: 
            # page_1.jpg 
            # page_2.jpg 
            # .... 
            # page_n.jpg 
            filename = r'C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\JPegs\S'+str(ff)+"\\"+PDF_file[-9:-4]+".jpg"
            #filename = r'C:\Users\mat\Desktop\Policy tools as commitment devices\Experiment\JPegs\S'+"21"+"\\"+PDF_file[-9:-4]+".jpg"   
            # Recognize the text as string in image using pytesserct 
            text = str(((pytesseract.image_to_string(Image.open(filename))))) 
        
            # The recognized text is stored in variable text 
            # Any string processing may be applied on text 
            # Here, basic formatting has been done: 
            # In many PDFs, at line ending, if a word can't 
            # be written fully, a 'hyphen' is added. 
            # The rest of the word is written in the next line 
            # Eg: This is a sample text this word here GeeksF- 
            # orGeeks is half on first line, remaining on next. 
            # To remove this, we replace every '-\n' to ''. 
            text = text.replace('-\n', '') 
            fund.append(text[text.find("Experiment")+11:text.find("Experiment")+29])
            eidi.append(filename[-9:-4])
            n=text[text.find("Empfanger:")+11:text.find("Empfanger:")+100]
            name1.append(n.split()[0])
            name2.append(n.split()[1])
            if str(name2[-1])=='¢_)':
                n=text[text.find("Buchungstext:")+14:text.find("Buchungstext:")+100]
                name1[-1]=n.split()[0]
                name2[-1]=n.split()[1]
            if "Summe" in text:    
                if "HILF" in text[text.find("Summe")+6:text.find("Summe")+11]:
                    pay[name[name.find("Session"):name.find("\Quittungen")]+filename[-9:-4]]=text[text.find("SICHERHEIT")+12:text.find("SICHERHEIT")+17].replace(",",".")
                    if "https" in text[text.find("SICHERHEIT")+12:text.find("SICHERHEIT")+17]:
                        pay[name[name.find("Session"):name.find("\Quittungen")]+filename[-9:-4]]=text[text.find("EUR")-6:text.find("EUR")-1].replace(",",".")
                else: 
                    pay[name[name.find("Session"):name.find("\Quittungen")]+filename[-9:-4]]=text[text.find("Summe")+6:text.find("Summe")+11].replace(",",".")
            else:
                pay[name[name.find("Session"):name.find("\Quittungen")]+filename[-9:-4]]=text[text.find("Betrag")+10:text.find("Betrag")+15].replace(",",".")
                if "ftrag" in text[text.find("Betrag")+10:text.find("Betrag")+15]:
                    pay[name[name.find("Session"):name.find("\Quittungen")]+filename[-9:-4]]=text[text.find("EUR")-6:text.find("EUR")-1].replace(",",".")
            # Finally, write the processed text to the file. 
            #f.write(text) 
    fname="bills"+str(ff)+".csv"

    with open(fname, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i, (key,value) in enumerate(pay.items()):
            writer.writerow([str(key),value,str(fund[i]),eidi[i],name1[i],name2[i]])
    
# Close the file after writing all the text. 
#f.close() 