import chess
import random

class Character:
    def __init__(self, name, level=1, experience=0):
        self.name = name
        self.level = level
        self.experience = experience

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        print(f"{self.name} leveled up to level {self.level}!")

class Quest:
    def __init__(self, description, reward):
        self.description = description
        self.reward = reward

    def complete(self, character):
        print(f"Quest completed: {self.description}")
        character.gain_experience(self.reward)

class ChessRPG:
    def __init__(self):
        self.board = chess.Board()
        self.characters = []
        self.quests = []

    def create_character(self, name):
        character = Character(name)
        self.characters.append(character)
        print(f"Character created: {name}")

    def add_quest(self, description, reward):
        quest = Quest(description, reward)
        self.quests.append(quest)
        print(f"Quest added: {description}")

    def start_quest(self, character_name, quest_description):
        character = next((c for c in self.characters if c.name == character_name), None)
        quest = next((q for q in self.quests if q.description == quest_description), None)
        if character and quest:
            self.play_chess(character, quest)
        else:
            print("Character or quest not found.")

    def play_chess(self, character, quest):
        while not self.board.is_game_over():
            print(self.board)
            move = input("Enter your move: ")
            try:
                self.board.push_san(move)
            except ValueError:
                print("Invalid move. Try again.")
                continue

            if self.board.is_game_over():
                print("Game over!")
                quest.complete(character)
                self.board.reset()
                break

            # Random move for the opponent
            legal_moves = list(self.board.legal_moves)
            self.board.push(random.choice(legal_moves))

    def command_line_interface(self):
        while True:
            command = input("Enter a command: ")
            if command == "create character":
                name = input("Enter character name: ")
                self.create_character(name)
            elif command == "add quest":
                description = input("Enter quest description: ")
                reward = int(input("Enter quest reward: "))
                self.add_quest(description, reward)
            elif command == "start quest":
                character_name = input("Enter character name: ")
                quest_description = input("Enter quest description: ")
                self.start_quest(character_name, quest_description)
            elif command == "exit":
                break
            else:
                print("Unknown command. Try again.")

if __name__ == "__main__":
    game = ChessRPG()
    game.command_line_interface()
