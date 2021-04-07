class EjercicioBasico:
    def __init__(self):
        self.list = [1,2,3,4,5,6,7,8,9,0]
        self.number_dict = {}

    def num_find(self, name):
        self.find_number = int(input('Add a number to find: '))
        for numbers in self.list:
            if self.find_number in self.list:
                self.number_dict[name] = [int(self.find_number)]
            else:
                print('the numbers isnt allowed')
                break
            
        return self.number_dict


exercise = EjercicioBasico()

print(exercise.num_find(input('Enter your name: ')))