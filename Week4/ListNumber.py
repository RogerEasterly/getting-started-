num_list = []
for i in range(0, 20):
    num = int(input("Enter a number: "))
    num_list.append(num)


print("The lowest number was: " + str(min(num_list)))
print("The highest number was: " + str(max(num_list)))
print("The sum of all numbers is: " + str(sum(num_list)))
