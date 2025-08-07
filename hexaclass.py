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
		self.set_point()

	def is_valid_line(self):
		if(not(self._point) and not(self._intercept)):
			raise NameError('LineError')
		if(self.is_vertical()):
			if(not(self._point)):
				raise ('LineError')

	def is_vertical(self):
		if(self._slope == 'inf'):
			return True
		else:
			return False

	def set_intercept(self):                
		if(self._intercept):
			self._intercept = self._intercept
		else:
			print(self._point)
			if(self.is_vertical()):
				self._intercept = 'dne'
			else:		
				self._intercept = self._point[1]-self._slope*self._point[0]


	def set_point(self):
		if(self._point):
			if(self._slope != 'inf'):
				self._point = [0, self._intercept]
			else:
				self._point = [self._point[0], 0]

	def get_slope(self):
		return self._slope

	def get_intercept(self):
		return self._intercept
	def get_point(self):
		return self._point
	def calc_x(self, x):
		if(self.is_vertical()):
			if(x == self._point[0]):
				return x
			else:
				raise('CalcError')
		else:
			return (self._slope*x+self._intercept)

	def calc_intersection(self, line):
		if(self.is_vertical() and line.is_vertical()):
			if(self._point[0] != line._point[0]):
				raise('CalcError')
			else:
				return line._point
		elif(self.is_vertical()):
			return([self._point[0], line.calc_x(self._point[0])])
		elif(line.is_vertical()):
			return([line._point[0], self.calc_x(line._point[0])])
		else:
			x = (self._intercept-line._intercept)/(line._slope-self._slope)
			y = self.calc_x(x)
			return [x,y]

class LineSegment:
	def __init__(self, slope = False, line = False, point = False, intercept = False, domain = False, reference_lines = False, seg_range = False):
		self.line = line
		self.domain = domain
		self.seg_range = seg_range

		try:
			self.is_valid_line_segment(reference_lines)
		except:
			print("Not Enough Data To Construct a Line Segment")
			raise
		self.set_line(slope, point, intercept)
		self.set_domain_range(reference_lines)

	def is_valid_line_segment(self, reference_lines):
		if((not(self.line) and not(self.slope and (self.point or self.intercept))) or (not(self.domain) and not(reference_lines))):
			raise NameError('LineError')

	def is_vertical(self):
		return self.line.is_vertical()

	def set_line(self, slope, point, intercept):
		if(not(self.line)):
			self.line = Line(slope, point, intercept)
		else:
			return

	def set_domain_range(self, reference_lines):
		if(not(self.domain)):
			p_1 = self.line.calc_intersection(reference_lines[0])
			p_2 = self.line.calc_intersection(reference_lines[1])
			if(p_1[0] > p_2[0]):
				self.domain = [p_2[0], p_1[0]]
			else:
				self.domain = [p_1[0], p_2[0]]
			if(p_1[1] > p_2[1]):
				self.seg_range = [p_2[1], p_1[1]]
			else:
				self.seg_range = [p_1[1], p_2[1]]

	def print_line_segment(self, num_posts = False):
		plot = []
		if(num_posts == False):
			num_posts = 1000
		plot.append(self.print_x(num_posts))
		plot.append(self.print_y(num_posts, plot[0]))
		return plot

	def print_x(self, num_posts):
		plot_x = []
		post_size = (self.domain[1]-self.domain[0])/num_posts
		if(self.is_vertical()):
			for i in range(num_posts):
				plot_x.append(self.line.get_point()[0])
		else:
			for i in range(num_posts):
				x = self.domain[0] + post_size*i
				plot_x.append(x)
		return plot_x

	def print_y(self, num_posts, x_values):
		plot_y = []
		post_size = (self.seg_range[1]-self.seg_range[0])/num_posts
		for i in range(num_posts):
			y = self.seg_range[0]+post_size*i
			plot_y.append(y)
		if(self.line.get_slope() != 'inf' and self.line.get_slope() < 0):
			plot_y.reverse()
		return plot_y
		

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
		delta_theta = self._get_delta_theta()
		offset = self.center
		first_vertex = self._get_first_vertex()
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
		lines = self._get_lines()
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

	def _get_lines(self):
		slopes = self.get_slopes()
		lines = []
		for i in range(self.sides):
			lines.append(Line(slopes[i], self.hex_verts[i]))
		return lines

 
	def _get_delta_theta(self):
		return (pi-self.interior_angles)

	def _get_first_vertex(self):
		first_x = self.center[0]-(self.side_size/2)
		first_y = self.center[1]-self.side_size*np.tan(self.interior_angles/2)/2
		return[np.round(first_x, 4),first_y]

	def print_ngram(self, num_posts = 1000):
		ngram_plot = []
		for i in range(self.sides):
			seg_plot = self.line_segments[i].print_line_segment(num_posts)
			ngram_plot.append(seg_plot)
		return ngram_plot

def main():
	test_hex = NGram(3, 0, [0,0], 16)
	ngram_plot = test_hex.print_ngram()
	for i in range(16):
		plt.plot(ngram_plot[i][0], ngram_plot[i][1])
	plt.show()

if __name__ == "__main__":
	main()
