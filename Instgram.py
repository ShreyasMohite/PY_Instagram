#===================
from tkinter import *
import tkinter.messagebox
from instaloader import *
from PIL import ImageTk
from PIL import *

#===================

class insta:
     def __init__(self,root):
          self.root=root
          self.root.title("Instagram")
          self.root.geometry("500x300")
          self.root.iconbitmap("insta.ico")
          self.root.resizable(0,0)

          user=StringVar()
          count=IntVar()

          post=IntVar()
          pic=IntVar()
          tagged_pic=IntVar()

          global pos,pics,tp


          insta=Instaloader()


#==============================================================================
#-============================================================================
#this thing work same as the hover effect
#but you need to specify where to use it [it only used in button so make sure you should assign the button name and bind it in buttion ]
          
          def on_enter1(e):
            But_Down['background']="black"
            But_Down['foreground']="cyan"
               
               

          def on_leave1(e):
            But_Down['background']="SystemButtonFace"
            But_Down['foreground']="SystemButtonText"


          def on_enter2(e):
            But_Hash['background']="black"
            But_Hash['foreground']="cyan"
               
               

          def on_leave2(e):
            But_Hash['background']="SystemButtonFace"
            But_Hash['foreground']="SystemButtonText"

          
          def on_enter3(e):
            But_Clear['background']="black"
            But_Clear['foreground']="cyan"
               
               

          def on_leave3(e):
            But_Clear['background']="SystemButtonFace"
            But_Clear['foreground']="SystemButtonText"
#========================================================
#==================================================
            #to clear the entries

          def clear():
             user.set("")
             count.set("")

#==========================================================================
             #this download all user post and saves in the location 
          def posts():
               global pos              
               if post.get()==1:
                    pos=True                    
                    #insta.download_profile({''}.format(user), profile_pic=True
               else:                   
                    pos=False
          posts()
          
#===============================================================
          #user can download only their profile pic if they want they do not have any other details in it

          def profiles_pics():
               global pics              
               if pic.get()==1:
                  pics=True                  
                    #insta.download_profile(user, profile_pic_only=True)
               else:                   
                    pics=False
          profiles_pics()
                    
#===================================================================
          #taged_pic is used in checkboxes to identify either its is check or not as per user requirement
          #and only downloads user taged pictures from insta
          #it downloads all the pictures in user profiles 

          def taged_pic():
               global tp                         
               if tagged_pic.get()==1:
                  tp=True                  
               else:                    
                     tp=False
          taged_pic()
                   
#===============================================================
          #downloads the pictures using hashtags
          #you can specify the number of pictures you want to download in given box

          def hashtags():
                    try:
                         if count.get()=="":
                              tkinter.messagebox.askretrycancel("Error","Please Enter some number ","error")
                         else:
                              insta=Instaloader()
                              insta.download_hashtag(user.get(),max_count=count.get())
                    except:
                         tkinter.messagebox.askretrycancel("Error","Network Error/Use only number")
#================================
                         #download function which takes the inputs from checkboxes and places in insta
          def download():
               names=user.get()
               try:
                    if names=="":
                         tkinter.messagebox.askretrycancel("Error","Please enter name ?","info")
                    else:
                         insta=Instaloader()
                         insta.download_profile(user.get(),profile_pic=pos, profile_pic_only=pics, fast_update=False, download_stories=False, download_stories_only=False, download_tagged=False, download_tagged_only=tp, post_filter=None, storyitem_filter=None)                                                
               except:
                    tkinter.messagebox.askretrycancel("Error","Network error or Invalid user")

#=====================================================================#
                    #this is the main frame
          MainFrame=Frame(self.root,width=500,height=300,relief="sunken",bd=3)
          MainFrame.place(x=0,y=0)

#=====================================================================#
          #this is used to add images in background of frame

          self.original1 = Image.open ("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Instagrampy\\instagrams.jpg")
          resized1 = self.original1.resize((495, 300),Image.ANTIALIAS)
          self.image1 = ImageTk.PhotoImage(resized1)
          bglab1=Label(MainFrame,image=self.image1,bd=1).place(x=0,y=0)
#=====================================================================#
          
          Lab_User=Label(MainFrame,text="Enter User Name :",bg="black",fg="white",font=("times new roman",12,"bold"))
          Lab_User.place(x=10,y=10)


          Ent_User=Entry(MainFrame,relief="sunken",textvariable=user,bd=3,font=("times new roman",12,"bold"),width=15)
          Ent_User.place(x=10,y=50)

          Lab_Count=Label(MainFrame,text="Count Number :",bg="black",fg="white",font=("times new roman",12,"bold"))
          Lab_Count.place(x=350,y=10)

          Ent_count=Entry(MainFrame,relief="sunken",textvariable=count,bd=3,font=("times new roman",12,"bold"),width=15)
          Ent_count.place(x=350,y=50)


          Lab_Downloadby=Label(MainFrame,text="Downloaded By:",bg="black",fg="white",font=("times new roman",12,"bold"))
          Lab_Downloadby.place(x=180,y=70)

          post_pic=Checkbutton(MainFrame,cursor="hand2",text="Posts",bg="black",fg="red",variable=post,command=posts,onvalue=1,offvalue=0,font=("times new roman",12,"bold"))
          post_pic.place(x=30,y=185)

          profile_pic=Checkbutton(MainFrame,cursor="hand2",bg="black",fg="red",text="Profile_pic_only",variable=pic,command=profiles_pics,onvalue=1,offvalue=0,font=("times new roman",12,"bold"))
          profile_pic.place(x=180,y=185)


          taged_pic=Checkbutton(MainFrame,cursor="hand2",bg="black",fg="red",text="Tagged_pic_only",variable=tagged_pic,command=taged_pic,onvalue=1,offvalue=0,font=("times new roman",12,"bold"))
          taged_pic.place(x=340,y=185)

#==========================================================================#
#the hover effect is bind here ,make sure that the name you have provided in function should be same while binding

          But_Down=Button(MainFrame,text="Download Profile",command=download,font=("times new roman",12,"bold"),width=15,bd=3,cursor="hand2")
          But_Down.place(x=10,y=240)
          But_Down.bind("<Enter>",on_enter1)
          But_Down.bind("<Leave>",on_leave1)

          But_Hash=Button(MainFrame,text="Download Hashtags",command=hashtags,font=("times new roman",12,"bold"),width=15,bd=3,cursor="hand2")
          But_Hash.place(x=180,y=240)
          But_Hash.bind("<Enter>",on_enter2)
          But_Hash.bind("<Leave>",on_leave2)

          But_Clear=Button(MainFrame,text="Clear",command=clear,font=("times new roman",12,"bold"),width=10,bd=3,cursor="hand2")
          But_Clear.place(x=370,y=240)
          But_Clear.bind("<Enter>",on_enter3)
          But_Clear.bind("<Leave>",on_leave3)




#=====================================================================#

if __name__ == "__main__":
    root=Tk()
    app=insta(root)
    root.mainloop()
