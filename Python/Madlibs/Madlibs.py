# string concantenation (how to put string together)
# we want to create a string that says "subscribe to _____"
# youtuber = "Splashjackson" # some string varible

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subcribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous person: ")

madlib = f"Computer programming is so" + {adj} + "! It makes me so exited all the time because \ "
"I love to" + {verb1} + "." "Stay loyal and" + {verb2} + "like you are" + {famous_person} + "!"

print(madlib)
