# __TODO__줄입력 받아서 단어 삭제
import random
if __name__ == "__main__":                                                 
    def test():
        print("--------------시험 시작 !!--------------\n")
        words = {}
        words_copy = {}
        f = open("C:/Users/user/Documents/Programming/pyPrac/afterPython/wordNote.txt", "rt", encoding="UTF-8")
        mode = input("한국어:1 영어:2\n")
        print("\n")
        while True:
            line = f.readline()
            if not line: break
            line = line.split(':')
            words[line[0]] = line[1].rstrip("\n")
            words_copy = words.copy()
        f.close()
        if mode == '2':
            words = {v: k for k, v in words.items()}
        while True:
            count = numOfWords = 0
            keys = words.keys()
            keys = list(keys)
            random.shuffle(keys)
            for v in keys:
                question = words[v]
                answer = input(v + " : ")
                numOfWords += 1
                if question == answer:
                    print("정답!\n")
                    count += 1
                    del words[v]
                else:
                    print("오답, 정답은 " + question + " 입니다.\n")

            print(f"당신의 점수는 {round(count/numOfWords*100,3)}")
            wyw = input("처음부터 다시풀기:1 오답만 다시풀기:2 시험종료:3\n")
            if wyw == '1':
                words = words_copy.copy()
            elif wyw == '2':
                continue
            elif wyw == '3':
                break

    def addWord(word,meaning):
        with open("wordNote.txt","a", encoding='UTF-8') as f:
            f.write("\n" + word + ":" + meaning)
    
    def showNote():
        print("-----------------------------")
        with open("WordNote.txt","r",encoding="UTF-8") as f:
            Nline = 1
            while True:
                line = f.readline()
                if not line: break
                line = line.rstrip("\n")
                print(f"{Nline} {line}")          
                Nline += 1
        print("-----------------------------\n\n")     
    
    def delWord(N):
        note = []
        with open("WordNote.txt","r",encoding="UTF-8") as f:
            cnt = 0
            while True:
                cnt += 1
                line = f.readline()
                if not line: break
                note.append(line)
        del note[int(N)-1]
        print(note)
        with open("WordNote.txt","w",encoding="UTF-8") as f:
            for i in note:
                f.write(i)


    while True:
        wyw = input("단어 추가:1 테스트 보기:2 단어장 보기:3 단어 삭제:4 종료:5\n")
        if  wyw == '1':
            a = input("추가할 단어 :")
            b = input("단어의 뜻 :")
            addWord(a,b)
        elif wyw == '2':
            test()
        elif wyw == '3':
            showNote()
        elif wyw == '4':
            N = input("삭제할 단어의 위치(줄):")
            delWord(N)
        elif wyw == '5':
            break