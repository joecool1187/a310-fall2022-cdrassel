from turtle import Turtle

def turtle_command(text):
  commandList = text.split(",")
  command = commandList[0]
  print (command)

  if command == "goto":
    x = float(commandList[1])
    y = float(commandList[2])
    width = float(commandList[3])
    color = commandList[4].strip()

    t.width(width)
    t.pencolor(color)
    t.goto(x,y)
  elif command == "circle":
    radius = float(commandList[1])
    width = float(commandList[2])
    color = commandList[3].strip()

    t.width(width)
    t.pencolor(color)
    t.circle(radius)
  elif command == "beginfill":
    color = commandList[1].strip()
    t.fillcolor(color)
    t.begin_fill()
  elif command == "endfill":
    t.end_fill()
  elif command == "penup":
    t.penup()
  elif command == "pendown":
    t.pendown()
  else:
    print("Unknown command found in file:" + command)


def main():   
  filename = input("Please enter filename: ")
  
  global t
  t = Turtle()
  
  screen = t.getscreen()

  #In the file
  with open(filename) as f:
    for line in f:
      # Iterating the lines
      text = line.strip()
      turtle_command(text)
      print(text)
  
  t.ht()
  screen.exitonclick()
  


if __name__ == "__main__":
  main()