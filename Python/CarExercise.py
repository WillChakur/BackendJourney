class carExercise:
    def __init__(self, velocity):
        self.Max_velocity = velocity
        self.current_velocity = 0
        
    def speed_up(self, add_velocity):
        if(self.current_velocity + add_velocity) > 180:
            print('You need to go slower')
        else:
            self.current_velocity += add_velocity
     
    def slow_down(self, decrease_velocity):
        if(self.current_velocity - decrease_velocity) < 0:
            self.current_velocity = 0
        else:
            self.current_velocity -= decrease_velocity
            
    def __str__(self):
        return f'Current velocity: {self.current_velocity}'
    
    
         
if __name__ == '__main__':
    c1 = carExercise(180)
    c1.speed_up(180)
    print(c1)
    c1.slow_down(200)
    print(c1)

    