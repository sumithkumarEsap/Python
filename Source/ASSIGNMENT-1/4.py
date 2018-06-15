Python = {"sumith","ravi","chaitu","raghu","shekar","rajiv","ram","morgan","yatish"}
web = {"kamal", "yatish", "reddy", "Yuvesh", "shekar","sumith","ravi"}

#sets provide us with the inbulit functions for union and intersections
#this gives the students who are in both python and web
print("students who are present in both python and web: {}".format(Python & web))
#this gives all the students who  present only in python
a = Python-web
print("students who are present only in python set are :{}".format(a))
#this gives all the student who are present only in web
b = web-Python
print("students who are  present only in web set are :{}".format(b))
#the elements which are only present in either web or python but not both
print("students who are present either in python or web but not in both are: {}".format(a.union(b)))