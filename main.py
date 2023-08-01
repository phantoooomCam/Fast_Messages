import keyboard
import time

ENTER = "enter"
HOTKEY = "esc"  #Detener el script
FILE_NAME= "file.txt"
EXIT = False

def salir() -> None:
    global EXIT
    EXIT = True
    print("The exit of the program is activated...")

def send_message(msg: str = "Hola!") -> None:
    keyboard.write(msg)
    keyboard.press(ENTER)
    print(f"SENT: {msg=}")


def main() -> None:
    keyboard.add_hotkey(HOTKEY,lambda: salir())
    print("Waiting...")
    time.sleep(5)

    with open(FILE_NAME, "r") as archivo:
        for line in archivo:
            list_word = line.split()
            for word in list_word:
                time.sleep(0.2) #this if you want to add more time between the each message 
                if EXIT:
                    exit()
                send_message(word.strip())

if __name__ == "__main__": 
    main()

