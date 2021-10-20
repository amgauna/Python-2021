# if a system has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of
# storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the
# calculate_storage function below. Which calculates the total number of baytes needed to store a file of a given size?

# calculate storage

def calculate_storage(filesize)
    block_size = 4096
	
    # Use floor division to calculate how many blocks are fully ocupied
    float full_blocks = filesize//block_size
	
    If full_blocks > 1 && full_blocks <= 2): 
       return 8192
    elif full blocks <= 1:
       return 4096
    
        # Use the modulo operator to check whether there´s any remainder
	partial_block_remainder = full_block%2
	
	# Depending on whether there´s a remainder or not, return
	# The totalnumber of bytes required to allocad enought blocks
	# to store your data.
	
	if patial_block_remainder > 0:
	   return (full_blocks + 1)*block_zise
	else
	   return (block_size)	
	   
return 2

print (calculate_storage(1)) # should be 4096	
print (calculate_storage(4096)) # should be 4096
print (calculate_storage(4097)) # should be 8192
print (calculate_storage(6000)) # should be 8192   
	
	
