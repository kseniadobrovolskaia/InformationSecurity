from functools import partial

from ksdyn.core import KeystrokeCaptureData
from ksdyn.model import Fingerprint, FingerprintDatabase
from ksdyn.sugar import create_fingerprint_from_capture_data

DATA_DIR= "data/"


example_text1='''Information security is the best!'''

def get_some_keystrokes():
    print("Write this text. In the end press Ctrl+C.")
    print("------------------")
    print(example_text1)
    data= KeystrokeCaptureData()
    try:
        import capture_keys
        capture_keys.start(data.on_key)
    except KeyboardInterrupt:
        pass
    print("\n")
    return data

def create_fingerprint():
    username= input("What is your name? ")
    data= get_some_keystrokes()
    data.save_to_file( DATA_DIR+username )
    fingerprint= create_fingerprint_from_capture_data( username, data )
    fingerprint.save_to_file( DATA_DIR+username )
    print("Your data created sucsessfully!")

def match_fingerprint():
    db= FingerprintDatabase().load_from_dir( DATA_DIR )
    data= get_some_keystrokes()
    f= create_fingerprint_from_capture_data( "TestPerson", data )
    best= db.best_match( f )
    print("You are: ", best.name)

if __name__=='__main__':
    print("Choose action:\n  1. Write new data.\n  2. Match text to a existing data.")
    try:
        option= int(input())
    except Exception:
        print("Option must be 1 or 2")
        exit()
    print("\n\n")
    if option==1:
        create_fingerprint()
    elif option==2:
        match_fingerprint()
    else:
        print("Option must be 1 or 2")

