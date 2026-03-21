# main drone
def run_workers_in_batches(worker_func_factory):
	size = get_world_size()
	limit = max_drones() 
	if limit < 1:
		limit = 1
	
	any_action_taken = False

	for start in range(0, size, limit):
		drones = []
		end = start + limit
		if end > size:
			end = size

		for i in range(start, end - 1):
			drones.append(spawn_drone(worker_func_factory(i)))
			
		master_task_index = end - 1
		master_result = worker_func_factory(master_task_index)()
		
		if master_result == True:
			any_action_taken = True
			
		for d in drones:
			if wait_for(d) == True:
				any_action_taken = True
				
	return any_action_taken

# sub drone plant row
def get_plant_worker(x):
	def worker():
		while get_pos_x() > x:
			move(West)
		while get_pos_x() < x:
			move(East)
		while get_pos_y() > 0:
			move(South)
		
		size = get_world_size()
		for _ in range(size):
			if get_ground_type() != Grounds.Soil: 
				till()
			if get_entity_type() != Entities.Cactus:
				harvest() 
				plant(Entities.Cactus)
			move(North)
			
		return False 
	return worker

# sub drone sort row
def get_col_worker(x):
	def worker():
		while get_pos_x() > x:
			move(West)
		while get_pos_x() < x:
			move(East)
		while get_pos_y() > 0:
			move(South)
		
		size = get_world_size()
		swapped = False 
		
		while get_pos_y() < size - 1:
			if measure() > measure(North):
				swap(North)
				swapped = True
				if get_pos_y() > 0:
					move(South)
				else:
					move(North)
			else:
				move(North)
		return swapped 
	return worker

# sub drone sort line
def get_row_worker(y):
	def worker():
		while get_pos_y() > y:
			move(South)
		while get_pos_y() < y:
			move(North)
		while get_pos_x() > 0:
			move(West)
		
		size = get_world_size()
		swapped = False
		
		while get_pos_x() < size - 1:
			if measure() > measure(East):
				swap(East)
				swapped = True
				if get_pos_x() > 0:
					move(West)
				else:
					move(East)
			else:
				move(East)
		return swapped
	return worker

# main
def cactus_farm():
	while True:
		run_workers_in_batches(get_plant_worker)
    
		is_sorted = False
		while not is_sorted:
			col_swaps = run_workers_in_batches(get_col_worker)
			row_swaps = run_workers_in_batches(get_row_worker)
			
			if not col_swaps and not row_swaps:
				is_sorted = True
				
		harvest()

cactus_farm()
mega_cactus_farm()
