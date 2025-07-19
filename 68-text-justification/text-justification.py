class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        textjustlist = []
        lettersleft = maxWidth
        sublist = []
        len_sub = 0
        for word in words:
            if lettersleft-len(word)>=0:
                ## Can accommodate the current word
                sublist.append(word)
                len_sub+=1
                lettersleft = lettersleft-(len(word)+1)
            else:
                lettersleft += 1
                if len_sub>1:
                    spaces = lettersleft//(len_sub-1)
                    remainder = lettersleft%(len_sub-1)
                    make_str = ""
                    last_word = sublist.pop(-1)
                    for text in sublist:
                        make_str += (text+" "*(spaces+1))
                        if remainder:
                            make_str+=(" ")
                            remainder -= 1

                    make_str+=(last_word)
                else:
                    make_str = sublist[0]+" "*lettersleft


                textjustlist.append(make_str)
                sublist = []
                sublist.append(word)
                len_sub=1
                lettersleft = maxWidth-(len(word)+1)

        if len_sub==1:
            make_str = sublist[0]+" "*(lettersleft+1)

            textjustlist.append(make_str)
        else:
            make_str = ""
            last_word = sublist.pop(-1)
            for text in sublist:
                make_str += (text+" "*(1))
            make_str+=(last_word)
            make_str = make_str+" "*(lettersleft+1)


            textjustlist.append(make_str)

        
        return textjustlist
                

        