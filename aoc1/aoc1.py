from elf import Elf
import utils.file_helper as filehelper


def get_elves_list_from_input_file(filename):
    puzzle_input_path = filehelper.get_resource_path(filename)
    file_lines = filehelper.read_file_lines(puzzle_input_path)

    elves = [Elf([])]
    i = 0

    for line in file_lines:
        if line != '\n':
            elves[i].add_food_item(int(line.strip()))
        else:
            i += 1
            elves.append(Elf([]))

    return elves


def run_aoc1():
    puzzle1_filename = "puzzle_1a_input.txt"
    elfs = get_elves_list_from_input_file(puzzle1_filename)
    sorted_elves = sorted(elfs, key=lambda x: x.total_calories_carried, reverse=True)
    print(sorted_elves[0])
    print("\n")

    # solving puzzle2
    total_calos_by_top_three = (sorted_elves[0].total_calories_carried +
                                sorted_elves[1].total_calories_carried +
                                sorted_elves[2].total_calories_carried)

    print(f"Total calories carried by the top three Elves is {total_calos_by_top_three}\n")


if __name__ == '__main__':
    run_aoc1()
