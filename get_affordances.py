from inspect import signature
import mistyPy
import os

def log_misty_aff():
    with open('affordances.txt', 'w') as fp:
        for aff in dir(mistyPy.Robot):
            if aff[0] != '_':
                aff_log = "Affordance Name: {}\n\tParameters:".format(aff)
                for k in signature(getattr(mistyPy.Robot, aff)).parameters.keys():
                    if k != 'self':
                        aff_log += " {}".format(k)
                fp.write(aff_log + "\n\n")
    fp.close()
log_misty_aff()
