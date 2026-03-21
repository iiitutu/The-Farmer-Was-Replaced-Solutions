# ======================
# multi drone
# ======================
def farm_one_column():
	size = get_world_size()
	for _ in range(size):
		harvest()
		move(North)

def farm_grass_multi_drone():
	size = get_world_size()
	active_drones = [] 
	
	for _ in range(size):
		if num_drones() < max_drones():
			drone_id = spawn_drone(farm_one_column)
			active_drones.append(drone_id)
		else:
			farm_one_column()
			
			for d in active_drones:
				wait_for(d)
			active_drones = []
		move(East)
		
	for d in active_drones:
		wait_for(d)

while True:
	farm_grass_multi_drone()


# ======================
# single drone
# ======================
def farm_grass_single_drone():
  for i in range(get_world_size()):
    for _ in range(get_world_size()):
      harvest()
      move(North)
    move(East)
