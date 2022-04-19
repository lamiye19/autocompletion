# Author : Sémiat Oyénikè Olaitan
# Date : 18 Avril 2022
#
# This program displays, for each word of a list of words entered by a
# distracted Internet user, the word closest to the dictionary and the cost
# of completion.
# 
# The closest word to the dictionary represents the lowest cost word that
# can be obtained from the user's word that is in the dictionary.

def autocompletion(dictionnary, words):
    print(dictionnary)
    print(words)
    for word in words:
        the_word = word
        tmp_word = word
        cost = 0
        for dic in dictionnary:
            char_deleted = 0
            char_added = 0
            char_replaced = 0
            char_switched = 0
            
            if dic.find(word[0]) != -1:
                # print(dic)
                char_added = dic.find(word[0])
                sub_dic = [dic[i] for i in range(len(dic)) if i > char_added]
                if len(word) == 1:
                    char_added = len(sub_dic)
                else:
                    i = 1

                    if char_added!= 0 and word[1] == dic[char_added - 1]:
                        char_added = char_added - 1
                        char_switched = char_switched + 1
                        i = 2

                    sub_word = word + "1"


                    while i < len(sub_word)-1:
                            if len(sub_dic) < 2:
                                sub_dic.append("0")
                                sub_dic.append("0")

                            # print(sub_word[i]+ ";" +sub_dic[0]+ "," +sub_dic[1])

                            if sub_word[i] != sub_dic[0]:
                                if sub_word[i] == sub_dic[1]:
                                    if sub_word[i + 1] == sub_dic[0]:
                                        char_switched = char_switched + 1
                                        # print("switch 0")
                                        sub_dic = sub_dic[2:]
                                        i = i + 1
                                    else:
                                        char_added = char_added + 1
                                        # print("del")
                                        sub_dic = sub_dic[2:]
                                elif sub_word[i+1] == sub_dic[0]:
                                    char_deleted = char_deleted + 1
                                    # print("add")
                                elif sub_word[i + 1] == sub_dic[1]:
                                    char_replaced = char_replaced + 1
                                    # print("replace")
                                    sub_dic = sub_dic[1:]
                                else:
                                    #sub_dic = sub_dic[1:]
                                    char_deleted = char_deleted + 1
                            else:
                                sub_dic = sub_dic[1:]

                            i = i+1


                sub_cost = 2*(char_deleted + char_added) + 3*(char_replaced + char_switched)

                if len(dic)-char_added+char_deleted == len(word):
                    if cost == 0 or cost > sub_cost:
                        cost = sub_cost
                        tmp_word = dic
                if cost == sub_cost:
                    tmp_word = dic if dic < the_word else tmp_word

                the_word = tmp_word
                # print(dic+": " + str(sub_cost))

        print("\t"+word+"\t->\t"+the_word+": "+str(cost))

if __name__ == '__main__':
    dictionnary1 = ["algorithme", "ahgorithme", "arbre", "barbe", "globe",\
     "orbe", "tac","bulbizarre", "herbizarre", "carapuce", "salameche"]

    words1 = ["rythme", "arbore", "logarithme", "lobe", "robe", "talc",\
    "carteapuce", "salamuce", "saramuce", "blubizarre", "herbebizarre", "xxxbizarre"]

    print("*** Test 1")
    autocompletion(dictionnary1, words1)
