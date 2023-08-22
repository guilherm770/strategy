from src import Character, Bow, Sword, Heal, Ax

knight = Character(Sword(6))
archer = Character(Bow(9))
healer = Character(Heal(7))
orc = Character(Ax(8))

knight.action()
archer.action()
archer.attr()
healer.attr()
orc.action()

# i could build a strategy pattern for a department store that has products and wants to abstract its types
# of discounts