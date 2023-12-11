#chromsome interpretation



# 16 loops -> big actions (states) referred to as chrome
# Each loop has 8 genes (instructions/jump/action) referred to as gene
# Conditionals jump to other states

def readChrome(chrome):
	loops = []
	for gene in chrome:
		#print("Current gene: {}".format(gene))
		
		loop = []		
		for instruction_gene in gene:
			#print("Current Instruction gene: {}".format(instruction_gene))
			
			
			if instruction_gene[0] == '1': # Case for jump chrom
				
				conditional_index = int(instruction_gene[1:5], 2)
				loop_number = int(instruction_gene[5:], 2)
				
			    # Structure: False, conditional index, jump to num	
				loop.append([False, conditional_index, loop_number])
				
				
				
				#print("Conditional loop: {}".format(conditional_index))
				#print("Loop number: {}".format(loop_number))
				
			else: # Case for action chromosome
				shoot = bool(int(instruction_gene[1]))
				thrust = bool(int(instruction_gene[2]))
				turn_quantity = int(instruction_gene[3:6], 2)
				turn_target = int(instruction_gene[6:], 2)
				
				#print("Shoot: {}".format(shoot))
				#print("Thrust: {}".format(thrust))
				#print("Turn Quantity: {}".format(turn_quantity))
				#print("Turn Target: {}" .format(turn_target))
				
				# If first val is true, action gene
				loop.append([True, shoot, thrust, turn_quantity, turn_target])
		loops.append(loop)

	return loops
#gene = [['100001111', '001111001', '010101101', '100111000']]
chromosome = [['100001111', '001111001', '010101101', '000111000'], ['101111001', '000111000']]
print(readChrome(chromosome))


#if checkConditional(conditional_index):
					# gene = chrome[conditional_index]
					# TODO GoTo loop_number
					#pass
					#print("Loop num: {}".format(loop_number))


