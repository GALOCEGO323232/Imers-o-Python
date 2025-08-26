def average(notas : dict[str, int]) -> float:
        value = notas.values()
        if not value:
                return 0
        total = sum(value)
        res = total / len(value)
        return res