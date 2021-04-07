""" Python Assignment 2 : Task 2
    Course Code         : FIT9136
    Created on          : May 25, 2020
    Author Name         : Namrata Palai
    Last Modified       : June 07, 2020

TasK 2: This task simulates the disease spread or health of people in a group over a period of time based on a meeting
probability which signifies if a person/patient is meeting another person/patient. Health points of any patient in set
between 0 & 100. When a contagious person meets a person/contagious person or vice versa, the viral load is calculated
& is infected to the respective person/contagious person resulting in decrease of health points. Also, 5 health points
are added to all persons/patients on daily basis as they sleep. At the end of the each day , the count of infected
people is calculated & stored in list data type for a given period of time.
"""

import random
from a2_31002188_task1 import *


# Patient class inherits the methods of the Person class
class Patient(Person):

    # method to create a new Patient object by inheriting from the Person class
    # first_name and last_name are strings containing the person’s name
    # health is the initial starting value of the person’s health points
    def __init__(self, first_name, last_name, initial_health):
        Person.__init__(self, first_name, last_name)
        self.health = initial_health

    # method returns the patient’s current health points
    def get_health(self):
        return self.health

    # method changes the patient’s current health points directly
    def set_health(self, new_health):
        self.health = new_health

    # method returns a Boolean result of TRUE/FALSE on the basis of person's health point in range of being contagious
    def is_contagious(self):
        if self.health < 50:
            return True
        else:
            return False

    # method infects the Patient object with a viral load
    def infect(self, viral_load):
        if 0 <= self.health <= 100:
            if self.health <= 29:
                new_health = self.health - (0.1 * viral_load)
                if new_health < 0:
                    new_health = 0
                self.set_health(new_health)

            elif 29 < self.health < 50:
                new_health = self.health - (1 * viral_load)
                if new_health < 0:
                    new_health = 0
                self.set_health(new_health)
            else:
                new_health = self.health - (2 * viral_load)
                if new_health < 0:
                    new_health = 0
                self.set_health(new_health)

    # method to recover some health points for person by one night's sleep
    def sleep(self):
        self.health = self.health + 5
        if self.health > 100:
            self.health = 100

# function to read the sample data file
def read_sample_data_file():

    # read the sample data file, if no exception occurs
    try:
        file_name = "a2_sample_set.txt"
        fh = open(file_name, "r")

        # all_person_data has list of each line of file as an item in list object
        all_person_data = fh.readlines()
        fh.close()
        if all_person_data:
            return all_person_data
        else:
            raise Exception("There is no data in the " + file_name)

    # print the error message, if exception occurs during reading sample data file
    except Exception as e:
        raise Exception(str(e))


# function to split the single list into multiple lists demarcating each list for Person and its connections
def parse_this_person(current_data_line):

    # execute splitting of lists, if no exception occurs
    try:
        # current_person_data has each line of the file as list holding names of person and its connections
        current_person_data = current_data_line.replace(":", ",").strip().split(", ")

        # print(current_person_data) #for validation

        # person_name has first person's name from every list
        person_name = current_person_data.pop(0)

        # print(person_name) #for validation

        # person_first_last_name has lists of split values of first names in person_name list
        person_first_last_name = person_name.split()

        # print(person_first_last_name) #for validation

        return {
            "first_name": person_first_last_name[0],
            "last_name": person_first_last_name[1],
            "my_connection": current_person_data,
        }

    # respond if any exception occurs in preceding try clause
    except Exception as e:
        print("Exception occurred in parsing the person " + str(e))
        return False


# function to check for existence of friends in person list to ensure single object value creation for any given person
def link_connection_obj(patient_name_list, patient_friends_list, patient_object_list):

    # execute string value comparison of friends & persons to map with respective object value list
    try:
        # iterating through friends list for each patient
        for j in range(len(patient_friends_list)):

            # for each patient's friend, iterating through one friend after the other
            for k in range(len(patient_friends_list[j])):

                # comparing the string values of friend list with patient's list to check the respective index numbers
                for r in range(len(patient_name_list)):

                    # if the index of both matches
                    if patient_name_list[r] == patient_friends_list[j][k]:

                        # add that friend's patient object
                        patient_object_list[j].add_friend(patient_object_list[r])

        # return the list of object values of all patient
        return patient_object_list

    # respond if any exception occurs in preceding try clause
    except Exception as e:
        raise Exception(str(e))


