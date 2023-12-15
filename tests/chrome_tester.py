from chromosome import Evolver


def find_different_indices(s1, s2):
    # Find indices of different characters
    different_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]

    return different_indices


# jump_chrome = [['100101010']]
# print("Input: {}".format(jump_chrome))
# #print("IsJumpGene: {}".format(Evolver.isJumpGene(jump_chrome[0])))

# #for i in range(10):
# #    mut = Evolver.mutate(jump_chrome, 1)
# #    print("Mutated: {}".format(Evolver.mutate(jump_chrome, 1)))
# #    print(find_different_indices(mut[0][0], jump_chrome[0][0]))


# action_chrome = [['000101010']]
# print("Input: {}".format(action_chrome))
# #print("IsJumpGene: {}".format(Evolver.isJumpGene(jump_chrome[0])))

# for i in range(10):
# 	mut = Evolver.mutate(action_chrome, 1)
# 	print("Mutated: {}".format(Evolver.mutate(action_chrome, 1)))
# 	print(find_different_indices(mut[0][0], action_chrome[0][0]))

chrome1 = [['100001111', '011011111', '011010001', '011111000', '011000010', '000000111', '000101111', '010011001'], ['100011001', '001101110', '000000110', '010111000', '000000000', '001011011', '010011110', '001001111'], ['100101100', '011011100', '001101000', '011100111', '011001010', '000110100', '001111101', '001111010'], ['100110111', '010100101', '001010100', '010000011', '001101111', '000100011', '000001010', '001110111'], ['101001010', '001111000', '011011111', '001011100', '011001000', '011101110', '001100110', '001100001'], ['101011100', '011010000', '000001000', '010100111', '010100110', '011001100', '010100001', '010010110'], ['101100000', '010011101', '000000101', '000000001', '001101100', '000001001', '010101111', '000010000'], ['101110111', '011110011', '011101011', '001011000', '010011010', '010001011', '010100010', '010100100'], ['110001100', '010111111', '001000001', '000011100', '010111100', '011010110', '001110111', '000011011'], ['110010101', '011010101', '001010111', '010001110', '011001000', '001100100', '011001011', '000011111'], ['110100111', '010111011', '011001011', '001101100', '011010100', '000010100', '010110101', '011011011'], ['110110100', '010011111', '010000000', '010011010', '011001101', '010111000', '011001110', '000101011'], ['111000001', '000000110', '000010110', '011111011', '011011010', '011011000', '010110100', '011011101'], ['111010011', '010010111', '010110000', '000010001', '011111100', '000010100', '000100100', '010011100'], ['111100000', '000110110', '000101101', '010110011', '010011111', '001101000', '011001111', '001101010'], ['111111011', '001001001', '011001011', '000011001', '010110100', '011001011', '000011111', '000000000']]
chrome2 = [['100001001', '010001000', '001000010', '010101111', '000001111', '001000000', '011111111', '010100000'], ['100011101', '001111111', '011100000', '001110100', '000000100', '000111000', '000000111', '001100010'], ['100101100', '001000010', '010010011', '000000110', '001000100', '011100110', '010101101', '000101010'], ['100110010', '000011101', '010111100', '011010011', '000111101', '000011011', '000111010', '011110001'], ['101001100', '001100101', '010101001', '001011001', '010110001', '011111100', '001001101', '001100000'], ['101010100', '000010011', '001111011', '001101011', '011010000', '000101101', '011011001', '010001101'], ['101100000', '000010111', '000011011', '000111001', '000000000', '011010111', '001101111', '001101000'], ['101111100', '010010011', '001100011', '010000000', '001011110', '000000100', '011000111', '000110101'], ['110001011', '010001000', '001011111', '000110100', '010110001', '001011010', '001111001', '001001011'], ['110011011', '001011100', '000110010', '001000101', '001000001', '001000101', '000010110', '000001111'], ['110100110', '010011001', '010001100', '001011010', '000101010', '000111010', '000010101', '000001111'], ['110111000', '010101011', '001011011', '001011010', '000001001', '000010010', '000101010', '000110110'], ['111001100', '000010011', '011101100', '011101001', '001100110', '010011011', '011111110', '011110101'], ['111010011', '001100001', '011011101', '010011100', '000000111', '010000000', '001011010', '001110101'], ['111100100', '000110100', '010011001', '010001111', '011100111', '001000100', '010000101', '011101001'], ['111111000', '001001101', '010010001', '011111110', '010010010', '000001010', '001111001', '001000110']]

cross_child = Evolver.crossover(chrome1, chrome2)
print("Crossed: {}".format(cross_child))
mut_child = Evolver.mutate(cross_child, 1)
print("Mut Child: {}".format(mut_child))
