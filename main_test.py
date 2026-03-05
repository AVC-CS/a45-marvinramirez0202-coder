import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    # Input: 10 20 30 -> ascending order: 10 20 30
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'10\s+20\s+30'], lines)


@pytest.mark.T2
def test_main_2():
    # Input: 15 5 25 -> ascending order: 5 15 25
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'5\s+15\s+25'], lines)


@pytest.mark.T3
def test_main_3():
    # Input: 30 10 20 -> ascending order: 10 20 30
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'10\s+20\s+30'], lines)


@pytest.mark.T4
def test_main_4():
    # Input: -3 7 -1 -> ascending order: -3 -1 7
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'-3\s+-1\s+7'], lines)
