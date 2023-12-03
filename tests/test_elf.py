from aoc1.elf import Elf


class TestElf:
    def test_sum_up_calories(self):
        elf = Elf([1, 2, 3])
        assert elf.total_calories_carried == 6
