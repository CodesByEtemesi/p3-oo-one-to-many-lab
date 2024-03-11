class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Pet type must be one of: {}".format(self.PET_TYPES))
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet class can be added as pets.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets



owner1 = Owner("Etemesi")
owner2 = Owner("Okune")

pet1 = Pet("Bob", "dog", owner1)
pet2 = Pet("Luna", "cat", owner1)
pet3 = Pet("Micky", "rodent", owner2)

print(owner1.get_sorted_pets())  
print(owner2.get_sorted_pets()) 

owner1.add_pet(pet3)  