
def safe_move(direction):
	if not move(direction):
		change_hat(Hats.Straw_Hat)
		change_hat(Hats.Dinosaur_Hat)
		move(direction)

def farm_bone():
	size = get_world_size()
	
  cols = size
	if cols % 2 != 0:
		cols -= 1
    
		while get_pos_x() < size - 1:
			move(East)
      
		for _ in range(size):
			plant(Entities.Bush)
			move(North)

	while get_pos_x() > 0: 
		move(West)
	while get_pos_y() > 0: 
		move(South)

	change_hat(Hats.Dinosaur_Hat)
	
	while True:
		for x in range(cols):
			if x % 2 == 0:
				while get_pos_y() < size - 1:
					safe_move(North)
			else:
				while get_pos_y() > 1:
					safe_move(South)
			
			if x < cols - 1:
				safe_move(East)

		safe_move(South)
		
		while get_pos_x() > 0:
			safe_move(West)

farm_bone()
