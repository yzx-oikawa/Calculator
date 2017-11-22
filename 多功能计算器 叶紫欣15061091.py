from tkinter import * #导入包
from tkinter import W,E,LEFT,RIGHT #导入方位
from tkinter.ttk import Style,Button,Label,Entry #导入风格、按钮、标签、文本框
import math #导入math模块函数

root = Tk() #计算器的窗体对象
root.title("多功能计算器") #添加标题
global i #设置与改变进制有关的全局变量i
i=10 #初始设定为十进制

#设定不同进制时的不同界面的函数
def menu10():#十进制
    global i
    i=10
    #显示数字23456789键
    two.grid(row=4,column=3)
    three.grid(row=4,column=4)
    four.grid(row=3,column=2)
    five.grid(row=3,column=3)
    six.grid(row=3,column=4)
    seven.grid(row=2,column=2)
    eight.grid(row=2,column=3)
    nine.grid(row=2,column=4)
    #隐藏abcdef键
    a.grid_forget()
    b.grid_forget()
    c.grid_forget()
    d.grid_forget()
    e.grid_forget()
    f.grid_forget()
def menu2():#二进制
    global i
    i=2
    #隐藏23456789abcdef键
    two.grid_forget()
    three.grid_forget()
    four.grid_forget()
    five.grid_forget()
    six.grid_forget()
    seven.grid_forget()
    eight.grid_forget()
    nine.grid_forget()
    a.grid_forget()
    b.grid_forget()
    c.grid_forget()
    d.grid_forget()
    e.grid_forget()
    f.grid_forget()
def menu8():#八进制
    global i
    i=8
    #显示数字234567键
    two.grid(row=4,column=3)
    three.grid(row=4,column=4)
    four.grid(row=3,column=2)
    five.grid(row=3,column=3)
    six.grid(row=3,column=4)
    seven.grid(row=2,column=2)
    #隐藏89abcdef键
    eight.grid_forget()
    nine.grid_forget()
    a.grid_forget()
    b.grid_forget()
    c.grid_forget()
    d.grid_forget()
    e.grid_forget()
    f.grid_forget()
def menu16():#十六进制
    global i
    i=16
    #显示23456789abcdef键
    two.grid(row=4,column=3)
    three.grid(row=4,column=4)
    four.grid(row=3,column=2)
    five.grid(row=3,column=3)
    six.grid(row=3,column=4)
    seven.grid(row=2,column=2)
    eight.grid(row=2,column=3)
    nine.grid(row=2,column=4)
    a.grid(row=6,column=0)
    b.grid(row=6,column=1)
    c.grid(row=6,column=2)
    d.grid(row=6,column=3)
    e.grid(row=6,column=4)
    f.grid(row=6,column=5)
def Help():#子目录【使用说明】
    root2 = Tk()#使用说明的窗体对象
    root2.title("帮助")#设置标题
    root2.geometry("350x170")#设置窗体大小
    label=Label(root2,text="",width=60)#设置标签宽度
    #使用说明文字
    label["text"]="\n欢迎使用！\n多功能计算器使用说明\n在“进制选择”中选取相应的进制\n用鼠标点击数字与运算符后将在显示屏中输出算式\n随后点击“=”即可得出结果\n注：进行下一次计算前需点击C清空显示屏"
    label.pack()#显示使用说明的窗体

#建立根菜单栏
menubar = Menu(root) #创建一个菜单对象menubar
root['menu'] = menubar #与根窗口对象root进行关联
submenu1 = Menu(menubar)
submenu2 = Menu(menubar)
#建立级联菜单
#为菜单对象添加子菜单：label=显示文本，menu=子菜单对象
#进制选择菜单
menubar.add_cascade(label='进制选择',menu=submenu1)
#在子菜单中添加命令按钮：label=显示文本，command=事件处理函数
submenu1.add_command(label='十进制',command=menu10)
submenu1.add_command(label='二进制',command=menu2)
submenu1.add_command(label='八进制',command=menu8)
submenu1.add_command(label='十六进制',command=menu16)
#帮助菜单
menubar.add_cascade(label="帮助",menu=submenu2)
submenu2.add_command(label="使用说明",command=Help)

#设置行与行（row）、列与列(column)之间的间隔（均为6）
root.grid_columnconfigure(0,pad = 6)
root.grid_columnconfigure(1,pad = 6)
root.grid_columnconfigure(2,pad = 6)
root.grid_columnconfigure(3,pad = 6)
root.grid_columnconfigure(4,pad = 6)
root.grid_columnconfigure(5,pad = 6)
root.grid_rowconfigure(0,pad = 6)
root.grid_rowconfigure(1,pad = 6)
root.grid_rowconfigure(2,pad = 6)
root.grid_rowconfigure(3,pad = 6)
root.grid_rowconfigure(4,pad = 6)
root.grid_rowconfigure(5,pad = 6)
root.grid_rowconfigure(6,pad = 6)

