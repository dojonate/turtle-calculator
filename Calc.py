#**********************  Calc.py  *********************
#
# Name: Nathan Dill
#
# Course: CSCI 1470
#
# Assignment: Final Project
#
# Algorithm:
#
# start
#     get turtle graphics
#     tell OS to draw screen
#     set drawing area
#     set window size
#     save button shapes
#     set screen update time to 0 ms (instant)
#     create empty list for main buttons
#     append first turtle to button list
#     pick up pen
#     set turtle shape to box
#     move turtle to start location
#     for turtle 2 through 16
#         append clone of first turtle to list of turtles
#     move turtles to y coordinates
#     move turtles to x coordinates
#     create special turtle for 0 button
#     create special turtle for decimal
#     create special turtle for 'calculate' (equals) button
#     label all turtles
#     create printer turtle
#     create cursor turtle
#     declare variables
#     create function calculate with parameters variable1, variable2, and operator
#         if var1 equal to 0
#             variable1 equals 0
#         end if
#         if variable2 not equal to ""
#             operate on variable1 with variable2 using relevant operation
#         end if
#         return variable1
#     create function myMainloop with parameters x and y
#         set variables to global
#         move cursor to location x,y
#         
#         if cursor near clear button
#             clear appropriate variable
#         if operator equal to '' or "="
#             if cursor position is in range of operator turtle
#                 printer turtle prints value of button
#                 operator equals equivalent operation symbol
#             else if cursor position is in range of main button turtle
#                 printer turtle prints value of main button turtle
#                 num1 append appropriate value
#             else if cursor position is in range of 0 turtle
#                 printer turtle prints value of button
#                 num1 append '0'
#             else if cursor position is in range of decimal turtle
#                 printer turtle prints value of button
#                 num1 append '.'
#             else if cursor position is in range of clear turtle
#                 num1 equals ''
#                 num2 equals ''
#                 operator equals ''
#             else if cursor position is in range of equals turtle
#                 if last calculation has results
#                     calculate result of last calculation operated on by last variable2
#                 printer turtle prints result or variable1
#                 operator equals "="
#                 end if
#             end if
#         else if operator not equal to '' and operator not equal to '='
#             else if cursor position is in range of 0 turtle
#                 if operator is "/"
#                     printer turtle prints division warning
#                 else:
#                     printer turtle prints value of button
#                     num2 append '0'
#             else if cursor position is in range of decimal turtle
#                 printer turtle prints value of button
#                 num2 append '.'
#             if cursor position is in range of main button turtle
#                 printer turtle prints value of main button turtle
#                 num2 append appropriate value
#             else if cursor position is in range of operator turtle
#                 variable1 equals result of previous operator calculation
#                 printer turtle prints value of button
#                 operator equals equivalent operation symbol
#             end if
#         end if
#         oldpos equals cursor position
#         
#     on click call myMainloop and pass click location
#     listen for click
#     
#     call mainloop
# stop
#
#**********************************************************

import turtle

wn = turtle.Screen()

wn.screensize(400,650)                          #Create Screen
wn.setup(450,700,None,None)

a = 45
b = 95
wn.register_shape("box", ((a,a), (-a,a), (-a,-a), (a,-a), (a,a), (a,-a), (-a,-a), (-a,a), (a,a)))
wn.register_shape("rect", ((a,b), (-a,b), (-a,-b), (a,-b), (a,b), (a,-b), (-a,-b), (-a,b), (a,b)))

wn.delay(0)
global butn
butn = []

locx = -150
locy = -175
oh = 100

butn.append(turtle.Turtle())
butn[0].penup()
butn[0].speed(0)				#make turtles update as fast as possible
butn[0].shape('box')
butn[0].goto(locx+0*oh, locy+0*oh)
for i in range(1,16):
    butn.append(butn[0].clone())
