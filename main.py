import Generator
import ErrorDetector
option = int(input("press 1 for Hamming code generation \npress 2 for Error checking\n"))
if(option==1):
    Generator.main()
elif(option==2):
    ErrorDetector.main()
else:
    print("invalid input")
#idkwhatimdoing
