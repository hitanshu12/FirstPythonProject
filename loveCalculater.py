
def calculate_love_score(name1, name2):
    n1 = []
    n2 = []

    # cmn_len = len(cmn)

    count = 0

    for i in name1:
        n1.append(i)

    for j in name2:
        if j in n1:
            n2.append(j)

    for c in "love":
        if c in n2:
            count = count + 1

    cmn = len(n2)

    print(f"Love Score: {cmn}{count}")


calculate_love_score(name1="Hitanshu", name2="Pooja")

# Alternate way

def love_calc(name3, name4):

    combined_names = name3 + name4
    lower_name = combined_names

    # how many times "true" word letter apper in combine name

    t = lower_name.count("t")
    r = lower_name.count("r")
    u = lower_name.count("u")
    e = lower_name.count("e")

    first_digit = t + r + u + e

    # how many times "love" word letter apper in combine name

    l = lower_name.count("l")
    o = lower_name.count("o")
    v = lower_name.count("v")
    e = lower_name.count("e")

    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(f"Love Calculator score is {score}")


love_calc("Kayne West", "Kim Kardashian")