#使用grid方法布局
content = StringVar()#定义字符串的控制变量content
screen = Entry(root,textvariable = content,justify = RIGHT)#创建显示屏并使显示屏中的字体右对齐
screen.grid(row = 0,columnspan = 7,sticky = W + E)#将显示屏置于第零行，长度为7列，居中放置
Style().configure("TButton",padding=(0,6,0,6),font="arial 9")#设置按钮的风格、字体在按钮中的位置及大小

#定义所有的函数（注释以其中一部分为例）

def OnOneClick():#数字键1
    screen.insert(len(content.get()),"1") #在显示屏中输入“1”，并用get函数读取到content中
def OnTwoClick():#数字键2
    screen.insert(len(content.get()),"2")
def OnThreeClick():#数字键3
    screen.insert(len(content.get()),"3")
def OnFourClick():#数字键4
    screen.insert(len(content.get()),"4")
def OnFiveClick():#数字键5
    screen.insert(len(content.get()),"5")
def OnSixClick():#数字键6
    screen.insert(len(content.get()),"6")
def OnSevenClick():#数字键7
    screen.insert(len(content.get()),"7")
def OnEightClick():#数字键8
    screen.insert(len(content.get()),"8")
def OnNineClick():#数字键9
    screen.insert(len(content.get()),"9")
def OnZeroClick():#数字键0
    screen.insert(len(content.get()),"0")
def OnCClick():#清除键
    screen.delete(0,len(content.get()))#删除显示屏中所有字符
def OnBackClick():#退格键
    screen.delete(len(content.get()) -1)#删除显示屏最右侧的一个字符
def OnPlusClick():#加号键
    screen.insert(len(content.get()),"+")
    #在显示屏中输入“+”，并用get函数读取到content中
def OnMinusClick():#减号键
    screen.insert(len(content.get()),"-")
def OnDivideClick():#除号键
    screen.insert(len(content.get()),"/")
def OnMulClick():#乘号键
    screen.insert(len(content.get()),"*")
def OnDotClick():#小数点键
    screen.insert(len(content.get()),".")
def OnEqualClick():#等号键【十分关键】
    global i
    if i==10:#十进制
        try:#不出现异常时
            content.set(eval(content.get()))#用eval函数对content读取的字符串进行运算，并将运算后的结果设定为显示屏的内容
        except:#出现各种异常时
            content.set("Error")#在显示屏中显示出错
    elif i==2:#二进制
        try:
            s=content.get()#将content读取的字符串保存到变量s中
            s="0b"+s#在字符串前加表示二进制的符号“0b”
            content.set(bin(eval(s))[2:])#用bin(eval）函数对content读取的字符串进行二进制运算，并将运算后的结果（后加[2:]使得不显示“0b”）设定为显示屏的内容
        except:
            content.set("Error")#在显示屏中显示出错
    elif i==8:#八进制
        try:
            s=content.get()#将content读取的字符串保存到变量s中
            s="0o"+s#在字符串前加表示八进制的符号“0o”
            content.set(oct(eval(s))[2:])#用oct(eval）函数对content读取的字符串进行八进制运算，并将运算后的结果（后加[2:]使得不显示“0o”）设定为显示屏的内容
        except:
            content.set("Error")#在显示屏中显示出错
    elif i==16:#十六进制
        try:
            s=content.get()#将content读取的字符串保存到变量s中
            s="0x"+s#在字符串前加表示十六进制的符号“0x”
            content.set(hex(eval(s))[2:])#用hex(eval）函数对content读取的字符串进行十六进制运算，并将运算后的结果（后加[2:]使得不显示“0x”）设定为显示屏的内容
        except:
            content.set("Error")#在显示屏中显示出错
def OnPieClick():#π键
    screen.insert(len(content.get()),"3.141592653590")
def OnEClick():#e键
    screen.insert(len(content.get()),"2.718281828459")
def OnSinClick():#三角函数sin键
    screen.insert(len(content.get()),"math.sin(")
def OnCosClick():#三角函数cos键
    screen.insert(len(content.get()),"math.cos(")
def Leftbracket():#左括号键
    screen.insert(len(content.get()),"(")
def Rightbracket():#右括号键
    screen.insert(len(content.get()),")")
def Factorial():#阶乘运算键
    screen.insert(len(content.get()),"math.factorial(")
def Square():#平方运算键
    screen.insert(len(content.get()),"**2")
def Cubic():#立方运算键
    screen.insert(len(content.get()),"**3")
def ExSquare():#开平方运算键
    screen.insert(len(content.get()),"math.sqrt(")
