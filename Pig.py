end = 0
while(end == 0):
    word = input("Введите слово: ")
    if word[0] == '1' or word[0] == '2' or word[0] == '3' or word[0] == '4' or word[0] == '5' or word[0] == '6' or word[0] == '7' or word[0] == '8' or word[0] == '9' or word[0] == '0':
        print("Цифры в начале слова не допустимы")
        break
    if word[0] == "e" or word[0] == "a" or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y':
        print(word + 'way')
    else:
        print(word[1:] + word[0] + 'ay' )
    end = 1
