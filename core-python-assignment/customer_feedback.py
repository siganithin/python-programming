def cal_pos_feedback(ratings):
    if len(ratings) == 0: 
        print("No ratings available.")
        return
    
    pos_count = 0
    for i in ratings:
        if i >= 4:  # Count only 4 or 5
            pos_count += 1

    percentage = (pos_count / len(ratings)) * 100
    print("Positive Feedback:", round(percentage, 2), "%")


ratings = [5, 4, 3, 5, 2, 4, 1, 5]
cal_pos_feedback(ratings)
