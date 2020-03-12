def is_multiple(n, m):
    "Function that takes two integer values (n, m).  "
    "Returns True if 'n' is a multiple of 'm'.  Otherwise, returns False."
    
    #check to be sure parameters are integers
    if isinstance(n, int) == True and isinstance(m, int) == True:
        try:
            return n % m == 0  # result 0 means 'n' is multiple of 'm' - returns True.  Otherwise returns False
         
        #if m is 0 - this will cause mathematical error - show message
        except ZeroDivisionError:
            print("Invalid 'm' parameter passed in.  Cannot be 0.")      
    
    #parameters were not integers - show message
    else:
        print("Invalid parameter(s) passed in.  They must both be integers.")  