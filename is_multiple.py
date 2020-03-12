def is_multiple(n, m):
    "Function that takes two integer values (n, m).  "
    "Returns True if 'n' is a multiple of 'm'.  Otherwise, returns False."
    
    #check to be sure parameters are integers
    if isinstance(n, int) == False or isinstance(m, int) == False:
        print("Invalid parameter passed in.  These must be integers.")
        
        
    else:
        
        #if 0 remainder when dividing, then this is a multiple and returns True.
        #else if not 0 remainder when dividing, then this is not a multiple and returns False.
        return n % m == 0
    
