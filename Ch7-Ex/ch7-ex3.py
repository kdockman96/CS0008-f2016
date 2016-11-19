def main():
    months = [0] * 12
    name_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', \
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def total(months):
        total = 0
        for num in months:
            total += num
        return total
    for index in range(12):
        print('Enter the amount of rain in',
              months[index] = int(input(name_months[index] + ': '))
    print('The total is', total(months), 'mm.')
    average = total(months)/12.0
    print('The average rainfall is', average, 'months')
    m_copy = months[0:]
    months.sort()
    lowest = months[0]
    print('Lowest is', lowest)
    lows = []
    for i in range(12):
        if m_copy[i] == lowest:
            lows.append(name_months[i])
    for i in range (len(lows)):
        print(lows[i])
        if i < len(lows)-1:
            print('and')
    highest = months[11]
    print('Highest is', highest)
    highs = []
    for i in range(12):
        if m_copy[i] == highest:
            highs.append(name_months[i])
    for i in range(len(highs)):
        print(highs[i])
        if i < len(highs)-1:
            print('and')

main()