class Weed:
    FAMILY_BLOOM = {
        "Айстрові":    60,
        "Злакові":     45,
        "Бобові":      30,
        "Хрестоцвіті": 20,
        "Губоцвіті":   50,
    }
    DEFAULT_BLOOM = 35

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def bloom_period(self):
        return self.FAMILY_BLOOM.get(self.family, self.DEFAULT_BLOOM)

    def __str__(self):
        return (
            f"Бур'ян: '{self.name}', сімейство: {self.family}, "
            f"цвітіння: {self.bloom_period():.1f} днів"
        )


class PerennialWeed(Weed):
    REDUCTION_PER_YEAR = 0.03

    def __init__(self, name, family, years):
        super().__init__(name, family)
        self.years = years

    def bloom_period(self):
        base = super().bloom_period()
        reduction = 1 - self.REDUCTION_PER_YEAR * self.years
        return base * max(reduction, 0)

    def __str__(self):
        return (
            f"Багаторічний бур'ян: '{self.name}', сімейство: {self.family}, "
            f"років життя: {self.years}, "
            f"цвітіння: {self.bloom_period():.1f} днів"
        )

if __name__ == "__main__":
    w1 = Weed("Амброзія", "Айстрові")
    w2 = Weed("Пирій", "Злакові")

    pw1 = PerennialWeed("Кульбаба", "Айстрові", 5)
    pw2 = PerennialWeed("Деревій", "Губоцвіті", 10)

    print(w1)
    print(w2)
    print()
    print(pw1)
    print(pw2)