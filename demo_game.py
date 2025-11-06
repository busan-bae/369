#!/usr/bin/env python3
"""
숫자 맞추기 게임 자동 데모
Auto Demo of Number Guessing Game
"""
import random
import time

def auto_demo():
    print("=" * 50)
    print("🎮 숫자 맞추기 게임 자동 데모 🎮")
    print("Automatic Demo of Number Guessing Game")
    print("=" * 50)

    # 1부터 100 사이의 랜덤 숫자 생성
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print(f"\n💡 1부터 100 사이의 숫자를 맞춰보세요!")
    print(f"🎯 최대 {max_attempts}번의 기회가 있습니다.")
    print(f"\n🔍 (비밀 번호: {secret_number})\n")

    time.sleep(1)

    # 자동으로 게임 플레이
    low = 1
    high = 100

    while attempts < max_attempts:
        # 중간값으로 추측 (이진 탐색 방식)
        guess = (low + high) // 2
        attempts += 1

        print(f"🤖 시도 {attempts}/{max_attempts} - AI가 추측: {guess}")
        time.sleep(0.5)

        if guess < secret_number:
            print(f"   📈 더 큰 숫자입니다! (범위: {guess+1}~{high})\n")
            low = guess + 1
        elif guess > secret_number:
            print(f"   📉 더 작은 숫자입니다! (범위: {low}~{guess-1})\n")
            high = guess - 1
        else:
            print(f"\n🎉 축하합니다! 정답입니다! 🎉")
            print(f"✨ AI가 {attempts}번 만에 맞췄습니다!")
            print(f"💡 정답: {secret_number}")
            return True

        time.sleep(0.5)

    print(f"\n😢 아쉽게도 기회를 모두 사용했습니다.")
    print(f"💡 정답은 {secret_number}이었습니다.")
    return False

if __name__ == "__main__":
    print("\n이 프로그램은 AI가 자동으로 숫자를 맞추는 과정을 보여줍니다.\n")
    time.sleep(1)
    auto_demo()
    print("\n" + "=" * 50)
    print("✅ 데모가 완료되었습니다!")
    print("💻 실제 게임을 플레이하려면: python3 number_game.py")
    print("=" * 50 + "\n")
