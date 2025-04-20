class Weapon:
    def __init__(self, name: str, dmg: float, rng: float):
        self.name = name
        self.dmg = dmg
        self.rng = rng

    def hit(self, actor, target):
        if not target.is_alive() :
            print(f"{target} is dead")
            return None
        if self.rng < abs(actor.vector() - target.vector()):
            print(f"{target} out of range")
            return None
        target.get_damage(self.dmg)
        print(f"attacked {target} with {self.name}. Damage: {self.dmg}")

class BaseCharacter:
    def __init__(self, x: float, y: float, hp: int):
        self.x = x
        self.y = y
        self.hp = hp

    def move(self, x, y):
        self.x += x
        self.y += y

    def is_alive(self):
        return self.hp >= 0

    def get_damage(self, amnt):
        self.hp -= amnt

    def get_coords(self) -> tuple[float, float]:
        return self.x, self.y

    def vector(self):
        return (self.x**2 + self.y**2)**1/2


class MainHero(BaseCharacter):
    def __init__(self, x: float, y: float, hp: int, name: str):
        super().__init__(x, y, hp)
        self.wpns = []
        self.wpn_curr = 0
        self.name = name

    def hit(self, target):
        if not self.wpns:
            print("Weaponless")
            return None
        if target.__class__.__name__ != "BaseEnemy":
            print("Cant Hit not Base Enemy")
            return None
        self.wpns[self.wpn_curr].hit(self, target)

    def add_weapon(self, wpn: Weapon):
        self.wpns.append(wpn)
        if len(self.wpns) == 1:
            self.wpn_curr = 0

    def next_weapon(self):
        match len(self.wpns):
            case 1:
                print("Only one Weapon in inventory")
                self.wpn_curr = 0
                return None
            case self.wpn_curr:
                self.wpn_curr = 0
                return None
        self.wpn_curr += 1

    def heal(self, amnt):
        self.hp += amnt if self.hp < 200 else 200
        print("Healed up to", self.hp)


class BaseEnemy(BaseCharacter):
    def __init__(self, x: float, y: float, hp: int, wpn: Weapon):
        super().__init__(x, y, hp)
        self.wpn = wpn

    def hit(self, target):
        if target.__class__.__name__ != "MainHero" :
            print("Cant Hit not Main Hero")
            return None
        self.wpn.hit(self, target)

    def __str__(self):
        return f"Enemy on coordinates {self.get_coords()} with {self.wpn.name}"

def main():
    weapon1 = Weapon("Cerberus", 5, 1)
    weapon2 = Weapon("Rebelion", 7, 2)
    weapon3 = Weapon("Coyote-A", 3, 10)
    weapon4 = Weapon("Faust", 1000, 1000)
    princess = BaseCharacter(100, 100, 100)
    archer = BaseEnemy(10, 10, 500, weapon3)
    armored_swordsman = BaseEnemy(10, 10, 500, weapon2)
    archer.hit(armored_swordsman)
    armored_swordsman.move(10, 10)
    print(armored_swordsman.get_coords())
    main_hero = MainHero(0,0, 200, "Dante")
    main_hero.hit(armored_swordsman)
    main_hero.next_weapon()
    main_hero.add_weapon(weapon1)
    main_hero.hit(armored_swordsman)
    main_hero.add_weapon(weapon4)
    main_hero.hit(armored_swordsman)
    main_hero.next_weapon()
    main_hero.hit(princess)
    main_hero.hit(armored_swordsman)
    main_hero.hit(armored_swordsman)


if __name__ == "__main__":
    main()
