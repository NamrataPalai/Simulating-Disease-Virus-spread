""" Python Assignment 2 : Task 3
    Course Code         : FIT9136
    Created on          : May 26, 2020
    Author Name         : Namrata Palai
    Last Modified       : June 07, 2020

TasK 3: This task provides the visualisation of count of infected people for a given period of time based on the
simulation performed in task 2

Scenario A: Number of days: 30, Meeting probability: 0.6, Patient zero health: 25 health points

The patient zero health point is very low, i.e. 25 which shows the first patient is quite unwell. Also, the meeting
probability is 60%. In this scenario, the social gatherings is higher, also the viral load infected by patient zero to
its friends can be high.
The plot for Scenario A shows a steady increase in the number of infected people in the given
time frame, as a result does match the predictions.


Scenario B: Number of days: 60, Meeting probability: 0.25, Patient zero health: 49 health points

The possibility of meeting is 25% which is very low , stating minimal social gatherings. Also, Patient zero's health
point 49 which shows which is maximally contagious. In this scenario, since the meeting probability is low,
there is uncertainty in the possibility of people meeting wherein giving people time to regain health points by sleeping
everyday. Also in this scenario due to simulation is done based on random probability, the output varies every time.

The plot for Scenario B shows rise & fall of count of infected people through out the time frame depicting uncertainty
prevailing with respect to virus spread as the output is unpredictable as per random probability, which matches the
predictions made.


Scenario C: Number of days: 90, Meeting probability: 0.18, Patient zero health: 40 health points

Although the time frame is large, but the meeting probability is very less, i.e. 18% which is nearly closed to the
possibility of almost 0 chances of meeting. So which chance of meeting being almost 0, the spread of virus will be
extensively less. Also, the health point of patient 0 is low which does spread the infection initially but with almost
no chances of any social gathering taking place patient can regain health points by sleeping daily.

The plot for Scenario C shows, the maximum count recorded for infected people is 1 which happens initially due to low
health points of patient zero which dies out quickly and comes down to 0, remaining constant for the rest of the time
period which apparently matches the predictions made.

"""

import matplotlib.pyplot as plt

from a2_31002188_task2 import *


# function to visualise the rate of spread of virus based on the run_simulation() in task2 output using matplotlib
def visual_curve(days, meeting_probability, patient_zero_health):
    # list of days for the time period specified
    days_list = list(range(days))
    print(days_list)

    # function call: run_simulation(arg1,arg2,arg3) for list of count of infected people each day for specified days
    infected_count = run_simulation(days, meeting_probability, patient_zero_health)

    # matplotlib library called to plot the graph
    plt.plot(days_list, infected_count)

    # Names of x & y labels specified
    plt.ylabel("Count of Infected people")
    plt.xlabel("Days")

    # to save the plot generated in .png format
    plt.savefig('Scenario_D')

    # to show the plot
    plt.show()


""" FOR COLORED TEXT IN TERMINAL: 
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python"""

# color code defined for the warning message to be printed on terminal
color_code = {"WARNING": "\033[93m", "ENDC": "\033[0m"}


# function to print warning message in terminal if value of days entered by user is incorrect
def get_days_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(
                f"{color_code['WARNING']}Warning: Day should be non negative integer. Enter again{color_code['ENDC']}"
            )
            continue

        if value < 0:
            print(
                f"{color_code['WARNING']}Warning: Day should be non negative integer. Enter again{color_code['ENDC']}"
            )
            continue
        else:
            break
    return value


# function to print warning message in terminal if value of meeting probability entered by user is incorrect
def get_meeting_probability_input(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print(
                f"{color_code['WARNING']} Warning: Meeting probability should be between 0 and 1.Enter again{color_code['ENDC']}"
            )
            continue

        if value < 0 or value > 1:
            print(
                f"{color_code['WARNING']} Warning: Meeting probability should be between 0 and 1.Enter again{color_code['ENDC']}"
            )
            continue
        else:
            break
    return value


# function to print warning message in terminal if value of patients initial health entered by user is incorrect
def get_patient_zero_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(
                f"{color_code['WARNING']}Warning: Patient zero health be between 0 and 100. Enter again{color_code['ENDC']}"
            )
            continue

        if value < 0 or value > 100:
            print(
                f"{color_code['WARNING']}Warning: Patient zero health be between 0 and 100. Enter again{color_code['ENDC']}"
            )
            continue
        else:
            break
    return value


# main function
if __name__ == "__main__":
    days = get_days_input("Enter number of days the simulation should run for:")
    meeting_probability = get_meeting_probability_input("Enter fractional probability of person visiting a friend:")
    patient_zero_health = get_patient_zero_input("Enter initial health of the first person in the file :")
    visual_curve(days, meeting_probability, patient_zero_health)
