
from PIL import ImageGrab
import cv2
import numpy as np
from tkinter import *

def record_screen():
    try:
        
        image = ImageGrab.grab()
        img_np_arr = np.array(image)
        shape = img_np_arr.shape
        print(f"Screen Resolution: {shape[1]}x{shape[0]}")

       
        screen_cap_writer = cv2.VideoWriter(
            'screen_recorded.avi',
            cv2.VideoWriter_fourcc(*'MJPG'),
            20,  # FPS
            (shape[1], shape[0])
        )

        
        scale_by_percent = 50
        width = int(shape[1] * scale_by_percent / 100)
        height = int(shape[0] * scale_by_percent / 100)
        new_dim = (width, height)

        print("Recording started... Press 'e' to stop.")

        while True:
            
            image = ImageGrab.grab()
            img_np_arr = np.array(image)
            final_img = cv2.cvtColor(img_np_arr, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV
            screen_cap_writer.write(final_img)

            
            resized_image = cv2.resize(final_img, new_dim)
            cv2.imshow("Recording Preview (Press 'e' to exit)", resized_image)

            
            if cv2.waitKey(1) == ord('e'):
                print("Recording stopped.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
       
        screen_cap_writer.release()
        cv2.destroyAllWindows()


def setup_gui():
    screen_recorder = Tk()
    screen_recorder.geometry("340x220")
    screen_recorder.title("Swami Screen Recorder")

    try:
        bg_img = PhotoImage(file="C:/Users/91893/Downloads/pngwing.com.png")
        label1 = Label(screen_recorder, image=bg_img, bd=0)
        label1.image = bg_img  # Keep a reference to prevent garbage collection
        label1.pack()
    except Exception as e:
        print(f"Background image error: {e}")

    title_label = Label(screen_recorder, text="Swami Screen Recorder", font=("Ubuntu Mono", 16), bg="#02b9e5")
    title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    info_label = Label(screen_recorder, text="Press 'e' to exit screen recording", bg="#02b9e5")
    info_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    screen_button = Button(screen_recorder, text="Record Screen", command=record_screen, relief=RAISED)
    screen_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    screen_recorder.mainloop()


setup_gui()
