import os
from text_to_audio import text_to_speech_file
import time
def text_to_audio(folder):
    with open(f"user_uploads/{folder}/desc.txt" , "r") as f:
        text = f.read()
    text_to_speech_file(text , folder)
def create_reels(folder):
    print("cc-" , folder)

if __name__ == "__main__":
    # folder = "73373....."
    while True:
        print("processing queu....!!!")
        with open("done.txt","r") as f:
            done_folder = f.readlines()
        done_folder = [f.strip() for f in done_folder]
        folders = os.listdir("user_uploads")
        # print(folders,done_folder)
        for folder in folders:
            if folder not in done_folder:
                text_to_audio(folder)#generate the audio from desc.txt
                create_reels(folder)# convert the images inside the folder to a reel
                with open("done.txt","a") as f:
                    f.write(folder + "\n")
        time.sleep(4)