def Ln():#自然对数运算键
    screen.insert(len(content.get()),"math.log(")
#十六进制时的数字键abcdef
def Sixteena():
    screen.insert(len(content.get()),"a")
def Sixteenb():
    screen.insert(len(content.get()),"b")
def Sixteenc():
    screen.insert(len(content.get()),"c")
def Sixteend():
    screen.insert(len(content.get()),"d")
def Sixteene():
    screen.insert(len(content.get()),"e")
def Sixteenf():
    screen.insert(len(content.get()),"f")

#定义所有的按钮（注释以其中一部分为例）
#空白键
start= Button(root,text="")
start.grid(row=1,column=0)
#清除键：按下该键时，显示屏中所有字符被删除
cls = Button(root,text="C",command=OnCClick)#root为窗体对象，显示文本为“C”，调用函数为OnCClick函数
cls.grid(row=1,column=1)#按钮的位置为第一行第二列
#阶乘运算键：按下该键时，显示屏中输入“math.factorial(”随后输入要计算的正整数和“)”“=”后得到结果
factorial = Button(root,text="n!",command=Factorial)#root为窗体对象，显示文本为“n!”，调用函数为Factorial函数
factorial.grid(row=1,column=2)#按钮的位置为第一行第三列
#退格键：按下该键时，将删除显示屏最右侧的一个字符
back = Button(root,text="←",command=OnBackClick)
back.grid(row=1,column=3)
#左括号键
left=Button(root,text="(",command=Leftbracket)
left.grid(row=1,column=4)
#右括号键
right=Button(root,text=")",command=Rightbracket)
right.grid(row=1,column=5)
#平方运算键：于数字后按下该键时，显示屏中输入“**2”，再输入“=”后得到结果
square=Button(root,text="x^2",command=Square)#显示文本为“n!”，调用函数为Square函数
square.grid(row=2,column=1)#按钮的位置为第二行第二列
#数字键7
seven = Button(root,text="7",command=OnSevenClick)
seven.grid(row=2,column=2)
#数字键8
eight = Button(root,text="8",command=OnEightClick)
eight.grid(row=2,column=3)
#数字键9
nine = Button(root,text="9",command=OnNineClick)
nine.grid(row=2,column=4)
#乘号键
mul = Button(root,text="*",command=OnMulClick)
mul.grid(row=2,column=5)
#数字键4
four = Button(root,text="4",command=OnFourClick)
four.grid(row=3,column=2)
#数字键5
five = Button(root,text="5",command=OnFiveClick)
five.grid(row=3,column=3)
#数字键6
six = Button(root,text="6",command=OnSixClick)
six.grid(row=3,column=4)
#减号键
mns = Button(root,text="-",command=OnMinusClick)
mns.grid(row=3,column=5)
#数字键1
one = Button(root,text="1",command=OnOneClick)
one.grid(row=4,column=2)
#数字键2
two = Button(root,text="2",command=OnTwoClick)
two.grid(row=4,column=3)
#数字键3
three = Button(root,text="3",command=OnThreeClick)
three.grid(row=4,column=4)
#加号键
plus = Button(root,text="+",command=OnPlusClick)
plus.grid(row=4,column=5)
#数字键0
zero = Button(root,text="0",command=OnZeroClick)
zero.grid(row=5,column=2)
#小数点键
dot = Button(root,text=".",command=OnDotClick)
dot.grid(row=5,column=3)
#除号键
divide = Button(root,text="/",command=OnDivideClick)
divide.grid(row=5,column=4)
#等号键
equal = Button(root,text="=",command=OnEqualClick)
equal.grid(row=5,column=5)
#π键
pie = Button(root,text="π",command=OnPieClick)
pie.grid(row=5,column=0)
#e键
e = Button(root,text="e",command=OnEClick)
e.grid(row=5,column=1)
#三角函数sin键   
sin = Button(root,text="sin",command=OnSinClick)
sin.grid(row=2,column=0)
#三角函数cos键 
cos = Button(root,text="cos",command=OnCosClick)
cos.grid(row=3,column=0)
#自然对数运算键
ln=Button(root,text="ln",command=Ln)
ln.grid(row=4,column=0)
#立方运算键
cubic=Button(root,text="x^3",command=Cubic)
cubic.grid(row=3,column=1)
#开平方运算键
exsquare=Button(root,text="√",command=ExSquare)
exsquare.grid(row=4,column=1)
#十六进制时的数字键abcdef
a = Button(root,text="a",command=Sixteena)
b = Button(root,text="b",command=Sixteenb)
c = Button(root,text="c",command=Sixteenc)
d = Button(root,text="d",command=Sixteend)
e = Button(root,text="e",command=Sixteene)
f = Button(root,text="f",command=Sixteenf)

root.mainloop()#事件循环
