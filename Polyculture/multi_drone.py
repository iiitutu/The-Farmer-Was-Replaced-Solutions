def goto(x, y):
	while get_pos_x() != x:
		move(East)
	while get_pos_y() != y:
		move(North)

# sub drone task
def get_nanny_worker(start_x):
	def worker():
		goto(start_x, 0)
		
		while True:
			# job 1: till
			if get_ground_type() != Grounds.Soil:
				till()
				
			# job 2: add water
      if get_water() < 0.8:
				if num_items(Items.Water) == 0: 
					trade(Items.Water)
				use_item(Items.Water)
				
			# patrol route
			move(North)
			if get_pos_y() == 0: 
				move(East)
	return worker

# main drone task
def polyculture_master(main_crop):
	chain = []
	goto(0, 0)
	
  # security
  if get_ground_type() != Grounds.Soil:
		till()
		
	plant(main_crop)
	chain.append([get_pos_x(), get_pos_y()])
	
	# Phase 1
	while True:
		comp = get_companion()
		if comp == None:
			break
			
		c_type, (c_x, c_y) = comp
		
		# check conflict
		is_conflict = False
		for pos in chain:
			if pos[0] == c_x and pos[1] == c_y:
				is_conflict = True
				break
				
		if is_conflict:
			curr_type = get_entity_type()
			harvest()
			plant(curr_type)
			continue 
			
		goto(c_x, c_y)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(c_type)
		chain.append([c_x, c_y])

	# Phase 2
	for pos in chain:
		goto(pos[0], pos[1])
		
		while not can_harvest():
			pass
			
		harvest()

# Coordination center
def mega_polyculture():
	size = get_world_size()
	
	nanny_count = max_drones() - 1 
	if nanny_count < 1:
		nanny_count = 1
	
	spacing = size // nanny_count
	if spacing < 1:
		spacing = 1
	
	for i in range(nanny_count):
		start_x = (i * spacing) % size
		spawn_drone(get_nanny_worker(start_x))
		
	while True:
		polyculture_master(Entities.Grass)

mega_polyculture()
