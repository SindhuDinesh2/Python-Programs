def cumulative_sum(lst):
    cum_sum = []
    current_sum = 0
    for num in lst:
        current_sum += num
        cum_sum.append(current_sum)
    return cum_sum
print(cumulative_sum([1,2,3]))