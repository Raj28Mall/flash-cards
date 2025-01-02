import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# ----------------------------Backend---------------------------- #
df=pd.read_csv('./data/french_words.csv')
language_data=df.to_dict(orient='records')

def new_word():
    canvas.itemconfig(text_text,text=language_data[random.randint(0,len(language_data)-1)]['French'])

# ----------------------------UI---------------------------- #
window=tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

card_front=tkinter.PhotoImage(file='./images/card_front.png')
card_back=tkinter.PhotoImage(file='./images/card_back.png')
right=tkinter.PhotoImage(file='./images/right.png')
wrong=tkinter.PhotoImage(file='./images/wrong.png')

canvas=tkinter.Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400,263, image=card_front)
language_text=canvas.create_text(400,150, text='French', font=('Ariel', 25, 'italic'))
text_text=canvas.create_text(390,263,text='Text', font=('Ariel', 45, 'bold'))
canvas.grid(column=0,row=0,columnspan=2)

right_button=tkinter.Button(image=right, highlightthickness=0, command=new_word)
right_button.grid(column=1, row=1)

wrong_button=tkinter.Button(image=wrong, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)
window.mainloop()

