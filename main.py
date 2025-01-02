import tkinter
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
word={}
# ----------------------------Backend---------------------------- #

try:
    data=pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data=pd.read_csv('./data/french_words.csv')
finally:
    language_data=data.to_dict(orient='records')    

def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word=random.choice(language_data)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(text_text,text=word['French'], fill='black')
    canvas.itemconfig(language_text,text='French', fill='black')
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(text_text,text=word['English'], fill='white')
    canvas.itemconfig(language_text,text='English', fill='white')

def correct_guess():
    global word
    language_data.remove(word)
    data=pd.DataFrame(language_data)
    data.to_csv('./data/words_to_learn.csv', index=False)
    next_card()

# ----------------------------UI---------------------------- #
window=tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

flip_timer=window.after(3000,func=flip_card)

card_front=tkinter.PhotoImage(file='./images/card_front.png')
card_back=tkinter.PhotoImage(file='./images/card_back.png')
right=tkinter.PhotoImage(file='./images/right.png')
wrong=tkinter.PhotoImage(file='./images/wrong.png')

canvas=tkinter.Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image=canvas.create_image(400,263, image=card_front)
language_text=canvas.create_text(400,150, text='', font=('Ariel', 25, 'italic'))
text_text=canvas.create_text(390,263,text='', font=('Ariel', 45, 'bold'))
canvas.grid(column=0,row=0,columnspan=2)

right_button=tkinter.Button(image=right, highlightthickness=0, command=correct_guess)
right_button.grid(column=1, row=1)

wrong_button=tkinter.Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
next_card()
window.mainloop()

