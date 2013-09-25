# gc_content
# base_count('G')
# reverse complement


class DNAString:
    def __init__(self, sequence):
        self.seq = sequence

    def base_count(self, base):
        return self.sequence.count(base)

    def gc_content(self):
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)



