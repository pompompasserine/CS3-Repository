class Starship:


    def _init_(self, base_weight, cargo_weight, final_fuel):
        self.base_weight = base_weight
        self.cargo_weight = cargo_weight
        self.final_fuel = final_fuel
    
    def calculatefuel(self):
        base_weight = 5000
        total_weight = base_weight + self.cargo_weight
        return total_weight * 3

    def load_cargo(self):
        cargo_weight =+ 1000
        
        

Starship = Starship()
Starship.load_cargo()
Starship.load_cargo()
Starship.load_cargo()

Starship.calculatefuel()