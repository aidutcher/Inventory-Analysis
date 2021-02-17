# Inventory Analysis 

Given a set of data including vendor, item, and stocking info, finds low movement items and presents best options

Create lists and variables 
	# Range containing rows where vendor code is specific value
	vendors 
	high_movement_list 
	low_movement_list
	# Maybe just an xls file w/ item, vendor, warehouse, usage
	suggested_transfers 
	suggested_rma
	

Define functions
	Calculate usage
	Write generic RMA request to txt file
	
# Iterate over vendors - maybe unnecessary at this high level
For vendor in vendor_list:  
	For item in inventory: 
		Calculate usage # On current warehouse
		If above threshold:
			# Maybe not necessary, could remove to save space in memory
			high_movement_list.append(item) 
		If below threshold:
			# Add item to list for further analysis
			low_movement_list.append(item) 
			continue

	For item in low_movement_list:
		For warehouse in branches:
			Calculate usage
			If above threshold: 
				# Add to list of items to transfer
				suggested_transfers.append(item) 
			If below threshold:
				# Add to list of items to get RMAs for
				suggested_rma.append(item) 
				
	For item in suggested_rma:
		# Iterate over receipts from newest to oldest until total among those receipts is greater than qty on hand
		# Return the PO number, date, item, qty received, and extended cost
		
				
				