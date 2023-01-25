class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    
    @staticmethod
    def print_in_row(array):
        for c in range(len(array)):
            print(c, end = "")
            if c < len(array)-1:
                print("-", end = "")
        
            
my_array = [4,1,8,7,2]

Arrays().print_in_col(my_array)
Arrays().print_in_row(my_array)

