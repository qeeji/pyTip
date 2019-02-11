## inWidget

def testMousePressEvent(event):
  button = event.button()
  print button
 
 
inWidget.mousePressEvent = testMousePressEvent
