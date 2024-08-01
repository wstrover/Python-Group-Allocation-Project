# Imports
# Maybe change from lists into a dictionary and just make a string with _ between then seperate
# (eg. ws144_vm113 = ws144 /n vm133)
import pandas as pd
import openpyxl
import random

from xlsxwriter import Workbook

from project import app, db
from project.models import Grouping
import asposecells



# reading the Excel doc
#df = pd.read_excel(r'\Users\willi\CO2201\CO2201(1).xlsx')
# Turning dataframe into List of Lists for ease of use
#dict = df.to_numpy().tolist()
# Copies for simultaneous testing
#dict1 = dict


#List Setups
Spice_up_your_life = []
Ungrading_Simulator = []
Group_Allocation_System = []
Optical_recognition_in_Online_Games = []
Mapping_Cities_in_Python = []
VICTA_Desktop = []
VICTA_Mobile_App = []
Scrapping_Job_listing_websites = []

ListofNames = ["Spice_up_your_life", "Ungrading_Simulator", "Group_Allocation_System", "Optical_recognition_in_Online_Games", "Mapping_Cities_in_Python", "VICTA_Desktop", "VICTA_Mobile_App", "Scrapping_Job_listing_websites"]
ListofSubs = [Spice_up_your_life, Ungrading_Simulator, Group_Allocation_System, Optical_recognition_in_Online_Games, Mapping_Cities_in_Python, VICTA_Desktop, VICTA_Mobile_App, Scrapping_Job_listing_websites]

FC = []
SC = []
TC = []
#                1   2   3   4   5   6   7   8   9   10
Userinf = [[], [], [], [], [], [], [], [], [], []]

names = []


# functions

# sets up the choices lists depending on how many choices the students can make

def setupinf(dictionary):
    for x in range(len(dictionary)):
        for i in range(len(dictionary[x])):
            l = i
            if i >= 1:
                l = i+1
            Userinf[l].append(dictionary[x][i])
    print(Userinf)


def setupclists(dictionary):
    nc = len(dictionary[0])-1
    if nc == 1:
        for i in range(len(dictionary)):
            names.append(dictionary[i][0])
        for i in range(len(dictionary)):
            FC.append(dictionary[i][1])
    elif nc == 2:
        for i in range(len(dictionary)):
            names.append(dictionary[i][0])
        for i in range(len(dictionary)):
            FC.append(dictionary[i][1])
        for i in range(len(dictionary)):
            SC.append(dictionary[i][2])
    elif nc == 3:
        for i in range(len(dictionary)):
            names.append(dictionary[i][0])
        for i in range(len(dictionary)):
            FC.append(dictionary[i][1])
        for i in range(len(dictionary)):
            SC.append(dictionary[i][2])
        for i in range(len(dictionary)):
            TC.append(dictionary[i][3])

# checks for the students matching first,second, or third choice
def Ccheck(numberchoice, choiname, listforuse, dictionary):
    for i in range(len(dictionary)):
        if str(dictionary[i][numberchoice]) == choiname:
            listforuse.append(str(dictionary[i][0]))
            dictionary.pop(i)
            FC.pop(i)
            SC.pop(i)
            TC.pop(i)
            break

# used for when a student has to be put into a group with no more remaining students as it for a choice
def randomc(listforuse, dictionary):
    if len(dictionary) != 0:
        listforuse.append(str(dictionary[0][0]))
        dictionary.pop(0)
        FC.pop(0)
        SC.pop(0)
        TC.pop(0)

# checks for if any students have the group as a choice and then calls the proper search protocol
def listchoice(listforuse, choiname, dictionary):
    if choiname in FC:
        Ccheck(1, choiname, listforuse, dictionary)
    elif (choiname not in FC) and (choiname in SC):
        Ccheck(2, choiname, listforuse, dictionary)
    elif (choiname not in FC) and (choiname not in SC) and (choiname in TC):
        Ccheck(3, choiname, listforuse, dictionary)
    elif (choiname not in FC) and (choiname not in SC) and (choiname not in TC):
        randomc(listforuse, dictionary)

# not useful rn, have to change it but trust
def toString(List):
    name = (str(List))
    for i in range(len(List)):
        print(List[i])

# doesn't matter rn
def averager(Lists):
    av = 0
    for i in range(len(Lists)):
        av = av + len(Lists[i])
    av = av / len(Lists)
    return av


def filler(Lists, ListofN, dictionary):
    av = 0
    count = 0
    maxim = (len(dictionary) / len(Lists)) + 1
    while len(dictionary) != 0:
        count = count + 1
        for i in range(len(Lists)):
            if len(Lists[i]) <= av:
                listchoice(Lists[i], ListofN[i], dictionary)
                av = averager(Lists)
        if count >= maxim:
            break
    add_db(Lists, ListofN)
    extoExcel(Lists, ListofN)
    #for i in range(len(Lists)):
        #print(ListofN[i])
        #toString(Lists[i])

# add to database to allow the teacher to change things better
def add_db(Lists, ListofN):
    # I really hope this works irl
    # db.session.query(my Life).delete()
    db.session.query(Grouping).delete()
    db.session.commit()
    for i in range(len(Lists)):
        for x in range(len(Lists[i])):
            grouped = Grouping.query.filter_by(username=str(Lists[i][x])).first()
            if (i == 0) and (x == 0):
                grouper = Grouping(username=Lists[i][x], group=ListofN[i])
                db.session.add(grouper)
                db.session.commit()
            else:
                if not grouped:
                    grouper = Grouping(username=Lists[i][x], group=ListofN[i])
                    db.session.add(grouper)
                    db.session.commit()


def extoExcel(Lists, ListofN):
    xlsheet = Workbook("vinceent.xlsx")
    xlsheets = xlsheet.add_worksheet()
    count = 1
    for i in range(len(Lists)):
        for x in range(len(Lists[i])):
            xlsheets.write('A'+str(count), Lists[i][x])
            xlsheets.write('B'+str(count), str(ListofN[i]).replace("_", " "))
            count = count + 1
    xlsheet.close()
