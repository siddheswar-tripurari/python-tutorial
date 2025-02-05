class bird:

    # attributes
    wings=2
    legs=2
    beak=1

    # functions or methods
    def eat(self):
        print("I am eating")
    
    def fly(self):
        print("I am flying")

    def make_sounds(self):
        print("I am chirping")
    
    def about(self,name):
        print("I am %s. I have %s wings and %s legs and %s beak." % (name,self.wings,self.legs,self.beak))

# creating objects

bluebird = bird()
sparrow = bird()

print(bluebird.eat())
sparrow.about("Sparrow")
