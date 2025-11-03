#十二支アキネーター
#準備
while True:
    print("ーーー 十二支の動物アキネーターへようこそ！ ーーー")
    print("選択肢：ねずみ・うし・とら・うさぎ・りゅう・へび・うま・ひつじ・さる・にわとり・いぬ・いのしし")
    print("選択肢の中から一つ決めてその動物について答えてね！")
    print("注意：質問に「はい」か「いいえ」で答えてね")

    ready = input("準備はいいですか？（はい / いいえ）: ")
    if ready == "はい":
        print("よし！ではゲームスタート！！")
    elif ready == "いいえ":
        print("またの挑戦待ってます！")
        break
    else:
        print("「はい」か「いいえ」で答えてね")
        break

#本番
#１階層
    ans1 = input("1. 実在しますか？（はい／いいえ）：")
    if ans1 == "いいえ":
        print("あなたが考えているのは……りゅう！")
        break
    elif ans1 != "はい":
        print("「はい」か「いいえ」で答えろって！最初からやり直しだ！\n")
        continue
#２階層
    ans2 = input("2. 哺乳類ですか？（はい／いいえ）：")
#３階層
    if ans2 == "いいえ":
        ans2_1 = input("3. 羽がありますか？（はい／いいえ）：")
        if ans2_1 == "はい":
            print("あなたが考えているのは……にわとり！")
            break
        elif ans2_1 == "いいえ":
            print("あなたが考えているのは……へび！")
            break
        else:
            print("日本語読めないのか？。最初からやり直し！\n")
            continue
    elif ans2 != "はい":
        print("注意をみろ！最初からやり直しだ！\n")
        continue
#３階層
    ans3 = input("3. 家畜として放牧されますか？（はい／いいえ）：")
#４階層
    if ans3 == "はい":
        ans3_1 = input("4. 闘牛に関係ありますか？（はい／いいえ）：")
        if ans3_1 == "はい":
            print("あなたが考えているのは……うし！")
            break
#５階層
        elif ans3_1 == "いいえ":
            ans3_2 = input("5. 競馬場で活躍してそうですか？（はい／いいえ）：")
            if ans3_2 == "はい":
                print("あなたが考えているのは……うま！")
                break
            elif ans3_2 == "いいえ":
                print("あなたが考えているのは……ひつじ！")
                break
            else:
                print("ちゃんと言えよ？最初からやり直しだ！\n")
                continue
        else:
            print("ちゃんと答えてよーー最初からやり直し！\n")
            continue
#４階層
    elif ans3 == "いいえ":
        ans4 = input("4. 桃太郎に登場しますか？（はい／いいえ）：")
#５階層
        if ans4 == "はい":
            ans4_1 = input("5. 人間と一緒にお散歩に行きますか？（はい／いいえ）：")
            if ans4_1 == "はい":
                print("あなたが考えているのは……いぬ！")
                break
            elif ans4_1 == "いいえ":
                print("あなたが考えているのは……さる！")
                break
            else:
                print("ちゃんとやれよ？？最初からやり直し！\n")
                continue
#５階層
        elif ans4 == "いいえ":
            ans5 = input("5. 人間の手のひらに乗りますか？（はい／いいえ）：")
#６階層
            if ans5 == "はい":
                ans5_1 = input("6. 実験で使われるイメージがありますか？（はい／いいえ）：")
                if ans5_1 == "はい":
                    print("あなたが考えているのは……ねずみ！")
                    break
                elif ans5_1 == "いいえ":
                    print("あなたが考えているのは……うさぎ！")
                    break
                else:
                    print("ほんとに注意読んだか？最初からやり直し！\n")
                    continue
#６階層
            elif ans5 == "いいえ":
                ans6 = input("6. 猫科ですか？（はい／いいえ）：")
                if ans6 == "はい":
                    print("あなたが考えているのは……とら！")
                    break
                elif ans6 == "いいえ":
                    print("あなたが考えているのは……いのしし！")
                    break
                else:
                    print("「はい」か「いいえ」だってば！最初からやり直し！\n")
                    continue
            else:
                print("日本語読める？やり直しだ！\n")
                continue
        else:
            print("…最初から！\n")
            continue
    else:
        print("キレるぞ？？最初からやり直し！\n")
        continue

print("\nーーー 終了！遊んでくれてありがとう！ ーーー")