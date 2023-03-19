#!/usr/bin/env python3
import random
import time

"""
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

Đọc file class.md trong thư mục này.
"""


class Fighter:
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health
        self.weapon = None
    
    def __str__(self) -> str:
        return f"{self.name} ({self.health})"


class Weapon:
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

    def __str__(self) -> str:
        return f"weapon: {self.name} ({self.damage})"

def solve(player1, player2):
    result = None
    """Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)"""
    while player1.health > 0 and player2.health>0:
        # player1 attack player2, condition health player1 > 0
        if player1.health>0:
            damage = random.randint(1,player1.weapon.damage)
            if player2.health > damage:
                player2.health -= damage
            else:
                player2.health = 0
                result = (player1.name, player1.health)
            print(f"{player1} -{damage}- {player2}")    
            time.sleep(2)
        
        # player1 attack player2,ondition health player2 > 0
        if player2.health >0:
            damage = random.randint(1,player2.weapon.damage)
            if player1.health > damage:
                player1.health -= damage
            else:
                player1.health = 0
                result = (player2.name, player2.health)
            print(f"{player1} -{damage}- {player2}")    
            time.sleep(2)
    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter('Nguyễn Phương Hằng', 300)
    player2 = Fighter('Thuỷ Tiên', 100)
    player1.weapon = Weapon("knife", 30)
    player2.weapon = Weapon("sword", 100)
    print(f"winner: {solve(player1, player2)}")


"""
NOTE
sau khi thành thạo việc tạo 1 class và viết method, có thể
vào link sau lấy chứng chỉ Python basic của HackerRank
Rất dễ, làm 5-10 phút là xong.

https://www.hackerrank.com/skills-verification/python_basic
"""


if __name__ == "__main__":
    main()
