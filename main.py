import cv2
car = cv2.imread("r34.jpg")
#circle
circle = cv2.circle(car,(750,60),35, (255, 36, 189), 10)
cv2.imshow("s", circle)
cv2.waitKey(0)
#rectangle
rectangle = cv2.rectangle(car, (500, 500), (800, 700),(79, 69, 255), 10 )
cv2.imshow("s2", rectangle)
cv2.waitKey(0)
#square
square = cv2.rectangle(car, (350, 350), (800, 800), (70, 85, 245), 10)
cv2.imshow("s3", square)
cv2.waitKey(0)
#line
line = cv2.line(car, (800, 800), (93, 600), (47, 73, 164), 10)
cv2.imshow("s4", line)
cv2.waitKey(0)
#text
text = cv2.putText(car, "ilikecars", (500, 450), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 10, (78, 43, 43), 9)
cv2.imshow("s5", text)
cv2.waitKey(0)