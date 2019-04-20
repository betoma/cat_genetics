import random
from alleles import Gene

class Cat:
    """ Cat class represents a single cat's genotype """
    def __init__(self):
        """ Create a new cat with a given genotype """
        self.Alleles = { 'sex_chrom' : Gene("incomplete",["XO","Xo"],"red","black","tortie",sex_chrom=True,y_alleles=["Y"]), 'length' : Gene("simple",["L","l"],"long","short"), 'eumelanin' : Gene("simple",["B","b","bl"], "black", "chocolate", "cinnamon"), 'dilution' : Gene("simple",["D","d"],"dilute","nondilute") }

kitty = Cat()
print(kitty.Alleles)