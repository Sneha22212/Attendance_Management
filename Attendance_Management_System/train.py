from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")

        title_1 = Label(self.root, text='TRAIN DATASET', font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_1.place(x=0, y=0, width=1450, height=65)

        # Displaying images on the GUI
        img1 = Image.open("bgimages/im1.jpg")
        img1 = img1.resize((500, 300), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1) 
        label_1 = Label(self.root, image=self.photoimg1)
        label_1.place(x=0, y=50, width=500, height=300)

        img2 = Image.open("bgimages/im2.jpg")
        img2 = img2.resize((500, 300), Image.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2) 
        label_2 = Label(self.root, image=self.photoimg2)
        label_2.place(x=500, y=50, width=500, height=300)

        img3 = Image.open("bgimages/im3.jpg")
        img3 = img3.resize((500, 300), Image.LANCZOS)  
        self.photoimg3 = ImageTk.PhotoImage(img3) 
        label_3 = Label(self.root, image=self.photoimg3)
        label_3.place(x=1000, y=50, width=500, height=300)

        # Button to train data
        b1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, font=("times new roman", 35, "bold"), cursor="hand", fg="blue", bg="white")
        b1.place(x=0, y=350, width=1450, height=80)

        # Background image for the lower part of the window
        img4 = Image.open("frontpage button/photos.jpg")
        img4 = img4.resize((1500, 750), Image.LANCZOS)  
        self.photoimg4 = ImageTk.PhotoImage(img4) 
        label_4 = Label(self.root, image=self.photoimg4)
        label_4.place(x=0, y=420, width=1500, height=750)

    def train_classifier(self):
        data_dir = "data"
        
        # Filtering only .jpg and .png files
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png'))]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow('Training', imageNp)
                cv2.waitKey(1) == 13
            except Exception as e:
                print(f"Error processing {image}: {e}")
                continue

        ids = np.array(ids)

        # Train the classifier and save it
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training datasets completed")
        except Exception as e:
            messagebox.showerror("Error", f"Error during training: {e}")
            print(f"Error during training: {e}")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()



