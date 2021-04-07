""" Python Assignment 2 : Task 1
    Course Code         : FIT9136
    Created on          : May 22, 2020
    Author Name         : Namrata Palai
    Last Modified       : June 07, 2020

Task 1 Description: In this task, we are using List Data type to store set of objects for persons in the sample data.
The methods defined in the object constructor allows us to retrieve both object & string values of the connections
 of the persons stored in the object list.
"""

# Person Class represents a person who is linked to other people by social connections & below defined are the methods
class Person:

    # method to create a new Person object, where first_name and last_name are strings containing the person’s name
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []

    # method should add a new social connection to be stored in another Person object(friend_person)
    def add_friend(self, friend_person):
        self.friends.append(friend_person)

    # method returns a string containing the person’s first and last name concatenated together
    def get_name(self):
        return self.first_name + " " + self.last_name

    # method returns a list of Person objects for the social connections that have been added
    def get_friends(self):
        return self.friends


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
def link_connection_obj(main_person_list, list_all_friends, list_all_people):

    # execute string value comparison of friends & persons to map with respective object value list
    try:
        # iterating through friends list for each person
        for j in range(len(list_all_friends)):

            # for each person's friend, iterating through one friend after the other
            for k in range(len(list_all_friends[j])):

                # comparing the string values of friend list with persons list to check  the respective index numbers
                for r in range(len(main_person_list)):

                    # if the index of both matches
                    if main_person_list[r] == list_all_friends[j][k]:

                        # add that friend's person object
                        list_all_people[j].add_friend(list_all_people[r])

        # return the list of object values of all people
        return list_all_people

    # respond if any exception occurs in preceding try clause
    except Exception as e:
        raise Exception(str(e))


# function to create person objects for all persons in sample file using the object constructor Person
def load_people():
    # execute creation of object values for all persons & append the same in list
    try:
        # empty list to store object values of all persons
        list_all_people = []

        # empty list to store string values of person
        main_person_list = []

        # empty list to store list of friends of all persons in sample file
        list_all_friends = []

        # function call: read_sample_data_file()
        all_person_data = read_sample_data_file()

        # iterating through the sample data
        for current_person_data in all_person_data:

            # function call: parse_this_person('argument')
            parsed_data = parse_this_person(current_person_data)

            # obj_person stores object values of persons created calling object constructor Person
            obj_person = Person(parsed_data["first_name"], parsed_data["last_name"])

            # add string values corresponding to object values in a list using method get_name() in Person Class
            main_person_list.append(obj_person.get_name())

            # add list of friends to a list, for all persons
            list_all_friends.append(parsed_data["my_connection"])

            # add the object values of the person to the list
            list_all_people.append(obj_person)

        # function call:link_connection_obj(arg1,arg2,arg3) for object value creation check & return list of objects
        return link_connection_obj(main_person_list, list_all_friends, list_all_people)

    # respond if any exception occurs in preceding try clause
    except Exception as e:
        print("Exception occurred while loading people " + str(e))
        return False


# main function
if __name__ == "__main__":

    # function call: load_people()
    objectPerson = load_people()

    # validation to check list of object values is returned as expected
    # print(objectPerson)
    # validation to ensure the object values created for person may it be person or friend is same
    # print(objectPerson[199].get_friends())
    # print(objectPerson[125].get_friends())
