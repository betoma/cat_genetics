import random

class Cat(object):
    """ Cat class represents a single cat's genotype """
    def __init__(self,sex="random",length="random",orange="random",eumelanin="random",dilution="random"):
        """ Create a new cat with a given genotype """
        self.Alleles = { 'sex_chrom' : set(), 'length' : set(), 'eumelanin' : set(), 'dilution' : set() }
        #---these constants allow for easy error handling---#
        VALID_SEX = {"male","female"}
        VALID_LENGTH = {"long","short"}
        VALID_ORANGE = {"red","black","tortie"}
        VALID_EUMEL = {"black","chocolate","cinnamon"}
        VALID_DILUTE = {"dilute","nondilute"}
        #--various allele constants--#
        LENGTH_ALLELES = {"L","l"}
        DILUTE_ALLELES = {"D","d"}
        #---sex chromosomes (and sex-linked traits like orange)---#
        orange = decideTypes(orange,VALID_ORANGE)
        if sex == "male" and orange == "tortie":
            raise ValueError("{}: cat cannot be both male and tortoiseshell".format(self))
        elif orange == "tortie":
            sex1 = "XO"
            sex2 = "Xo"
        else:
            sex_choice = decideTypes(sex,VALID_SEX,True)
            if orange == "random":
                x_choices = {"XO","Xo"}
            elif orange == "black":
                x_choices = {"Xo"}
            elif orange == "red":
                x_choices = {"XO"}
            sex1 = pickOne(x_choices)
            if sex_choice == "male":
                sex2 = "Y"
            else:
                sex2 = pickOne(x_choices)
        self.Alleles['sex_chrom'].add(sex1)
        self.Alleles['sex_chrom'].add(sex2)
        #---coat length---#
        length = decideTypes(length,VALID_LENGTH)
        if length == "long":
            length1 = "l"
            length2 = "l"
        else:
            if length == "short":
                length1 = "L"
            else:
                length1 = pickOne(LENGTH_ALLELES)
            length2 = pickOne(LENGTH_ALLELES)
        self.Alleles['length'].add(length1)
        self.Alleles['length'].add(length2)
        #---eumelanin density---#
        eumelanin = decideTypes(length,VALID_EUMEL)
        if eumelanin == "cinnamon":
            eu1 = "bl"
            eu2 = "bl"
        else:
            if eumelanin == "chocolate":
                eu1 = "b"
                eumel_alleles = {"bl","b"}
                eu2 = pickOne(eumel_alleles)
            else:
                eumel_alleles = {"B","b","bl"}
                eu1 = pickOne(eumel_alleles)
                if eumelanin == "black":
                    eu2 = "B"
                else:
                    eu2 = pickOne(eumel_alleles)
        self.Alleles['eumelanin'].add(eu1)
        self.Alleles['eumelanin'].add(eu2)
        #---dilution---#
        dilution = decideTypes(length,VALID_DILUTE)
        if dilution == "dilute":
            dil1 = "d"
            dil2 = "d"
        else:
            if dilution == "nondilute":
                dil1 = "D"
            else:
                dil1 = pickOne(DILUTE_ALLELES)
            dil2 = pickOne(DILUTE_ALLELES)
        self.Alleles['dilution'].add(dil1)
        self.Alleles['dilution'].add(dil2)

def pickOne(valid_items: set):
    chosenOne = random.choice(tuple(valid_items))
    return chosenOne

def decideTypes(attribute: str, valid_items: set, make_choose: bool=False):
    if attribute == "random":
        if make_choose:
            decision = pickOne(valid_items)
        else:
            decision = attribute
    elif attribute in valid_items:
        decision = attribute
    else:
        raise ValueError("{}: sex must be one of {} or 'random'.".format(attribute,valid_items))
    return decision

kitty = Cat()
print(kitty.Alleles)