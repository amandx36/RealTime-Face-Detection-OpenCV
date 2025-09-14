import cv2 as cv 
import os 

# loading the pretrained module provided by the open cv 

haarCascadeFile =  cv.CascadeClassifier("haar_face.xml")

# capturing the video from the web camera 

videoCapture =  cv.VideoCapture(0) 

# now reading frame by frame 
while (1):
    true , frame  =  videoCapture.read()
    if not true:
        print("camera capturing error !!!! ")
        break ;

# converting the frame into the grey scale !!! 
    grayFrame  = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # scaleFactor = reducing the capture fame dimension smaller to smaller like  the pyramid for getting the more precision !!! 
    isFaceAvailable = haarCascadeFile.detectMultiScale(grayFrame , scaleFactor = 1.1 , minNeighbors = 3 )



    # now highlighting the face with the rectangle !!! 

    for (x, y ,  w , h ) in isFaceAvailable :
        cv.rectangle(frame , (x,y) , (x + w , y + h ) , (0,0,255), thickness = 2 )
        
        # if multiple faces so one time text show thus adding this functionality !!! 
    if len(isFaceAvailable)> 0 :
             # adding text if the face is detected brother !!! 
            cv.putText(frame , "Face Detected ",(20,90,),cv.FONT_HERSHEY_SIMPLEX
,1.5,(0,0,255),3)
    
    if len(isFaceAvailable) == 0 :
         cv.putText(frame , "No Face Available !  ",(20,90,),cv.FONT_HERSHEY_SIMPLEX
,1.5,(0,0,255),3)
    
         
        
        

    # now showing  the image 
    cv.imshow("Face Detection ", frame)

    # add functionality for quit by the user !!! 
    # some time key return some extra junk bytes so we are filtering need only last 8 bit so we use this filter !!! 0xFF 
    if cv.waitKey(1) & 0xFF == ord('q'):
        break ;

videoCapture.release()
cv.destroyAllWindows()
