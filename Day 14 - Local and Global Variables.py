# Local and Global Variables

# As summary:
# There are two kind of type of variables.
# Local - You can use only where you define that variable.
# Global - You can use everywhere. When you make any changes,
#that affect to that variable.

#Some examples for Local Variables:

def Stephen():
    a = 2
    print(a)


#You can't call the variable 'a'
#And you can create another variable which is 'a'

Stephen()
a = 3
print(a)

# they are two different variables.
# And second 'a' is an example for Global Variables.
# You can call that variable everywhere.
# DO NOT FORGET: Any changes affect that GLOBAL VARIABLE!
# let's SEE:

print("A is currently:", a)
import time
print("A is changing..")
time.sleep(2)
a = 78
print("A is changed. New value of A:", a)


# P.S: If a variable defined in a class, in a loop etc. That's makes that variable Local.