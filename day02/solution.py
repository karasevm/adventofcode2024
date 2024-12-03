import sys

def check_nums(input: list[str]):
    nums = []
    for s in input:
        nums.append(int(s))
        
    increasing = True
    inc_count = 0
    dec_count = 0
    eq_count = 0
    for i in range(len(nums)-1):
        if int(nums[i+1]) > int(nums[i]):
            inc_count += 1
        elif int(nums[i+1]) < int(nums[i]):
            dec_count += 1
        else:
            eq_count += 1
            
    if eq_count > 2:
        return False
    if inc_count < dec_count:
        increasing = False
    for i in range(len(nums)-1):
        first = int(nums[i])
        second = int(nums[i+1])
        if abs(first - second) > 3 or abs(first - second) < 1 or (first > second and increasing) or (first < second and not increasing):
            return False
    return True

def part1(input_list: list[str]) -> int:
    safe_count = 0
    for line in input_list:
        nums = line.split(" ")
        if check_nums(nums):
            safe_count += 1
                
    return safe_count

def part2(input_list: list[str]) -> int:
    unsafe_count = 0
    for line in input_list:
        nums = line.split(" ")
        if not check_nums(nums):
            results = []
            for j in range(len(nums)):
                new_nums = nums.copy()
                new_nums.pop(j)
                results.append(check_nums(new_nums))
            print(line, results)
            if True not in results:
                unsafe_count += 1

                
    return len(input_list) - unsafe_count

if __name__ == "__main__":
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Error opening the file, try again")
        sys.exit(1)
    with f:
        lines = f.readlines()
        f.close()
        lines = [line.rstrip() for line in lines]
        print(
        f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
