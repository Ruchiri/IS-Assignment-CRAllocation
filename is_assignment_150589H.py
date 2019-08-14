#get user inputs of input file and output file
input_file= input("Enter input file name:")
output_file=input("Enter output file name:")

input_data=[]
subjects=[]
rooms=[]
time_slots={}
assignments=[]

import csv
#read input csv file and add subjects and rooms
with open(input_file+'.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile)
     for row in spamreader:
        input_data.append(row)
subjects=input_data[:-1]
rooms=input_data[-1]

#add subjects
for subject in subjects:
   for time_slot in subject[2:]:
      if(time_slot not in time_slots):
         time_slots[time_slot]=-1
   assignments.append([subject[0],-1,-1])

#assign time slots and rooms depending on class type
def backtracking_search(assignments, time_slots,depth):
   if (depth == len(assignments)):
        return True   
   subject = subjects[depth][0]
   available_slots = subjects[depth][2:]
   class_type = subjects[depth][1]
   if (class_type == "c"):
      for time_slot in available_slots:
         if (time_slots[time_slot] == -1):
               assignments[depth] = [subject, time_slot, rooms[0]]
               time_slots[time_slot] = rooms[0]
               if (backtracking_search(assignments, time_slots, depth+1)):
                  return True
               else:
                  time_slots[time_slot] = -1
                  assignments[depth] = [subject, -1, -1]
      else:
         return False
   elif (class_type == "o"):
      for time_slot in available_slots:
         if (time_slots[time_slot] == -1):
               assignments[depth] = [subject, time_slot, rooms[0]]
               time_slots[time_slot] = [rooms[0]]
               if (backtracking_search(assignments, time_slots, depth+1)):
                   return True
               else:
                  time_slots[time_slot] = -1
                  assignments[depth] = [subject, -1, -1]
         elif (type(time_slots[time_slot]) == list):
               assign_rooms = time_slots[time_slot]
               temp_rooms = assign_rooms[:]
               if (len(assign_rooms) == len(rooms)):
                  continue;
               assign_rooms.append(rooms[len(assign_rooms)])
               assignments[depth] = [subject, time_slot, assign_rooms[-1]]
               time_slots[time_slot] = assign_rooms
               if (backtracking_search(assignments, time_slots, depth+1)):
                  return True
               else:
                  time_slots[time_slot] = temp_rooms
                  assignments[depth] = [subject, -1, -1]
      else:
         return False
#if timetable assignment successful, write results to a csv file
if(backtracking_search(assignments, time_slots, 0)):
   print ("Assignment successful!")
   with open(output_file+'.csv','w') as resultFile:
      wr = csv.writer(resultFile, dialect='excel')
      wr.writerows(assignments)
else:
   print ("Assignmnet failure!")
   








































