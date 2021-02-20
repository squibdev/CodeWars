def DNA_strand(dna):
    return dna.translate(dna.maketrans('ATCG', 'TAGC'))

"""
def DNA_strand(dna):
    output = ''
    for l in dna:
        if l == 'A':
            output+='T'
        if l == 'T':
            output+='A'
        if l == 'C':
            output+='G'
        if l == 'G':
            output+='C'
            
    return output
"""