# function to create person objects for all persons in sample file using the object constructor Patient
def load_patients(default_health):

    # execute creation of object values for all patients appending the same in  a list
    try:
        # empty list created to store object values of all patients
        patient_object_list = []

        # empty list created to store string values of patients
        patient_name_list = []

        # empty list created to store list of friends of all patients in sample file
        patient_friends_list = []

        # function call: read_sample_data_file()
        all_patient_data = read_sample_data_file()

        # iterating through the sample data
        for current_patient_data in all_patient_data:

            # function call: parse_this_person(argument)
            parsed_data = parse_this_person(current_patient_data)

            # obj_patient stores object values of patients created calling object constructor Patient
            obj_patient = Patient(parsed_data["first_name"], parsed_data["last_name"], default_health)

            # add string values corresponding to object values in a list using method get_name() in Person Class
            patient_name_list.append(obj_patient.get_name())

            # add list of friends to a list, for all patients
            patient_friends_list.append(parsed_data["my_connection"])

            # add the object values of the patient to the list
            patient_object_list.append(obj_patient)

        # function call:link_connection_obj(arg1,arg2,arg3) for object value creation check & return list of objects
        return link_connection_obj(patient_name_list, patient_friends_list, patient_object_list)

    # respond if any exception occurs in preceding try clause
    except Exception as e:
        print("Exception occurred while loading patient " + str(e))
        return False


# function to simulate disease spread in patients & their friends & calculate count of infected patients everyday
# meeting probability is the possibility between patient & friends
# patient_zero_health is the health of first patient in list, rest have 75 as default health

def run_simulation(days, meeting_probability, patient_zero_health):

    # execute the simulation logic, if no exception occurs
    try:

        # default health of all patients is set to 75
        default_health = 75

        # function call: load_patient(argument) to load patients with their initial health value
        patients = load_patients(default_health)

        # first patient's default_health is inputted by user
        patients[0].set_health(patient_zero_health)

        # empty list created to store the count of infected people each day
        infected_people = []

        # iterate through each day to calculate the count of infected people
        for d in range(days):

            # count of infected people initialised
            infected_count = 0

            # iterate through the list of patients
            for i in patients:

                # list the object values of the friends for every patient using get_friends() method
                patient_friends = i.get_friends()

                # iterating through the list of friends of patients
                for j in patient_friends:

                    # random probability is set importing random library
                    random_prob = random.random()

                    # Check if the meeting probability of patients & their friends is more
                    if random_prob <= meeting_probability:

                        # Check if patient is contagious, infect viral load to patient's friends
                        if i.is_contagious():  # method call: is_contagious()
                            # formula to calculate viral load by getting initial health using get_health() method
                            viral_load_patient = 5 + (((i.get_health() - 25) ** 2) / 62)
                            # Patient infects the viral load to friends using infect() method
                            j.infect(viral_load_patient)

                        # Check if patient's friend is contagious, infect viral load to patient
                        if j.is_contagious():  # method call: is_contagious()
                            # formula to calculate viral load by getting initial health using get_health() method
                            viral_load_friend = 5 + (((j.get_health() - 25) ** 2) / 62)
                            # Friend infects the viral load to patient using infect() method
                            i.infect(viral_load_friend)

            # iterating through patients list to check the count of infected people
            for k in patients:
                # check if patient is contagious
                if k.is_contagious():
                    # increase the count of infected people
                    infected_count = infected_count + 1

                # to add 5 health points to patient health as the patient sleeps everyday, method call: sleep()
                k.sleep()

            # append the count of infected people in the list day wise for the number of days specified by user
            infected_people.append(infected_count)

        # return the list of count of infected people each day
        return infected_people

    # respond if any exception occurs in preceding try clause
    except Exception as e:
        print("Exception occurred while simulation" + str(e))
        return False


# main function
if __name__ == '__main__':
    # test_result = run_simulation(15, 0.8, 49)
    # print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]

    test_result = run_simulation(40, 1, 1)
    print(test_result)
    # sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
