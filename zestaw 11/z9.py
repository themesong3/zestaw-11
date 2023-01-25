import random
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
                
    @staticmethod #A
    def copy_printer(num, e):
        return [e] * num
    
    @staticmethod #B
    def random_range(num, start, finish):
        new_array = [0] * num
        for i in range(len(new_array)):
            new_array[i] = random.randint(start, finish)
        return new_array       
    
    @staticmethod #C
    def num_elem_in_range(array, start, finish):
        counter = 0
        for i in array:
            if i >= start and i <= finish:
                counter += 1
        return counter
     
            
my_array = [4,1,8,7,2]

Arrays().print_in_col(my_array)

Arrays().print_in_row(my_array)

new_array = Arrays().copy_printer(10, "A")
print(new_array)

new_array = Arrays().random_range(10, 1, 20)
print(new_array)


z9c = Arrays().num_elem_in_range(new_array, 4, 7)
print(z9c)


