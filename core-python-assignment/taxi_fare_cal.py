def cal_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    total_fare = base_fare + distance_fare
    return total_fare

trips = [5, 10, 3]  
total_fare = 0
for i in range(len(trips)):
    fare = cal_fare(trips[i])
    print(f"Trip {i+1}: ${fare}")
    total_fare += fare

print("Total Fare: $", total_fare)
