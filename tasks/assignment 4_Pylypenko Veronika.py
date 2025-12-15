import random

class Player:
    def __init__(self):
        self.moves = ['камінь', 'ножиці', 'папір']
    def make_move(self):
        while True:
            current_move = input("Введіть хід (камінь, ножиці, папір): ").strip().lower()
            if current_move in self.moves:
                return current_move
            print("Неправильний хід! Спробуйте ще раз.")

class Bot:
    def __init__(self):
        self.moves = ['камінь', 'ножиці', 'папір']
    def make_move(self):
        return random.choice(self.moves)

class FileLogger:
    def __init__(self, filename="results.txt"):
        self.filename = filename
    def write(self, result):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{result['player']};{result['ai']};{result['win']}\n")
    def leaderboard(self):
        data = {"player": 0, "ai": 0, "draw": 0}
        total_p = 0
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    total_p += 1
                    parts = line.strip().split(";")
                    if len(parts) != 3:
                        continue
                    winner = parts[2]
                    if winner == "player":
                        data["player"] += 1
                    elif winner == "ai":
                        data["ai"] += 1
                    else:
                        data["draw"] += 1
        except FileNotFoundError:
            return 0, data
        return total_p, data

class Game:
    def __init__(self):
        self.player = Player()
        self.bot = Bot()
        self.logger = FileLogger()
        self.moves = ['камінь', 'ножиці', 'папір']
    def determine_winner(self, p, ai):
        if p == ai:
            return "draw"
        rules = {'камінь': 'ножиці', 'ножиці': 'папір', 'папір': 'камінь'}
        if rules[p] == ai:
            return "player"
        return "ai"
    def play_round(self):
        player_move = self.player.make_move()
        ai_move = self.bot.make_move()
        winner = self.determine_winner(player_move, ai_move)
        result = {'player': player_move, 'ai': ai_move, 'win': winner}
        self.logger.write(result)
        print("Ваш хід:", player_move)
        print("Хід бота:", ai_move)
        if winner == "player":
            print("Ви перемогли!")
        elif winner == "ai":
            print("Бот переміг!")
        else:
            print("Нічия!")
    def result(self):
        total, data = self.logger.leaderboard()
        print("\nСтатистика:")
        print("Ігор:", total)
        print("Гравець –", data['player'])
        print("Бот –", data['ai'])
        print("Нічия ", data['draw'])
    def run(self):
        while True:
            self.play_round()
            while True:
                again = input("Зіграти ще раз? (y/n): ").strip().lower()
                if again == 'y':
                    break
                elif again == 'n':
                    self.result()
                    return
                else:
                    print("Помилка!!! Введіть 'y' або 'n'!")
if __name__ == "__main__":
    game = Game()
    game.run()
