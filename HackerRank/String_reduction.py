#!/usr/bin/py
# Head ends here
def stringReduction(a):
    # strings are immutable hence converted to list
    mdfy_a = list(a)
    pos_str = ('a', 'b', 'c')
    count_letters = {alphabet:mdfy_a.count(alphabet) for alphabet in pos_str}
    # print(count_letters)
    distinct_count = len(set(mdfy_a))
    if distinct_count == 1:
        return len(mdfy_a)
    else:
        while distinct_count != 1:
            l = len(mdfy_a)
            flag = False
            freq_flag = False
            highest_count = max(count_letters.values())
            # get the frequent occurring letter and look in string to reduce it
            # freq_flag is to ensure that only the first frequent letter is taken to consideration when count is same
            # for multiple alphabets
            for letter, count in count_letters.items():
                if count == highest_count:
                    freq_letter = letter
                    freq_flag = True

                if freq_flag:
                    break

            # print(freq_letter)
            # iterating through the string to reduce
            for i in range(l):
                # reducing string from left to right
                if i+1 < l and mdfy_a[i] == freq_letter and mdfy_a[i] != mdfy_a[i+1]:
                    adj = (mdfy_a[i], mdfy_a[i+1])
                    for x in pos_str:
                        if x not in adj:
                            rplc_chr = x
                    # decrement the count of reducible letter
                    # print(rplc_chr, 'is the replacement character')

                    count_letters[mdfy_a[i]] -= 1
                    count_letters[mdfy_a[i+1]] -= 1
                    del mdfy_a[i:i+2]
                    mdfy_a.insert(i, rplc_chr)
                    # increment the count of inserted letter after reducing
                    count_letters[rplc_chr] += 1
                    flag = True

                    # print(mdfy_a, 'is the new list after string reduction')

                # reducing string from right to left.
                elif i-1 >= 0 and mdfy_a[i] == freq_letter and mdfy_a[i] != mdfy_a[i-1]:
                    adj = (mdfy_a[i], mdfy_a[i - 1])
                    for x in pos_str:
                        if x not in adj:
                            rplc_chr = x
                    # decrement the count of reducible letter
                    # print(rplc_chr, 'is the replacement character')

                    count_letters[mdfy_a[i]] -= 1
                    count_letters[mdfy_a[i - 1]] -= 1
                    del mdfy_a[i-1:i+1]
                    mdfy_a.insert(i, rplc_chr)
                    # increment the count of inserted letter after reducing
                    count_letters[rplc_chr] += 1
                    flag = True
                else:
                    pass

                if flag:
                    break

            distinct_count = len(set(mdfy_a))
            # print(distinct_count, 'is the new length after reduction')
        return len(mdfy_a)

# Tail starts here
if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        a = input()
        print(stringReduction(a))
