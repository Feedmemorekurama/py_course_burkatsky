attack_wolf = ["sheep","sheep","sheep","wolf","sheep"] #первый цикл 
go_away_wolf = ["sheep","sheep","wolf"] #второй цикл

attack_wolf.reverse()
for i in attack_wolf: # проверка первого цикла
    if attack_wolf.index("sheep") == 0 and attack_wolf.index("wolf") == 1:
        print("Oi! Sheep number 1! You are about to be eaten by a wolf!")
        break
    else:
        print("Wolf will eat another sheep")

go_away_wolf.reverse()
for k in go_away_wolf: #проверка второго цикла
    if go_away_wolf.index("wolf") < go_away_wolf.index("sheep"):
        print("Pls go away and stop eating my sheep")
        break
    else:
        print("Wolf ate sheep")
        break