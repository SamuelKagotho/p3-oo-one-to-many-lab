class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []  
    
    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception(f"Invalid type for name: {type(name).__name__}. Expected str.")
        
        if not isinstance(pet_type, str):
            raise Exception(f"Invalid type for pet_type: {type(pet_type).__name__}. Expected str.")
        
        if owner is not None and not isinstance(owner, Owner):
            raise Exception(f"Invalid type for owner: {type(owner).__name__}. Expected Owner or None.")
        
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Valid types are: {', '.join(Pet.PET_TYPES)}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        if owner:
            owner.add_pet(self)
        
        Pet.all.append(self)  


class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception(f"Invalid type for name: {type(name).__name__}. Expected str.")
        self.name = name
        self._pets = []  

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        pets = self.pets()
        if not all(isinstance(pet, Pet) for pet in pets):
            raise Exception("All pets must be instances of the Pet class.")
        
        return sorted(pets, key=lambda pet: pet.name)

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception(f"Invalid pet type: {type(pet).__name__}. Expected Pet.")
        
        if pet.owner is not None and pet.owner != self:
            raise Exception(f"Pet already has an owner: {pet.owner.name}.")
        
        self._pets.append(pet)
        pet.owner = self  