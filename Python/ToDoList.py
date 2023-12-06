class task:
    def __init__(self, name, doneOrNot=False):
        self.name = name
        self.done_or_not = doneOrNot
        
    def __str__(self):
        return f'Task: {self.name} // Are the task done?: {self.done_or_not}'    
          
    def is_done(self):
        self.done_or_not = True
    
    def is_not_done(self):
        self.done_or_not = False
        
    def change_task_status(self, name):
        self.name = name

class toDoList():
    def __init__(self, name='ToDoList'):
        self.task_list = []
    
    def add_task(self, name, doneOrNot=False):
        self.task_list.append(task(name))
        
    def remove_task(self, name):
        for t in self.task_list:
            if t.name == name:
                self.task_list.remove(t)
                
    def get_task(self, name):
        for t in self.task_list:
            if t.name == name:
                print(t)
               
    def done_tasks(self):
        are_done = [t for t in self.task_list if t.done_or_not]
        for t in are_done:
            print(t)
        
    def not_done_tasks(self):
        not_done = [t for t in self.task_list if t.done_or_not == False]
        for t in not_done:
            print(t)
            
    def list_tasks(self):
        for t in self.task_list:
            print(t)
            
    def do_task(self, name):
        for t in self.task_list:
            if t.name == name:
                t.done_or_not = True
                
    def undo_task(self, name):
        for t in self.task_list:
            if t.name == name:
                t.done_or_not = False
                
class menu:
    def __init__(self):
        self.menu_options = ['a', 'r', 't', 'd', 'x', 'o', 'u', 'e']
        
    def user_option(self):
        while(True):
            print()
            print('===== To Do List =====') 
            print('a: Add task')
            print('r: Remove task')
            print('t: List tasks')
            print('d: Done tasks')
            print('x: Tasks to do')
            print('o: Do task')
            print('u: Undo task')
            print('e: Exit')  
        
            user_input = input('Enter an option: ')
        
            if user_input in self.menu_options:
                return user_input
        
            else:
                print()
                print('Option not available!!')
                
            return user_input       
    

def main():
    menu_options = ['a', 'r', 't', 'd', 'x', 'o', 'u']
    task_list = toDoList()
    options_menu = menu()
    
    while True:
        user_input = options_menu.user_option()

        if user_input == 'e':
            break
        elif user_input == 'a':
            task_name = input('Enter task name: ')
            task_list.add_task(task_name)
        elif user_input == 'r':
            task_list.list_tasks()
            task_name = input('Enter task name: ')
            task_list.remove_task(task_name)
        elif user_input == 't':
            task_list.list_tasks()
        elif user_input == 'd':
            task_list.done_tasks()
        elif user_input == 'x':
            task_list.not_done_tasks()
        elif user_input == 'o':
            task_list.not_done_tasks()
            task_name = input('Enter task name: ')
            task_list.do_task(task_name)
        elif user_input == 'u':
            task_list.done_tasks()
            task_name = input('Enter task name: ')
            task_list.undo_task(task_name)
   
        
if __name__ == '__main__':
    main()