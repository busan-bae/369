#!/usr/bin/env python3
"""
간단한 숫자 맞추기 게임
Simple Number Guessing Game
"""
import random

def play_game():
    print("=" * 50)
    print("🎮 숫자 맞추기 게임에 오신 것을 환영합니다! 🎮")
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)

    # 1부터 100 사이의 랜덤 숫자 생성
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print(f"\n💡 1부터 100 사이의 숫자를 맞춰보세요!")
    print(f"🎯 최대 {max_attempts}번의 기회가 있습니다.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"시도 {attempts + 1}/{max_attempts} - 숫자를 입력하세요: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️  1부터 100 사이의 숫자를 입력해주세요!\n")
                continue

            if guess < secret_number:
                print("📈 더 큰 숫자입니다!\n")
            elif guess > secret_number:
                print("📉 더 작은 숫자입니다!\n")
            else:
                print(f"\n🎉 축하합니다! 정답입니다! 🎉")
                print(f"✨ {attempts}번 만에 맞추셨습니다!")
                return True

        except ValueError:
            print("⚠️  올바른 숫자를 입력해주세요!\n")

    print(f"\n😢 아쉽게도 기회를 모두 사용하셨습니다.")
    print(f"💡 정답은 {secret_number}이었습니다.")
    return False

def main():
    while True:
        play_game()

        play_again = input("\n다시 플레이하시겠습니까? (y/n): ").lower()
        if play_again != 'y' and play_again != 'yes':
            print("\n👋 게임을 종료합니다. 즐거우셨나요? 안녕히 가세요!")
            break
        print("\n")

if __name__ == "__main__":
    main()
