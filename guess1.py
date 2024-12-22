import random

def ultimate_password():
    print("歡迎來到終極密碼遊戲！")
    print("我會選一個 1 到 100 之間的數字，你需要猜出它來。")
    print("每次猜測後，我會告訴你你猜的數字範圍。")

    # 隨機選擇一個數字
    number_to_guess = random.randint(1, 100)
    attempts = 0

    # 設定初始範圍
    low, high = 1, 100

    while True:
        try:
            # 玩家輸入猜測的數字
            guess = int(input(f"請輸入你猜的數字（目前範圍是 {low} 到 {high}）："))
            attempts += 1

            if guess < number_to_guess:
                low = guess + 1  # 更新範圍
                print(f"猜測錯誤！提示：數字範圍是 {low} 到 {high}，試著猜更大的數字。")
            elif guess > number_to_guess:
                high = guess - 1  # 更新範圍
                print(f"猜測錯誤！提示：數字範圍是 {low} 到 {high}，試著猜更小的數字。")
            else:
                print(f"恭喜！你猜對了！正確答案是 {number_to_guess}。")
                print(f"你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入一個有效的數字！")

# 開始遊戲
ultimate_password()
