from aoc1.elf import Elf


class TestAoC1:
    def test_sum_up_calories(self):
        elf = Elf([1, 2, 3])
        assert elf.total_calories_carried == 6
