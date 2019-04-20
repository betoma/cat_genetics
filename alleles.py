import random

class Gene:
    """ Gene class represents a single gene and allows for defining and creating said gene's alleles, allowed genotypes, etc. """
    
    VALID_DOM_TYPES = {"simple","incomplete","complex"}
    MATRIX_RELATIONS = {"dom","rec","inc"}

    def __init__(self, dominance_type: str, alleles: list, *phenotypes: str, sex_chrom: bool=False, y_alleles: list=None, custom_matrix: list=None, **assignments):
        """ Create a new gene with alleles from a given list """
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
            if y_alleles:
                self.y_allele_types = set(y_alleles)
                self.alt_allele_types = self.allele_types.union(self.y_allele_types)
            else:
                self.y_allele_types = None
                self.alt_allele_types = self.allele_types
            for _ in alleles:
                self.dom_matrix.append(list())
            if not sex_chrom:
                if dominance_type in Gene.VALID_DOM_TYPES:
                    if dominance_type == "simple":
                        for i,_ in enumerate(self.dom_matrix):
                            for j,_ in enumerate(alleles):
                                if i <= j:
                                    self.dom_matrix[i].append("dom")
                                else:
                                    self.dom_matrix[i].append("rec")
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