def weekly_average(total_steps, days):
    average = total_steps / days
    return average

def goal_met(steps, goal):
    if steps >= goal:
        return True
    return False

average_steps = weekly_average(56000, 7)
print("Average steps:", average_steps)

if goal_met(9000, 8000):
    print("Daily goal achieved!")
else:
    print("Keep exercising!")
