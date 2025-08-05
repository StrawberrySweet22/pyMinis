import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

def sin(theta):
	return np.sin(theta)

def cos(theta):
	return np.cos(theta)

class Line:
	def __init__(self, slope, point = False, intercept = False):
		self._slope = slope
		self._point = point
		self._intercept = intercept
		try:
			self.is_valid_line()
		except:
			print("Not Enough Data To Construct a Line")
			raise
		self.set_intercept()
		self.set_pont()

	def is_valid_line(self):
		if(not(self._point) and not(self._intercept)):
			raise NameError('LineError')
		if(self.is_vertical()):
			if(not(point)):
				raise ('LineError')

	def is_vertical(self):
		if(slope == 'inf'):
			return True
		else:
			return False

	def set_intercept(self):                
		if(self._intercept):
			self._intercept = self.intercept
		else
			if(self.is_vertical()):
				self._intercept = 'dne'
			else:		
				self._intercept = self._point[1]-self._slope*self._point[0]

	def calc_x(self, x):
		if(self.is_vertical()):
			if(x == self._pont[0]):
				return x
			else:
				raise('CalcError')
		else:
			return (self._slope*x+self._intercept)

	def calc_intersection(self, line):
		if(self.is_vertical() and line.is_vertical):
			if(self._point[0] != line._pont[0])
				raise('CalcError')
			else:
				return line._point
		elif(self.is_vertical()):
			x = line.calc_x(self._point[0])
		else:
			return

class LineSegment:
	def __init__(self, slope = False, line = False, point = False, intercept = False, domain = False, reference_lines = False):
		self.line = line
		self.domain = domain
		try:
			self.is_valid_line_segment(reference_lines)
		except:
			print("Not Enough Data To Construct a Line Segment")
			raise
		self.set_line(slope, point, intercept)
		self.set_domain(reference_lines)

	def is_valid_line_segment(self, reference_lines):
		if((not(self.line) and not(self.slope and (self.point or self.intercept))) or (not(self.domain) and not(reference_lines))):
			raise NameError('LineError')

	def set_line(self, slope, point, intercept):
		if(not(self.line)):
			self.line = Line(slope, point, intercept)
		else:
			return

	def set_domain(self, reference_lines):
		if(not(self.domain)):
			slope = self.line.slope
			intercept = self.line.intercept
			slope_1 = reference_lines[0].slope
			slope_2 = reference_lines[1].slope
			intercept_1 = reference_lines[0].intercept
			intercept_2 = reference_lines[1].intercept
			x_1 = (intercept_1-intercept)/(slope-slope_1)
			x_2 = (intercept_2-intercept)/(slope-slope_2)
			if x_1 > x_2:
				self.domain = [x_2, x_1]
			else:
				self.domain = [x_1, x_2]
		else:
			return

class NGram:
	def __init__(self, side_size, rotation, center, sides):
		self.side_size = side_size
		self.sides = sides
		self.rotation = rotation
		self.center = center
		self.hex_verts = []
		self.interior_angles = 0
		self.line_segments = []

		self.set_interior_angles()
		self.set_hex_verts()
		self.set_line_segments()

	def set_interior_angles(self):
		self.interior_angles = (self.sides-2)*pi/self.sides

	def set_hex_verts(self):
		size = self.side_size
		sides = self.sides
		rotation = self.rotation
		delta_theta = self.get_delta_theta()
		offset = self.center
		first_vertex = self.get_first_vertex()
		if rotation != 0:
			v_x = first_vertex[0]
			v_y = first_vertex[1]
			rot_x = v_x*cos(rotation) - v_y*sin(rotation)
			rot_y = v_x*sin(rotation) + v_y*sin(rotation)
			first_vertex[0] = rot_x  
			first_vertex[1] = rot_y
		
		hex_verts = [first_vertex]
		for i in range(sides-1):
			v_y = np.round(size*sin(i*delta_theta+rotation)+hex_verts[i][1], 4)
			v_x = np.round(size*cos(i*delta_theta+rotation)+hex_verts[i][0], 4)
			hex_verts.append([v_x,v_y])
		self.hex_verts = hex_verts

	def set_line_segments(self):
		lines = self.get_lines()
		line_segments = []
		for i in range(self.sides):
			ref_lines = [lines[(self.sides+i-2)%self.sides], lines[(i+2)%self.sides]]
			line_segments.append(LineSegment(False, lines[i], False, False, False, ref_lines))
		self.line_segments = line_segments

	def get_slopes(self):
		slopes=[]
		for i in range(self.sides):
			x_1 = self.hex_verts[i][0]
			x_2 = self.hex_verts[(i+1)%self.sides][0]
			y_1 = self.hex_verts[i][1]
			y_2 = self.hex_verts[(i+1)%self.sides][1]
			if(x_1 == x_2):
				slopes.append('inf')
			else:
				slope = np.round((y_1-y_2)/(x_1-x_2), 4)
				slopes.append(slope)
		return slopes

	def get_lines(self):
		slopes = self.get_slopes()
		lines = []
		for i in range(self.sides):
			lines.append(Line(slopes[i], self.hex_verts[i]))
		return lines


	def get_delta_theta(self):
		return (pi-self.interior_angles)

	def get_first_vertex(self):
		first_x = self.center[0]-(self.side_size/2)
		first_y = self.center[1]-self.side_size*np.tan(self.interior_angles/2)/2
		return[first_x,first_y]


def print_line_segment(line_segment):
	x_list = []
	y_list = []
	x_min = line_segment.domain[0]
	x_max = line_segment.domain[1]

	num_of_posts = 1000
	size_of_posts = (x_max-x_min)/1000

	for i in range(1000):
		x = x_min+i*size_of_posts
		y = line_segment.line.calc_x(x)
		x_list.append(x)
		y_list.append(y)

	plt.plot(x_list, y_list)

def main():
	test_hex = NGram(3, pi, [0,0], 5)
	for i in range(5):
		print_line_segment(test_hex.line_segments[i])
	
	plt.show()

if __name__ == "__main__":
	main()
