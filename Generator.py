def main():
    option = int(input("press 1 for left to right generation \npress 2 for right to left generation\n"))
    if(option==1):
        print('Enter the data bits')
        d=input()
        data=list(d)
        #data.reverse()
        c,ch,j,r,h=0,0,0,0,[]
        ''' 
            r : number of parity bit
            h : hamming code
        '''
        while ((len(d)+r+1)>(pow(2,r))):#calculating number of parity bit
            r=r+1

        for i in range(0,(r+len(data))):#putting the data bits in their corresponding index
            p=(2**c)

            if(p==(i+1)):
                h.append(0)
                c=c+1

            else:
                h.append(int(data[j]))
                j=j+1

        for parity in range(0,(len(h))):
            ph=(2**ch)
            if(ph==(parity+1)):
                startIndex=ph-1
                i=startIndex
                toXor=[]

                while(i<len(h)):
                    block=h[i:i+ph]
                    toXor.extend(block)
                    i+=2*ph

                for z in range(1,len(toXor)):
                    h[startIndex]=h[startIndex]^toXor[z]
                ch+=1

        
        print('Hamming code generated from right to left is:- ', end="")
        print(str(''.join(map(str, h))))
    elif (option==2):
        print('Enter the data bits')
        d=input()
        data=list(d)
        data.reverse()
        c,ch,j,r,h=0,0,0,0,[]

        while ((len(d)+r+1)>(pow(2,r))):
            r=r+1

        for i in range(0,(r+len(data))):
            p=(2**c)

            if(p==(i+1)):
                h.append(0)
                c=c+1

            else:
                h.append(int(data[j]))
                j=j+1

        for parity in range(0,(len(h))):
            ph=(2**ch)
            if(ph==(parity+1)):
                startIndex=ph-1
                i=startIndex
                toXor=[]

                while(i<len(h)):
                    block=h[i:i+ph]
                    toXor.extend(block)
                    i+=2*ph

                for z in range(1,len(toXor)):
                    h[startIndex]=h[startIndex]^toXor[z]
                ch+=1

        h.reverse()
        print('Hamming code generated from right to left is:- ', end="")
        print(str(''.join(map(str, h))))
    else:
        print("invalid bruh")

    
if __name__ == '__main__':
    main()