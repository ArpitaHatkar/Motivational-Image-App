from tkinter import*
from requests import*
from PIL import Image,ImageTk


root = Tk()
root.geometry("1000x1000+300+300")
root.configure(bg = "light blue")
root.title("Motivational Image App")
f = ("Arial",30,"bold")

lab_si = Label(root)
lab_si.pack(pady=10)


def gi():
	try:
		url = "https://zenquotes.io/api/image"
		res = get(url)
		try:
			with open("Mi.png","wb") as f:
				f.write(res.content)
			img = Image.open("mi.png")
			imgtk = ImageTk.PhotoImage(image=img)
			lab_si.configure(image=imgtk)
			lab_si.photo = imgtk
		except Exception as e:
			print("file issue",e)
	except Exception as e:
		print("issue",e)
	root.after(10000,gi)
gi()


root.mainloop()