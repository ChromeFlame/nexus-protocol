class Character:
    def __init__(self, name, stats, hp, ac):
        self.name = name
        self.str = stats[0]     # Set Strength
        self.wis = stats[1]     # Set Wisdom
        self.dex = stats[2]     # Set Dexterity
        self.maxhp = hp         # Set MaxHP
        self.hp = self.maxhp    # Set HP to MaxHP
        self.ac = ac            # Set Armorclass

# STAT BREAKDOWN
# Strength - Melee Damage, Overworld Tasks, Minor HP Buff per point
# Wisdom - Quickhacks, 