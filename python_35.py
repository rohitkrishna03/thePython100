# what is the use of using  if__name =="__main"
# the if__name =="__main__" idiom is the common pattern used in python scripts to determine
# whether the scripts is being run directly or being imported as a module into another script
# in python , the __name__ variable is a built-in variable that is automitically set
# to the current module.
# when a python scripts is rn directly, the __name__ variable is set to the string __main__ 
# when the script is imported as a module into another script, the __name variable is set to the name of the module.
# here lets take 2 files like rohit.py and main.py

# # in rohit.py i will create
# def welcome():
#     print("you are welcome form rohit")
#     welcome()
#     if __name__ =="__main__":
    
    
    
    
    # # and in the main.py we will create 
    # import rohit
    # rohit.welcome()
    
    