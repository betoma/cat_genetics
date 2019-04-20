import random

class Gene:
    """ Gene class represents a single gene and allows for defining and creating said gene's alleles, allowed genotypes, etc. """
    
    VALID_DOM_TYPES = {"simple","incomplete","complex"}
    MATRIX_RELATIONS = {"dom","rec","inc"}

    def __init__(self, dominance_type: str, alleles: list, *phenotypes: str, sex_chrom: bool=False, y_alleles: list=None, custom_matrix: list=None, y_trait_phenotypes: list=None, custom_male_matrix: list=None, complex_y_linked: bool=False, custom_y_linked_matrix: list=None, **assignments):
        """ Create a new gene with alleles from a given list """
        self.sex_chrome = sex_chrom
        self.allele_types = set(alleles)
        self.alleles = alleles
        self.phenotypes = phenotypes
        self.genotype = set()
        self.simple_pheno_map = dict()
        no_of_alleles = len(alleles)
        if len(phenotypes) > no_of_alleles:
            self.inc_phenotypes = phenotypes[no_of_alleles:]
            self.inc_phenomap = dict()
        else:
            self.inc_phenotypes = None
            self.inc_phenomap = dict()
        for i,a in enumerate(alleles):
            self.simple_pheno_map[a] = phenotypes[i]
        if custom_matrix:
            self.dom_matrix = custom_matrix
        else:
            self.dom_matrix = list()
            for _ in alleles:
                self.dom_matrix.append(list())
            if sex_chrom:
                if not y_alleles:
                    raise ValueError("Gene: if sex_chrome is True, valid y_alleles must be provided")
                else:
                    self.y_allele_types = set(y_alleles)
                    self.alt_allele_types = self.allele_types.union(self.y_allele_types)
                    if len(y_alleles) >= 1 and not y_trait_phenotypes:
                        raise ValueError("Gene: if more than one y_allele is provided, phenotypes must be provided for additional y_alleles")
                    elif custom_male_matrix:
                        self.male_matrix = custom_male_matrix
                    else:
                        self.male_matrix = list()
                        for _ in alleles:
                            self.male_matrix.append(list())
                        for i,_ in enumerate(self.male_matrix):
                            for _ in alleles:
                                self.male_matrix[i].append("dom")
                    if complex_y_linked:
                        if not custom_y_linked_matrix:
                            raise ValueError("Gene: if complex y linked traits are to be used, a custom y linked matrix must be provided")
                        else:
                            self.y_linked_matrix = custom_y_linked_matrix
                    else:
                        self.y_linked_matrix = None
            else:
                self.y_allele_types = None
                self.alt_allele_types = self.allele_types
                self.male_matrix = None
                self.y_linked_matrix = None
            if dominance_type in Gene.VALID_DOM_TYPES:
                if dominance_type == "simple":
                    for i,_ in enumerate(self.dom_matrix):
                        for j,_ in enumerate(alleles):
                            if i <= j:
                                self.dom_matrix[i].append("dom")
                            else:
                                self.dom_matrix[i].append("rec")
                elif dominance_type == "complex":
                    raise ValueError("Gene: dominance type 'complex' requires a custom matrix")
                else:
                    for i,_ in enumerate(self.dom_matrix):
                        for j,_ in enumerate(alleles):
                            if i == j:
                                self.dom_matrix[i].append("dom")
                            else:
                                self.dom_matrix[i].append("inc")
            else:
                raise ValueError("Gene: dominance type must be one of {}".format(Gene.VALID_DOM_TYPES))

test = Gene("simple", ["L","l"], "long", "short")
print(test.dom_matrix)
print(test.inc_phenotypes)