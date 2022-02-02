
word =["juego"]
max_tries= 5
len_word= len(word[0])

for ii in range(max_tries):
    trial= input("Introduce a " + str(len_word) + " letter word, you have " + str(max_tries-ii) + " oportunities more: ")
    while (len(trial)!= len_word):
        trial= input(" Try again, this time with a " + str(len_word) + " letter word: ")
    result=[]
    for jj in range(len_word):
        result.append(-1)
        print(word[0][jj] , trial[jj])
        if(word[0][jj]==trial[jj]):
            print("entra")
            result[jj]=1
        else:
            for kk in range(len_word):
                if(word[0][kk]==trial[jj]):
                    result[jj]=0
    print(result)
