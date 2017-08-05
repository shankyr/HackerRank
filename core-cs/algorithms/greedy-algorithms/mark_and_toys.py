# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
    # Compute and return final answer over here
    answer = 0
    prices.sort()
    for ind in xrange(len(prices)):
        rupees -= prices[ind]

        if rupees >= 0:
            answer += 1
        elif rupees < 0:
            break

    return answer


if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)
