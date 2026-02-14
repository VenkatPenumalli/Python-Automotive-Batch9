class Kanban:
    def __init__(self):
        self.todo = []
        self.progress = []
        self.done = []
        
    def add_assignments(self,assignment):
        self.todo.append(assignment)
        
    def progress_assignment(self,assignment):
        if assignment in self.todo:
            self.todo.remove(assignment)
            self.progress.append(assignment)
        else:
            print("Assignment not listed")
    
    def finished_assignments(self,assignment):
        if assignment in self.progress:
            self.progress.remove(assignment)
            self.done.append(assignment)
        else:
            print("Assignment not listed")
    
    def view(self):
        print("KABAN BOARD")
        print("TO DO",self.todo)
        print("In Progress",self.progress)
        print("Done",self.done)

kanban = Kanban()

while True:
    Options = input("Enter 1 for Add, 2 for Progression, 3 for finished, 4 for exit :: ")
    if Options == "1":
        m = int(input("How many assignments to be added :: "))
        for i in range(m):
            add = str(input("Enter the subjects :: "))    
            kanban.add_assignments(add)
    elif Options == "2":
        n = int(input("Enter no of assignments to be added in Progress :: "))
        for i in range(n):
            add_2 = str(input("Enter the assignments to be In Progress :: "))    
            kanban.progress_assignment(add_2)
    elif Options == "3":
        o = int(input("Enter no of assignments to be added in Done :: "))    
        for i in range(o):
            add_3 = str(input("Enter the Completed assignments :: "))
            kanban.finished_assignments(add_3)
    elif Options == "4":
        print("Closed the Kanban")  
        break 
    else:
        print("Enter a Valid Option!")
    kanban.view()