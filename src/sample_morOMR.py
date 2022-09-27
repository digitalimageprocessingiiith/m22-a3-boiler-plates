# Author: @BVK
# Assignment 3: Question 1 Boiler Plate
import cv2 as cv
import numpy as np
# do not import any other library
# Note: this is just a boiler plate
# feel free to make changes in the structure
# however, input/output should essentially be the same.

def getAnswers(omr_sheet)->list:
  """
     Your documentation here
  """
  # do all your processing here.
  # return answers of particular omr sheet here
  
  pass

if __name__ == "__main__":
  
  # Read the number of test cases
  # input() returns str by default, i.e. 1000 is read as '1000'.
  # .strip() used here to strip of the trailing `\n` character
      
  T = int(input().strip())
                           
  
  for i in range(T):
    
    fileName = input().strip() # read path to image
    omr_sheet = cv.imread(fileName)
    
    
    answers = getAnswers(omr_sheet) # fetch your answer
    for answer in answers: # assuming answers is a list
      print(answer)  # print() function automatically appends the `\n`
