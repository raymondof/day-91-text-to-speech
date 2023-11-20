from reader import Reader
from polly_TTS import TTS
from sound_player import SoundPlayer
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os

root = Tk()
root.title("PDF To Speech PTS")
root.geometry("400x300")

# variable to store selectable file path
pdf_filepath_var = StringVar()
pdf_filepath_var.set("No file selected")
pdf_filepath = ""

tts = TTS()
play_sound = False
sound_player = SoundPlayer()


def select_file():
    global pdf_filepath
    pdf_filepath = filedialog.askopenfilename()
    pdf_name, pdf_extension = return_file_name(pdf_filepath)
    print("Selected:", pdf_name, pdf_extension)
    print("Which type is:", type(pdf_filepath))
    pdf_name_with_extension = f"{pdf_name}{pdf_extension}"
    pdf_filepath_var.set(pdf_name_with_extension)


def convert_to_mp3():
    global pdf_filepath, mp3_path
    if pdf_filepath_var != "":
        pdf_string = read_pdf(pdf_filepath)
        pdf_name, pdf_extension = return_file_name(pdf_filepath)
        mp3_path = pdf_to_speech(pdf_string, pdf_name)
        print(f"output path {mp3_path}")
        sound_player.set_path(mp3_path)
    else:
        messagebox.showerror("No file selected", "You haven't selected PDF to read.")


def read_pdf(filepath):
    reader = Reader(filepath)
    story = reader.read()
    return story

def pdf_to_speech(pdf, name):
    output_path = tts.text_to_speech(pdf, name)
    return output_path
    # sound_player = SoundPlayer(output_path)


def play_pause_mp3():
    global play_sound

    if not play_sound:
        sound_player.play_sound()
        play_sound = True
    else:
        sound_player.pause_sound()
        play_sound = False

def return_file_name(filepath):
    """Function to split a file path and return the file name without extension"""
    # Use os.path to split the file path
    file_dir, file_name = os.path.split(filepath)

    # Split the file name from its extension
    file_name_without_extension, file_extension = os.path.splitext(file_name)
    return file_name_without_extension, file_extension

# Set buttons
add_file_button = tkinter.Button(root, width=8, text="Open file", command=select_file)
add_file_button.grid(column=2, row=0, sticky=E)

convert_to_mp3_button = tkinter.Button(root, width=15, text="Convert to speech", command=convert_to_mp3)
convert_to_mp3_button.grid(column=1, row=1, sticky=E)

play_pause_button = tkinter.Button(root, width=8, text="Play / Pause", command=play_pause_mp3)
play_pause_button.grid(column=2, row=1)

# Set labels
ttk.Label(root, text="Filename: ").grid(column=0, row=0, sticky=E)
ttk.Label(root, textvariable=pdf_filepath_var).grid(column=1, row=0, sticky=W)

root.mainloop()