for i in range(0,16):
    butn[i].goto(butn[i].xcor(),locy+i//4*oh)
for i in range(0,4):
    butn[i+0 ].goto(locx+i*oh,butn[i+0 ].ycor())
    butn[i+4 ].goto(locx+i*oh,butn[i+4 ].ycor())
    butn[i+8 ].goto(locx+i*oh,butn[i+8 ].ycor())
    butn[i+12 ].goto(locx+i*oh,butn[i+12 ].ycor())

#zero button
global but0
but0 = turtle.Turtle()
but0.penup()
but0.speed(0)
but0.shape('rect')
but0.goto(locx+.5*oh, locy-1*oh)

#decimal button
global butdot
butdot = turtle.Turtle()
butdot.penup()
butdot.speed(0)
butdot.shape('box')
butdot.goto(locx+2*oh, locy-1*oh)

#calculate button
global buteq
buteq = turtle.Turtle()
buteq.penup()
buteq.speed(0)
buteq.shape('box')
buteq.goto(locx+3*oh, locy-1*oh)

#labels
for i in range(0,16):
    if i<3:
        butn[i].write(str(i+1), False, "center", ("Monaco",26,"bold"))
    elif 3<i<7:
        butn[i].write(str(i),   False, "center", ("Monaco",26,"bold"))
    elif 7<i<11:
        butn[i].write(str(i-1), False, "center", ("Monaco",26,"bold"))
but0.write    (" 0 ", False, "center", ("Monaco",28,"bold"))
butn[3].write (" + ", False, "center", ("Monaco",28,"bold"))
butn[7].write (" – ", False, "center", ("Monaco",28,"bold"))
butn[11].write(" x ", False, "center", ("Monaco",28,"bold"))
butn[15].write(" ÷ ", False, "center", ("Monaco",28,"bold"))
butn[12].write(" AC ", False, "center", ("Monaco",28,"bold"))
butn[13].write("+/-", False, "center", ("Monaco",28,"bold"))
butn[14].write("exp", False, "center", ("Monaco",28,"bold"))
butdot.write  (" . ", False, "center", ("Monaco",28,"bold"))
buteq.write   (" = ", False, "center", ("Monaco",28,"bold"))

global printer
printer = turtle.Turtle()
printer.penup()
printer.ht()
printer.goto((locx+3.5*oh)-2, locy+4*oh)
printer.pendown()
printer.write("0", False, "right", ("Monaco",32,"normal"))

global cursor
cursor = turtle.Turtle()
cursor.speed(0)
cursor.pu()
cursor.ht()

oldpos = cursor.pos()

#declare variables
var1 = ""
var2 = ""
oper = ""
temp2 = ""
temopr = ""

def calculate(var1,var2,oper):
	if var1 == "":
		var1 = "0"
	if var2 != "":
		if   oper[len(oper)-1]=="+":
			var1 = str(float(var1)+ float(var2))
			if var1[len(var1)-2:len(var1)] == ".0":
				var1 = var1[0:len(var1)-2]
		elif oper[len(oper)-1]=="–":
			var1 = str(float(var1)- float(var2))
			if var1[len(var1)-2:len(var1)] == ".0":
				var1 = var1[0:len(var1)-2]
		elif oper[len(oper)-1]=="x":
			var1 = str(float(var1)* float(var2))
			if var1[len(var1)-2:len(var1)] == ".0":
				var1 = var1[0:len(var1)-2]
		elif oper[len(oper)-1]=="÷":
			var1 = str(float(var1)/ float(var2))
			if var1[len(var1)-2:len(var1)] == ".0":
				var1 = var1[0:len(var1)-2]
		elif oper        =="\npwr(":
			var1 = str(float(var1)**float(var2))
			if var1[len(var1)-2:len(var1)] == ".0":
				var1 = var1[0:len(var1)-2]
		for i in range (10):
		    err = var1.find(str(i)+str(i)+str(i)+str(i))
		    decpt = var1.find('.')
		    if err != -1 and err > decpt:
		        if i != 0:
		            var1 = var1[0:decpt]
		        else:
		            var1 = var1[0:decpt+4]
		    
	return var1

def myMainloop(x,y):
    global oldpos, var1, var2, oper, temp2, temopr
    cursor.goto(x,y)
    #Clear
    if cursor.xcor() in range ((butn[12].xcor()-45),(butn[12].xcor()+45)) and cursor.ycor() in range (butn[12].ycor()-45,butn[12].ycor()+45):
        if var2!="":
            var2=""
            oper=""
        elif var1!="":
            var1=""
            oper=""
            butn[12].clear()
            butn[12].write(" AC ", False, "center", ("Monaco",28,"bold"))
        else:
            var1=""
            var2=""
            oper=""
        printer.clear()
        printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
        print(var1,oper,var2)

    
    elif oper == "" or oper == "=":
        #First Variable
        vary = var1
        if cursor.xcor()   in range ((butn[3].xcor()-45), (butn[3].xcor()+45))  and cursor.ycor() in range (butn[3].ycor()-45,butn[3].ycor()+45):
            printer.clear()
            oper = "\n+"
            printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[7].xcor()-45), (butn[7].xcor()+45))  and cursor.ycor() in range (butn[7].ycor()-45,butn[7].ycor()+45):
            printer.clear()
            oper = "\n–"
            printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[11].xcor()-45),(butn[11].xcor()+45)) and cursor.ycor() in range (butn[11].ycor()-45,butn[11].ycor()+45):
            printer.clear()
            oper = "\nx"
            printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[14].xcor()-45),(butn[14].xcor()+45)) and cursor.ycor() in range (butn[14].ycor()-45,butn[14].ycor()+45):
            printer.clear()
            oper = "\npwr("
            printer.write(var1 + oper + ")", False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[15].xcor()-45),(butn[15].xcor()+45)) and cursor.ycor() in range (butn[15].ycor()-45,butn[15].ycor()+45):
            printer.clear()
            oper = "\n÷"
            printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[13].xcor()-45),(butn[13].xcor()+45)) and cursor.ycor() in range (butn[13].ycor()-45,butn[13].ycor()+45):
            printer.clear()
            if var1[0]!="-":
                var1 = "-" + var1
            else:
                var1 = var1[1:len(var1)]
            printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        
        elif cursor.xcor() in range ((butn[5].xcor()-145),butn[5].xcor()+145) and cursor.ycor() in range (butn[5].ycor()-145,butn[5].ycor()+145):
            if oper == "=":
                var1 = ""
                oper = ""
                temopr = ""
                var2 = ""
            if var1 == "0":
                var1 = ""
            for button in range(0,16):
                if button<3:
                    if cursor.xcor() in range ((butn[button].xcor()-45),(butn[button].xcor()+45)) and cursor.ycor() in range (butn[button].ycor()-45,butn[button].ycor()+45):
                        printer.clear()
                        var1 += str(button+1)
                        printer.write(var1, False, "right", ("Monaco",32,"normal"))
                        print(var1)
                elif 3<button<7:
                    if cursor.xcor() in range ((butn[button].xcor()-45),butn[button].xcor()+45) and cursor.ycor() in range (butn[button].ycor()-45,butn[button].ycor()+45):
                        printer.clear()
                        var1 += str(button)
                        printer.write(var1, False, "right", ("Monaco",32,"normal"))
                        print(var1)
                elif 7<button<11:
                    if cursor.xcor() in range (butn[button].xcor()-45,butn[button].xcor()+45) and cursor.ycor() in range (butn[button].ycor()-45,butn[button].ycor()+45):
                        printer.clear()
                        var1 += str(button-1)
                        printer.write(var1, False, "right", ("Monaco",32,"normal"))
                        print(var1)
        elif ((but0.xcor()-90) < cursor.xcor() < (but0.xcor()+90)) and cursor.ycor() in range (but0.ycor()-45,but0.ycor()+45):
            if oper == "=":
                oper = ""
                var1 = ""
                temopr = ""
                var2 = ""
            if var1 == "0":
                var1 = ""
            printer.clear()
            var1 += "0"
            printer.write(var1, False, "right", ("Monaco",32,"normal")) 
            print(var1)
        elif ((butdot.xcor()-45) < cursor.xcor() < (butdot.xcor()+45)) and cursor.ycor() in range (butdot.ycor()-45,butdot.ycor()+45):
            if oper == "=":
                oper = ""
                var1 = ""
                temopr = ""
                var2 = ""
            printer.clear()
            var1 += "."
            printer.write(var1, False, "right", ("Monaco",32,"normal"))
            print(var1)
        elif ((buteq.xcor()-45) < cursor.xcor() < (buteq.xcor()+45)) and cursor.ycor() in range (buteq.ycor()-45,buteq.ycor()+45):
            printer.clear()
            if temp2 != "" and var1 != "" and len(temopr)>0:
                var1 = calculate(var1,temp2,temopr)
            printer.write(var1, False, "right", ("Monaco",32,"normal"))
            oper = "="
        if vary != var1:
            butn[12].clear()
            butn[12].write(" C ", False, "center", ("Monaco",28,"bold"))
    
        
    elif oper != "" and oper != "=":
        #Second Variable
        if ((but0.xcor()-90) < cursor.xcor() < (but0.xcor()+90)) and cursor.ycor() in range (but0.ycor()-45,but0.ycor()+45):
            printer.clear()
            if oper != "\n÷" or var2 != "":
                if var1 == "0":
                    var1 = ""
                var2 += "0"
                if oper == "\npwr(":
                    printer.write(var1 + oper + var2 + ")", False, "right", ("Monaco",32,"normal"))
                else:
                    printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
            else:
                printer.write(var1 + oper + "Can't Divide", False, "right", ("Monaco",32,"normal"))
            print(var2)
        elif ((butdot.xcor()-45) < cursor.xcor() < (butdot.xcor()+45)) and cursor.ycor() in range (butdot.ycor()-45,butdot.ycor()+45):
            printer.clear()
            var2 += "."
            if oper == "\npwr(":
                printer.write(var1 + oper + var2 + ")", False, "right", ("Monaco",32,"normal"))
            else:
                printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
            print(var2)
        elif cursor.xcor() in range ((butn[5].xcor()-145),butn[5].xcor()+145) and cursor.ycor() in range (butn[5].ycor()-145,butn[5].ycor()+145):
            for button in range(0,16):
                if button<3:
                    if cursor.xcor() in range ((butn[button].xcor()-45),(butn[button].xcor()+45)) and cursor.ycor() in range (butn[button].ycor()-45,butn[button].ycor()+45):
                        printer.clear()
                        var2 += str(button+1)
                        if oper == "\npwr(":
                            printer.write(var1 + oper + var2 + ")", False, "right", ("Monaco",32,"normal"))
                        else:
                            printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
                        print(var1 + oper + var2)
                elif 3<button<7:
                    if cursor.xcor() in range ((butn[button].xcor()-45),butn[button].xcor()+45) and cursor.ycor() in range (butn[button].ycor()-45,butn[button].ycor()+45):
                        printer.clear()
                        var2 += str(button)
                        if oper == "\npwr(":
                            printer.write(var1 + oper + var2 + ")", False, "right", ("Monaco",32,"normal"))
                        else:
                            printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
                            print(var1 + oper + var2)
                elif 7<button<11:
                    if cursor.xcor() in range (butn[button].xcor()-45,butn[button].xcor()+45) and cursor.ycor() in range (butn[button].ycor()-45,butn[button].ycor()+45):
                        printer.clear()
                        var2 += str(button-1)
                        if oper == "\npwr(":
                            printer.write(var1 + oper + var2 + ")", False, "right", ("Monaco",32,"normal"))
                        else:
                            printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
                            print(var1 + oper + var2)
        elif ((buteq.xcor()-45) < cursor.xcor() < (buteq.xcor()+45)) and cursor.ycor() in range (buteq.ycor()-45,buteq.ycor()+45):
            printer.clear()
            var1 = calculate(var1,var2,oper)
            printer.write(var1, False, "right", ("Monaco",32,"normal"))
            temp2 = var2
            temopr = oper
            var2 = ""
            oper = "="
        elif cursor.xcor() in range ((butn[3].xcor()-45),(butn[3].xcor()+45)) and cursor.ycor() in range (butn[3].ycor()-45,butn[3].ycor()+45):
            #add
            printer.clear()
            if var2=="":
                oper = "\n+"
                printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
            else:
                var1 = calculate(var1,var2,oper)
                var2 = ""
                oper = "\n+"
                printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[7].xcor()-45),(butn[7].xcor()+45)) and cursor.ycor() in range (butn[7].ycor()-45,butn[7].ycor()+45):
            #subtract
            printer.clear()
            if var2=="":
                oper = "\n-"
                printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
            else:
                var1 = calculate(var1,var2,oper)
                var2 = ""
                oper = "\n-"
                printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[11].xcor()-45),(butn[11].xcor()+45)) and cursor.ycor() in range (butn[11].ycor()-45,butn[11].ycor()+45):
            #multiply
            printer.clear()
            if var2=="":
                oper = "\nx"
                printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
            else:
                var1 = calculate(var1,var2,oper)
                var2 = ""
                oper = "\nx"
                printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[15].xcor()-45),(butn[15].xcor()+45)) and cursor.ycor() in range (butn[15].ycor()-45,butn[15].ycor()+45):
            #divide
            printer.clear()
            if var2=="":
                oper = "\n÷"
                printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
            else:
                var1 = calculate(var1,var2,oper)
                var2 = ""
                oper = "\n÷"
                printer.write(var1 + oper, False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[14].xcor()-45),(butn[14].xcor()+45)) and cursor.ycor() in range (butn[14].ycor()-45,butn[14].ycor()+45):
                #exponent
                if var2=="":
                        printer.clear()
                        oper = "\npwr("
                        printer.write(var1 + oper + var2 + ")", False, "right", ("Monaco",32,"normal"))
        elif cursor.xcor() in range ((butn[13].xcor()-45),(butn[13].xcor()+45)) and cursor.ycor() in range (butn[13].ycor()-45,butn[13].ycor()+45):
            printer.clear()
            if var2 == "":
                var2 = "0"
            if var2[0]!="-":
                var2 = "-" + var2
            else:
                var2 = var2[1:len(var2)]
            if oper == "\npwr(":
            	printer.write(var1 + oper + var2 + ")", False, "right", ("Monaco",32,"normal"))
            else:
            	printer.write(var1 + oper + var2, False, "right", ("Monaco",32,"normal"))
        
            
        
            
    oldpos = cursor.pos()


wn.onclick(myMainloop)
wn.listen()
##butn2 = butn1.clone()
##butn2.goto(-50,250)

wn.mainloop()
