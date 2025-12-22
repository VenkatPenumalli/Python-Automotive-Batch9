class Dog:
    #first define common and then unique
    def _init_(self,name,age):
        self.name = name
        self.age = age
#Dog Barks
#Behaviour of parent class
    def bark(self):
        #Attribures unique to each instance of dog class
        return "{self.name} says Woof!"
    
#Objects : Instances of a class dog
#dog1 is a Dog
#dog2 is a DOg
dog1 = Dog("Lucy",4)
dog2 = Dog("Test",2)
#As many number of dogs as per the requirement

dog1.bark()
dog2.bark()