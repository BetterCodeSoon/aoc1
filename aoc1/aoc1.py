from elf import Elf
import utils.file_helper as filehelper


def create_elf_from_list(food_item_list):
    return Elf(food_item_list)


def get_elfs_list_from_input_file(filename):
    puzzle_input_path = filehelper.get_resource_path(filename)
    file_lines = filehelper.read_file_lines(puzzle_input_path)

    elfs = [Elf([])]
    i = 0

    for line in file_lines:
        if line != '\n':
            elfs[i].add_food_item(int(line.strip()))
        else:
            i += 1
            elfs.append(Elf([]))

    return elfs


def run_aoc1():
    puzzle1_filename = "puzzle_1a_input.txt"
    elfs = get_elfs_list_from_input_file(puzzle1_filename)
    sorted_elfs = sorted(elfs, key=lambda x: x.total_calories_carried, reverse=True)
    print(sorted_elfs[0])


if __name__ == '__main__':
    run_aoc1()
