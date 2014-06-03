import wx
import random
from specialInput import *
from specialOutput import *

class HundredWordCut(wx.Frame):
    def __init__(self, parent):
	wx.Frame.__init__(self, parent, wx.ID_ANY, "Hundred Word Cut",size=(630,600))

	self.panel = wx.Panel(self)
        self.wordList=WordList()
        self.notYet=NotYet()
        self.cutted=Cutted()
        self.name1=self.name2=self.name3=self.name4=''

        self.Word=wx.StaticText(self.panel,-1, pos=(100,50))

        self.btnImage1 = wx.BitmapButton(self.panel, -1, pos=(100, 100),size=(200,200))
        self.Bind(wx.EVT_BUTTON, self.OnClick1, self.btnImage1)


        self.btnImage2 = wx.BitmapButton(self.panel, -1, pos=(320, 100),size=(200,200))
        self.Bind(wx.EVT_BUTTON, self.OnClick2, self.btnImage2)


        self.btnImage3 = wx.BitmapButton(self.panel, -1, pos=(100, 320),size=(200,200))
        self.Bind(wx.EVT_BUTTON, self.OnClick3, self.btnImage3)


        self.btnImage4 = wx.BitmapButton(self.panel, -1, pos=(320, 320),size=(200,200))
        self.Bind(wx.EVT_BUTTON, self.OnClick4, self.btnImage4)


        self.Reset()
	self.btnCut = wx.Button(self.panel, label="Cut", pos=(400, 50))
	self.btnCut.Bind(wx.EVT_BUTTON, self.Cut)
        
    def Reset(self):
        self.notYet=NotYet()
        self.cutted=Cutted()
        if len(self.notYet)==0:
            self.theEnd()

        else:
            self.current=self.notYet[random.randint(0,len(self.notYet)-1)]
            self.Word.SetLabel(self.wordList[self.current-1])

            self.randomName()

            self.bmp1 = wx.Image(self.name1+".jpg").ConvertToBitmap()
            self.btnImage1.SetBitmapLabel(self.bmp1)

            self.bmp2 = wx.Image(self.name2+".jpg").ConvertToBitmap()
            self.btnImage2.SetBitmapLabel(self.bmp2)

            self.bmp3 = wx.Image(self.name3+".jpg").ConvertToBitmap()
            self.btnImage3.SetBitmapLabel(self.bmp3)

            self.bmp4 = wx.Image(self.name4+".jpg").ConvertToBitmap()
            self.btnImage4.SetBitmapLabel(self.bmp4)

            
    def randomName(self):
        self.name1=self.wordList[self.current-1]

        self.name2=self.wordList[random.randint(0,len(self.wordList)-1)]
        while self.name1==self.name2:
            self.name2=self.wordList[random.randint(0,len(self.wordList)-1)]

        self.name3=self.wordList[random.randint(0,len(self.wordList)-1)]
        while self.name1==self.name3 or self.name3==self.name2:
            self.name3=self.wordList[random.randint(0,len(self.wordList)-1)]

        self.name4=self.wordList[random.randint(0,len(self.wordList)-1)]
        while self.name1==self.name4 or self.name2==self.name4 or self.name3==self.name4:
            self.name4=self.wordList[random.randint(0,len(self.wordList)-1)]

        self.right=random.randint(1,4)

        if self.right==2:
            self.name1, self.name2=self.name2, self.name1

        if self.right==3:
            self.name1, self.name3=self.name3, self.name1
        
        if self.right==4:
            self.name1, self.name4=self.name4, self.name1

    def Cut(self,e):
        self.notYet.remove(self.current)
        self.cutted.append(self.current)
        NewNotYet(self.notYet)
        NewCutted(self.cutted)
        self.Reset()

    def theEnd(self):
        wx.MessageBox("You Win!")
        Redo()

    def OnClick1(self,e):
        if self.right==1:
            self.Reset()
        else:
            wx.MessageBox("No! It's "+self.name1)
        
    def OnClick2(self,e):
        if self.right==2:
            self.Reset()
        else:
            wx.MessageBox("No! It's "+self.name2)
        
    def OnClick3(self,e):
        if self.right==3:
            self.Reset()
        else:
            wx.MessageBox("No! It's "+self.name3)
        
    def OnClick4(self,e):
        if self.right==4:
            self.Reset()
        else:
            wx.MessageBox("No! It's "+self.name4)
        






#-----------------------------------------------------#
app = wx.App(False)
frame = HundredWordCut(None)
frame.Show()
app.MainLoop()
