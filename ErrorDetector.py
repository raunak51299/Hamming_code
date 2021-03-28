def main():
    option = int(input("enter 1 for left to right and 2 for right to left"))
    if(option == 1):
        print('Enter the hamming code received')
        d=input()
        m = len(str(d))
        nr=0
        for i in range(m): #calculate number of parity bits
            if(2**i >= m + i + 1):
                nr = i


        d = [int(i) for i in str(d)]
        n = len(d)
        res = 0

        # Calculate parity bits 
        for i in range(nr):
            val = 0
            for j in range(1, n + 1):
                if(j & (2**i) == (2**i)):
                    val = val ^ int(d[-1 * j])
            # Create a binary no by appending parity bits together.
            res = res + val*(10**i)
        # Convert binary to decimal
        position = int(str(res), 2)# bin to decimal
        print("position of error is ",position," from left")

        position = m-position
        if(d[position] == 1):#correction of error
            d[position] = 0
        else:
            d[position] = 1

        string_ints = [str(int) for int in d]
        d = "".join(string_ints)

        print("corrected code is ","".join(str(d)))

    elif(option == 2):
        print('Enter the hamming code received')
        d=input()
        m = len(str(d))
        nr=0
        for i in range(m): #calculate number of parity bits
            if(2**i >= m + i + 1):
                nr = i


        d = [int(i) for i in str(d)]
        n = len(d)
        res = 0

        # Calculate parity bits again
        for i in range(nr):
            val = 0
            for j in range(1, n + 1):
                if(j & (2**i) == (2**i)):
                    val = val ^ int(d[-1 * j])
            # Create a binary no by appending
            # parity bits together.
            res = res + val*(10**i)
        # Convert binary to decimal
        position = int(str(res), 2)# bin to decimal
        print("position of error is ",position," from right")

        position = m-position
        if(d[position] == 1):#correction of error
            d[position] = 0
        else:
            d[position] = 1

        string_ints = [str(int) for int in d]
        d = "".join(string_ints)

        print("corrected code is ","".join(str(d)))
    else:
        print("invalid option.")

if __name__ == '__main__':
    main()
