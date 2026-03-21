def sort_cactus():
	size = get_world_size()

	# make sure map is filled with cactus
	for i in range(size * size):
		if get_entity_type() != Entities.Cactus:
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
		move(North)
		if get_pos_y() == 0:
			move(East)

	# Gnome Sort
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		
		for x in range(size):
			while get_pos_x() != x:
				move(East)
			while get_pos_y() != 0:
				move(South)
				
			while get_pos_y() < size - 1:
				if measure() > measure(North):
					swap(North)
					if get_pos_y() > 0:
						move(South)
					else:
						move(North)
				else:
					move(North)
					
		for y in range(size):
			while get_pos_y() != y:
				move(North)
			while get_pos_x() != 0:
				move(West)
				
			while get_pos_x() < size - 1:
				if measure() > measure(East):
					swap(East)
					if get_pos_x() > 0:
						move(West)
					else:
						move(East)
				else:
					move(East)
					
	harvest()

sort_cactus()
	sort_cactus_master()
