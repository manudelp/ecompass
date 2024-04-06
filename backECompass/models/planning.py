class Planning:
    def __init__(self, id, name, saves, savesAcu, dateEnd, cost):
        self.id = id
        self.name = name
        self.saves = saves
        self.savesAcu = savesAcu
        self.dateEnd = dateEnd
        self.cost = cost

# Ejemplo de uso
planning = Planning(1,"Plan A", 10, 100, "2022-12-31", 500)