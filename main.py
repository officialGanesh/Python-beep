# import required module
import winsound

def Beep_sound():
    """This function is used to generate beep sound """

    frequency ,duration = 2500 ,5000
    return winsound.Beep(frequency,duration)

    
if __name__ == '__main__':

    Beep_sound()
    print("Code Completed")