#리스트의 평균을 구하기 위해서는 리스트 안에 있는 원소를 모두 더해 원소의 개수로 나누면 되므로
#전체 합을 나타내는 sum()을 리스트안의 원소의 개수를 나타내는 len()으로 나누어주면 된다.
nums = [1,2,3,4,5]
average = sum(nums)/len(nums)
print(average)
 