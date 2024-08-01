import random
import sys


def groupPicker():
    while True:

        try:
            print("This is a random group picker read and follow the prompts.")
            groupNo = int(input("What number of groups would you like?"))
            peopleNo = int(input("How many people are there?"))
            if groupNo == 'Q':
                sys.exit(0)
            print("Number each person from 1 to", peopleNo, ".")

            nums = []
            for i in range(1, peopleNo+1):
                nums.append(i)

            if peopleNo % groupNo:
                print("You have an incorrect number of people to divide them into groups equally")
                sys.exit(1)

            peoplePerTeam = int(peopleNo/groupNo)

            group = {}
            for i in range(1,groupNo+1):
                group[i] = set()

            for person in nums:
                while True:
                    randomGroup = random.randint(1,groupNo)

                    if len(group[randomGroup]) < peoplePerTeam:
                        group[randomGroup].add(person)
                        break

            for i in range(1,groupNo+1):
                print("Team %s members are %s" %(i, group[i]))

        except:
            print("Only input integers")
            break


groupPicker()