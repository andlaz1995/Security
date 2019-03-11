import string
def isEnglish(input): # check if character is an english character
	try:
		input.encode(encoding='utf-8').decode('ascii')
	except UnicodeDecodeError:
		return False
	else:
		return True
def isAny(input): #check if character is space, digit or punctuation
    if input.isspace() or input.isdigit() or input in string.punctuation:
        return True
    else:
        return False

def hextobin(input):#convert hexadecimal to binary representation
	list1=[]
	for index, value in enumerate(input):
		list1.append(bin(int(value,16)+16)[3:])
	toreturn="".join(list1)
	return toreturn

def bin2string(input):#convert binary representation to ascii
    return ''.join(chr(int(input[i*8:i*8+8],2)) for i in range(len(input)//8))

def word2bin(input):#to convert the word into binary representation
	complete_bin=""

	for i in range(len(input)):
		bin_let = bin(ord(input[i]))[2:]
		bin_let = bin_let.rjust(8, '0')
		complete_bin = complete_bin + bin_let
	return complete_bin


with open("ciphertexts.txt", 'r') as inputfile:
        ciphertext = inputfile.readlines()
        ciphertext=[line.strip() for line in ciphertext]
        ciphertext_list= []
        for line in ciphertext:
        	ciphertext_list.append(hextobin(line))
        xor_list=[]
        which_xor=0
        for x in range(len(ciphertext_list)):
        	y=x+1
        	for y in range(y, len(ciphertext_list)):
        		which_xor+=1
        		a= int(ciphertext_list[x],2)
        		b=int(ciphertext_list[y],2)
        		temp=a^b
        		xor_list.append('{0:0{1}b}'.format(temp,len(ciphertext_list[x])))
        		y+=1
        		#print(which_xor , x+1 , y+1)				# This is to find out which ciphertexts were misencrypted
        	x+=1
        crib = word2bin("the") #the word to xor with the xored cyphertexts
        #thefile = open('list.txt', 'w')   #to output the information found to a file
        new_list=[]
        for m in range(0,len(xor_list)):       #AFTER WE HAVE FOUND WHICH OF THE XORS IS THE ONE WE CAN ATTACK WE DONT NEED TO PARSE THROUGH ALL OF THEM AGAIN
        	for i in range(0,len(xor_list[m]), 8): #skip 8 bits each time
        		z = xor_list[m][i:i+len(crib)]	#take the length of the crib from the xor_list so we can xor them
        		a= int(z,2)			#ciphertext part
        		b=int(crib,2)		#crib
        		temp=a^b 			#the xor process
        		xored_word = bin2string('{0:0{1}b}'.format(temp,len(z)))
        		i=0
        		for char in xored_word:
        			if isEnglish(char) == True or isAny(char) == True:
        				i+=1
        				if len(xored_word)==i:
        					print(m,xored_word)
            				#new_list.append(xored_word) #append this to a list if we want to   
        			else:
        				break
        	
        #thefile.write("%s\n" % new_list)   	# to output the information found to the file




        #z = xor_list[59][0:0+len(crib)]									#WHEN WE HAVE FOUND THE POSITION OF THE FIRST WORD WE CAN KEEP ADDING TO IT SO WE DONT NEED EXTRA LOOPS/SEARCHING AT ALL THE POSSIBLE POSITIONS
        #a= int(z,2)														#AND WE CAN USE THIS FUNCTION WITHOUT THE FOR LOOP
        #b=int(crib,2)
        #temp=a^b
        #print(bin2string('{0:0{1}b}'.format(temp,len(z))))
