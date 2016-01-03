import winsound
import tkinter
from PIL import ImageTk, Image
import sys,os
localdir = os.path.dirname(__file__)
localdir = sys.path[0]




root = tkinter.Tk()
root.minsize(1000,1000)
root.wm_title("Harrison Ford Sound Board")
print(localdir)

num_clips = 10

clips = []

for i in range(0,num_clips):
	fpath = sys.path[0] + '/content/' + str(i) + '.wav'
	clips.append(fpath)


def playClip(clip_num):
	winsound.PlaySound(clips[clip_num], winsound.SND_FILENAME)	


photo = ImageTk.PhotoImage(Image.open(r'C:/Users/Bash/Downloads/harrison.jpg'))


image_label = tkinter.Label(root, height = 295, width = 236, image=photo);
image_label.pack()
image_label.place(bordermode = 'inside', x = 0, y = 0)


buttons = []

for i in range(0,num_clips):
	print(i)
	buttons.append(tkinter.Button(root, text = str(i), command = lambda i=i: playClip(i)))
	buttons[i].pack()
	buttons[i].place(x=600,y=i*40)



root.mainloop()