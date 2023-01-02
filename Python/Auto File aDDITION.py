from datetime import date
now = date.today()
date3 = now.strftime("%B %d, %Y")
question = input("Did Teacher join class? (True/False): ")
if question == 'yes' or question == 'Yes' or question == 'True' or question == 'true':
    file = open("Did Teacher Join Class.txt", "a")
    file.write("Teacher Joined Class on " + date3 + "\n")
    file.close()
elif question == 'No' or question == 'no' or question == 'False' or question == 'false':
    file = open("Did Teacher Join Class.txt", "a")
    file.write("Teacher Did Not Join Class on " + date3 + "\n")
    file.close()