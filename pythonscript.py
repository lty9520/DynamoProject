import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('DSCoreNodes')
from DSCore import *

#输入参数列表
input = IN
#first
centerPoint = input[0]
b1_01 = input[1]
h1_01 = input[2]#1
b_01 = input[3]
b2_01 = input[4]
h_01 = input[5]
h2_01 = input[6]
m = input[7]
b_02 = input[8]
b1_02 = input[9]
h1_02 = input[10]
h_02 = input[11]
#second
b_07 = input[12]
b1_04 = input[13]
b2_04 = input[14]
h_04 = input[15]
h2_04 = input[16]
h2_05 = input[17]
h1_04 = input[18]
b_04 = input[19]
b_06 = input[20]
b1_06 = input[21]
h1_06 = input[22]
h_06 = input[23]
b2_08 = input[24]
b_08 = input[25]
#third
t_08 = b2_04
b_10 = input[26]
b1_10 = b2_04
h1_10 = input[27]
h_09 = input[28]
h_10 = h_09
b_11 = input[29]
b2_12 = input[30]
b_12 = input[31]
h_12 = h_09
t_09 = b2_04
b_09 = input[32]
#fourth
h_13 = input[33]
w_13 = b2_04
l_13 = input[34]
w_14 = b2_04
l_14 = input[35]
b1_15 = input[36]
t_15 = b2_04
b_15 = input[37]
h_15 = h_13
h_16 = input[38]
r_16 = input[39]


########################class Util########################

class Util:

############createQuadCenter############
	#创建四边形面
	#p->面的中心点
	#r->面的边长
	#z->面的位置z值
	def createQuadCenter(self, p, r):

		#	.p1----.p2
		#	|		|
		#	|	p	|
		#	|		|
		#	|		|
		#	.p4----.p3
		x1 = p.X - r
		y1 = p.Y - r
		z1 = p.Z
	
		#test=p.X
	
		x2 = p.X + r
		y2 = p.Y - r
		z2 = p.Z
	
		x3 = p.X + r
		y3 = p.Y + r
		z3 = p.Z
	
		x4 = p.X - r
		y4 = p.Y + r
		z4 = p.Z
	
		p1 = Point.ByCoordinates(x1, y1, z1)
		p2 = Point.ByCoordinates(x2, y2, z2)
		p3 = Point.ByCoordinates(x3, y3, z3)
		p4 = Point.ByCoordinates(x4, y4, z4)
	
		poly = Polygon.ByPoints({p1, p2, p3, p4})
	
		#l1 = List.FirstItem(p1)
		#l1 = List.AddItemToEnd(p2)
		#l1 = List.AddItemToEnd(p3)
		#l1 = List.AddItemToEnd(p4)
	
		#sur = Surface.ByPatch(ploy)
	
		return poly

############createQuadCenter End############

############createTrape############
	#创建梯形平面
	#p->短边中心点
	#d1->短边边长
	#d2->长边边长
	#h->高
	#d->倾斜进深
	#direc->倾斜方向
	def createTrape(self, p, d1, d2, h, d, direc):
	
		x1 = 0
		x2 = 0
		x3 = 0
		x4 = 0
		y1 = 0
		y2 = 0
		y3 = 0
		y4 = 0
		z1 = 0
		z2 = 0
		z3 = 0
		z4 = 0
		
		
		if(direc == "y-"):
		
			x1 = p.X - d1 / 2
			y1 = p.Y
			z1 = p.Z
	
			x2 = p.X + d1 / 2
			y2 = p.Y
			z2 = p.Z
	
			x3 = p.X + d2 / 2
			y3 = p.Y - d
			z3 = p.Z + h
	
			x4 = p.X - d2 / 2
			y4 = p.Y - d
			z4 = p.Z + h
		
	
		if(direc == "y+"):
		
			x1 = p.X - d1 / 2
			y1 = p.Y
			z1 = p.Z
	
			x2 = p.X + d1 / 2
			y2 = p.Y
			z2 = p.Z
	
			x3 = p.X + d2 / 2
			y3 = p.Y + d
			z3 = p.Z + h
	
			x4 = p.X - d2 / 2
			y4 = p.Y + d
			z4 = p.Z + h
		
	
		if(direc == "x-"):
		
			x1 = p.X
			y1 = p.Y - d1 / 2
			z1 = p.Z
	
			x2 = p.X
			y2 = p.Y+ d1 / 2
			z2 = p.Z
	
			x3 = p.X - d
			y3 = p.Y + d2 / 2
			z3 = p.Z + h
	
			x4 = p.X - d
			y4 = p.Y - d2 / 2
			z4 = p.Z + h
		
	
		if(direc == "x+"):
		
			x1 = p.X
			y1 = p.Y- d1 / 2
			z1 = p.Z
	
			x2 = p.X
			y2 = p.Y+ d1 / 2
			z2 = p.Z
	
			x3 = p.X + d
			y3 = p.Y + d2 / 2
			z3 = p.Z + h
	
			x4 = p.X + d
			y4 = p.Y - d2 / 2
			z4 = p.Z + h
			
	
	
		p1 = Point.ByCoordinates(x1, y1, z1)
		p2 = Point.ByCoordinates(x2, y2, z2)
		p3 = Point.ByCoordinates(x3, y3, z3)
		p4 = Point.ByCoordinates(x4, y4, z4)
	
		poly = Polygon.ByPoints({p1, p2, p3, p4})
	
		return poly

############createTrape End############

############createUPlane############

	#创建栌枓U型侧面
	#p->底边中心定位点
	#w->长边长
	#w1->顶部短边长
	#h1->高（h - h1)
	#h2->中间U型部分高
	#direc->绘制方向
	def createUPlane(self, p, w, w1, h1, h2, direc):
	
		x1 =0
		y1 =0
		z1 =0
		x2 =0
		y2 =0
		z2 =0
		x3 =0
		y3 =0
		z3 =0
		x4 =0
		y4 =0
		z4 =0
		x5 =0
		y5 =0
		z5 =0
		x6 =0
		y6 =0
		z6 =0
		x7 =0
		y7 =0
		z7 =0
		x8 =0
		y8 =0
		z8 =0
	
		
	
		if(direc == "x"):
		
			x1 = p.X - w / 2
			y1 = p.Y
			z1 = p.Z
	
			x2 = p.X + w / 2
			y2 = p.Y
			z2 = p.Z
	
			x3 = p.X + w / 2
			y3 = p.Y
			z3 = p.Z + h1
	
			x4 = p.X + w1 / 2
			y4 = p.Y
			z4 = p.Z + h1
	
			x5 = p.X + w1 / 2
			y5 = p.Y
			z5 = p.Z + h1 - h2
	
			x6 = p.X - w1 / 2
			y6 = p.Y
			z6 = p.Z + h1 - h2
	
			x7 = p.X - w1 / 2
			y7 = p.Y
			z7 = p.Z + h1
	
			x8 = p.X - w / 2
			y8 = p.Y
			z8 = p.Z + h1
		
	
		if(direc == "y"):
		
			x1 = p.X
			y1 = p.Y - w / 2
			z1 = p.Z
	
			x2 = p.X
			y2 = p.Y + w / 2
			z2 = p.Z
	
			x3 = p.X
			y3 = p.Y + w / 2
			z3 = p.Z + h1
	
			x4 = p.X
			y4 = p.Y + w1 / 2
			z4 = p.Z + h1
	
			x5 = p.X
			y5 = p.Y + w1 / 2
			z5 = p.Z + h1 - h2
	
			x6 = p.X
			y6 = p.Y - w1 / 2
			z6 = p.Z + h1 - h2
	
			x7 = p.X
			y7 = p.Y - w1 / 2
			z7 = p.Z + h1
	
			x8 = p.X
			y8 = p.Y - w / 2
			z8 = p.Z + h1
		
	
		
	
		p1 = Point.ByCoordinates(x1, y1, z1)
		p2 = Point.ByCoordinates(x2, y2, z2)
		p3 = Point.ByCoordinates(x3, y3, z3)
		p4 = Point.ByCoordinates(x4, y4, z4)
		p5 = Point.ByCoordinates(x5, y5, z5)
		p6 = Point.ByCoordinates(x6, y6, z6)
		p7 = Point.ByCoordinates(x7, y7, z7)
		p8 = Point.ByCoordinates(x8, y8, z8)
	
		poly = Polygon.ByPoints([p1, p2, p3, p4, p5, p6, p7, p8])
	
		return poly

############createUPlane End############

############createJuanshaCurve############
	#创建卷杀曲线
	#p->定位点
	#b1->卷杀部分长
	#b2->其余部分长
	#m->卷杀段数
	#h1->卷杀部分高
	#h->整体高
	#direc->方向
	def createJuanshaCurve(self, p, b1, b2, m, h1, h, direc):
	
		x1 = 0
		y1 = 0
		z1 = 0
		x2 = 0
		y2 = 0
		z2 = 0
		x3 = 0
		y3 = 0
		z3 = 0
		x4 = 0
		y4 = 0
		z4 = 0
		x5 = 0
		y5 = 0
		z5 = 0
		x6 = 0
		y6 = 0
		z6 = 0
		x7 = 0
		y7 = 0
		z7 = 0
		x8 = 0
		y8 = 0
		z8 = 0
		
	
		if(direc == "x+"):
		
			x1 = p.X
			y1 = p.Y
			z1 = p.Z
	
			x2 = p.X + b2
			y2 = p.Y
			z2 = p.Z
	
			x3 = p.X + b2 + ((4.0 / 10.0) * b1)
			y3 = p.Y
			z3 = p.Z + ((1.0 / 10.0) * h1)
	
			x4 = p.X + b2 + ((7.0 / 10.0) * b1)
			y4 = p.Y
			z4 = p.Z + ((3.0 / 10.0) * h1)
	
			x5 = p.X + b2 + ((9.0 / 10.0) * b1)
			y5 = p.Y
			z5 = p.Z + ((6.0 / 10.0) * h1)
	
			x6 = p.X + b2 + b1
			y6 = p.Y
			z6 = p.Z + h1
	
			x7 = p.X + b2 + b1
			y7 = p.Y
			z7 = p.Z + h
	
			x8 = p.X
			y8 = p.Y
			z8 = p.Z + h
		
	
		if(direc == "x-"):
		
			x1 = p.X
			y1 = p.Y
			z1 = p.Z
	
			x2 = p.X - b2
			y2 = p.Y
			z2 = p.Z
	
			x3 = p.X - b2 - ((4.0 / 10.0) * b1)
			y3 = p.Y
			z3 = p.Z + ((1.0 / 10.0) * h1)
	
			x4 = p.X - b2 - ((7.0 / 10.0) * b1)
			y4 = p.Y
			z4 = p.Z + ((3.0 / 10.0) * h1)
	
			x5 = p.X - b2 - ((9.0 / 10.0) * b1)
			y5 = p.Y
			z5 = p.Z + ((6.0 / 10.0) * h1)
	
			x6 = p.X - b2 - b1
			y6 = p.Y
			z6 = p.Z + h1
	
			x7 = p.X - b2 - b1
			y7 = p.Y
			z7 = p.Z + h
	
			x8 = p.X
			y8 = p.Y
			z8 = p.Z + h
		
	
		if(direc == "y+"):
		
			x1 = p.X
			y1 = p.Y
			z1 = p.Z
	
			x2 = p.X
			y2 = p.Y + b2
			z2 = p.Z
	
			x3 = p.X
			y3 = p.Y + b2 + ((4.0 / 10.0) * b1)
			z3 = p.Z + ((1.0 / 10.0) * h1)
	
			x4 = p.X
			y4 = p.Y + b2 + ((7.0 / 10.0) * b1)
			z4 = p.Z + ((3.0 / 10.0) * h1)
	
			x5 = p.X
			y5 = p.Y + b2 + ((9.0 / 10.0) * b1)
			z5 = p.Z + ((6.0 / 10.0) * h1)
	
			x6 = p.X
			y6 = p.Y + b2 + b1
			z6 = p.Z + h1
	
			x7 = p.X
			y7 = p.Y + b2 + b1
			z7 = p.Z + h
	
			x8 = p.X
			y8 = p.Y
			z8 = p.Z + h
		
	
		if(direc == "y-"):
		
			x1 = p.X
			y1 = p.Y
			z1 = p.Z
	
			x2 = p.X
			y2 = p.Y - b2
			z2 = p.Z
	
			x3 = p.X
			y3 = p.Y - b2 - ((4.0 / 10.0) * b1)
			z3 = p.Z + ((1.0 / 10.0) * h1)
	
			x4 = p.X
			y4 = p.Y - b2 - ((7.0 / 10.0) * b1)
			z4 = p.Z + ((3.0 / 10.0) * h1)
	
			x5 = p.X
			y5 = p.Y - b2 - ((9.0 / 10.0) * b1)
			z5 = p.Z + ((6.0 / 10.0) * h1)
	
			x6 = p.X
			y6 = p.Y - b2 - b1
			z6 = p.Z + h1
	
			x7 = p.X
			y7 = p.Y - b2 - b1
			z7 = p.Z + h
	
			x8 = p.X
			y8 = p.Y
			z8 = p.Z + h
		
	
	
		p1 = Point.ByCoordinates(x1, y1, z1)
		p2 = Point.ByCoordinates(x2, y2, z2)
		p3 = Point.ByCoordinates(x3, y3, z3)
		p4 = Point.ByCoordinates(x4, y4, z4)
		p5 = Point.ByCoordinates(x5, y5, z5)
		p6 = Point.ByCoordinates(x6, y6, z6)
		p7 = Point.ByCoordinates(x7, y7, z7)
		p8 = Point.ByCoordinates(x8, y8, z8)
	
		poly = Polygon.ByPoints([p1, p2, p3, p4, p5, p6, p7, p8])
	
		curve = PolyCurve.ByPoints([p1, p2, p3, p4, p5, p6, p7, p8], True)
	
		return curve

############createJuanshaCurve End############

############createCubiod############
	#创建单卷杀长方体栱部分，
	#cur->边界曲线
	#width->长方体长度
	#direction->延伸方向
	def createCubiod(self, cur, width, direction):
	
		x1 = 0
		y1 = 0
		z1 = 0
		x2 = 0
		y2 = 0
		z2 = 0
	
		
		
		if(direction == "x+"):
		
			x1 = cur.StartPoint.X + width
			y1 = cur.StartPoint.Y
			z1 = cur.StartPoint.Z
	
			x2 = cur.EndPoint.X + width
			y2 = cur.EndPoint.Y
			z2 = cur.EndPoint.Z
		
	
		if(direction == "x-"):
		
			x1 = cur.StartPoint.X - width
			y1 = cur.StartPoint.Y
			z1 = cur.StartPoint.Z
	
			x2 = cur.EndPoint.X - width
			y2 = cur.EndPoint.Y
			z2 = cur.EndPoint.Z
		
	
		if(direction == "y+"):
		
			x1 = cur.StartPoint.X
			y1 = cur.StartPoint.Y + width
			z1 = cur.StartPoint.Z
	
			x2 = cur.EndPoint.X
			y2 = cur.EndPoint.Y + width
			z2 = cur.EndPoint.Z
		
	
		if(direction == "y-"):
		
			x1 = cur.StartPoint.X
			y1 = cur.StartPoint.Y - width
			z1 = cur.StartPoint.Z
	
			x2 = cur.EndPoint.X
			y2 = cur.EndPoint.Y - width
			z2 = cur.EndPoint.Z
		
		
	
		p1 = Point.ByCoordinates(x1, y1, z1)
		p2 = Point.ByCoordinates(x2, y2, z2)
	
		curve = PolyCurve.ByPoints({p1, p2}, False)
	
		return curve
	
############createCubiod End############

############getNDGFangCenterPoint############
	#获取创建枋类构件的中心点
	#p_center->与坊正交的栱的长方体部分的质心
	#p_down->栌枓的内角点
	#dh->与坊正交的栱的高的一半
	def getNDGFangCenterPoint(self, p_center, p_down, dh):
	
		x1 = 0
		y1 = 0
		z1 = p_down.Z + (p_center.Z + dh - p_down.Z) / 2
	
		p1 = Point.ByCoordinates(x1, y1, z1)
	
		return p1

############getNDGFangCenterPoint End############

############getHGFang############
	#获取创建枋类构件的中心点
	#p_center->与坊正交的栱的长方体部分的质心
	#p_down->栌枓的内角点
	#dh->与坊正交的栱的高的一半
	def getHGFang(self, p, db, w, l, h):
	
		x1 = p.X + db - l / 2
		y1 = p.Y - w / 2
		z1 = p.Z + h / 2
	
		p1 = Point.ByCoordinates(x1, y1, z1)
	
		cube = Cuboid.ByLengths(p1, l, w, h)
	
		return cube

############getHGFang End############

############getMidPoint############
	#获取整体枋类中心点
	#p1->一端端点(sandou)
	#p2->另一端端点(snadou)
	#h1->散枓h1高
	#dh->散枓槽口到斜边高
	#h->枋高
	#
	def getMidPoint(self, p1, p2, h1, dh, h):
	
		x1 = (p1.X + p2.X) / 2
		y1 = (p1.Y + p2.Y) / 2
		z1 = p1.Z + h1 + dh + h / 2
	
		p_mid = Point.ByCoordinates(x1, y1, z1)
	
		return p_mid

############getMidPoint End############

########################class Util End########################

########################class ExtendUtil########################

class ExtendUtil:

############createFirst############
	#create first tiao
	
	def createFirst(self, centerPoint, b1_01, h1_01, b_01, b2_01, h_01, h2_01, m, b_02, b1_02, h1_02, h_02):
		utils = Util()
		result = []
		#create quad
		#centerpoint
		p = centerPoint
		#radius
		r = b1_01 / 2
		#create Trape -- d
		T_d = (b_01 - b1_01) / 2
		#create U Plane -- h1
		U_h1 = h_01 - h1_01
		#create JuanSha -- u
		JS_u = h2_01 / U_h1
		#create JuanSha -- v
		JS_v = b2_01 / b_01
		#create JuanSha -- 1 - v
		JS_mv = 1 - (b2_01 / b_01)
		#create JuanSha -- b2
		JS_b2 = ((b_02 - 2 * b1_02) - b_01) / 2
		###bottom quad
		bottomQuad = utils.createQuadCenter(centerPoint, r)
	
		bottomQuadSurface = Surface.ByPatch(bottomQuad)
		#0
		result = List.AddItemToEnd(bottomQuadSurface, result)
		#####create trape
		###trape1
		p_T1 = Surface.PointAtParameter(bottomQuadSurface, 0.5, 0)
	
		direc1 = "y-"
		Trape1 = utils.createTrape(p_T1, b1_01, b_01, h1_01, T_d, direc1)
	
		Trape1_S = Surface.ByPatch(Trape1)
		#1
		result = List.AddItemToEnd(Trape1_S, result)
	
		###trape2
		p_T2 = Surface.PointAtParameter(bottomQuadSurface, 0.5, 1)
	
		direc2 = "y+"
		Trape2 = utils.createTrape(p_T2, b1_01, b_01, h1_01, T_d, direc2)
	
		Trape2_S = Surface.ByPatch(Trape2)
		#2
		result = List.AddItemToEnd(Trape2_S, result)
	
		###trape3
		p_T3 = Surface.PointAtParameter(bottomQuadSurface, 1, 0.5)
	
		direc3 = "x+"
		Trape3 = utils.createTrape(p_T3, b1_01, b_01, h1_01, T_d, direc3)
	
		Trape3_S = Surface.ByPatch(Trape3)
		#3
		result = List.AddItemToEnd(Trape3_S, result)
	
		###trape4
		p_T4 = Surface.PointAtParameter(bottomQuadSurface, 0, 0.5)
	
		direc4 = "x-"
		Trape4 = utils.createTrape(p_T4, b1_01, b_01, h1_01, T_d, direc4)
	
		Trape4_S = Surface.ByPatch(Trape4)
		#4
		result = List.AddItemToEnd(Trape4_S, result)
	
		######create U plane
		###UPlane1
		p_U1 = Surface.PointAtParameter(Trape1_S, 0, 0.5)
	
		direc12 = "x"
		UPlane1 = utils.createUPlane(p_U1, b_01, b2_01, U_h1, h2_01, direc12)
	
		UPlane1_S = Surface.ByPatch(UPlane1)
		#5
		result = List.AddItemToEnd(UPlane1_S, result)
	
		###UPlane2
		p_U2 = Surface.PointAtParameter(Trape2_S, 0, 0.5)
	
	
		UPlane2 = utils.createUPlane(p_U2, b_01, b2_01, U_h1, h2_01, direc12)
	
		UPlane2_S = Surface.ByPatch(UPlane2)
		#6
		result = List.AddItemToEnd(UPlane2_S, result)
	
		###UPlane3
		p_U3 = Surface.PointAtParameter(Trape3_S, 0, 0.5)
	
		direc34 = "y"
		UPlane3 = utils.createUPlane(p_U3, b_01, b2_01, U_h1, h2_01, direc34)
	
		UPlane3_S = Surface.ByPatch(UPlane3)
		#7
		result = List.AddItemToEnd(UPlane3_S, result)
	
		###UPlane4
		p_U4 = Surface.PointAtParameter(Trape4_S, 0, 0.5)
	
	
		UPlane4 = utils.createUPlane(p_U4, b_01, b2_01, U_h1, h2_01, direc34)
	
		UPlane4_S = Surface.ByPatch(UPlane4)
		#8
		result = List.AddItemToEnd(UPlane4_S, result)
	
		#####create JuanSha
		###JS1
		direc1 = "y-"
		##JS1_1
		p_JS1_1 = Surface.PointAtParameter(UPlane1_S, JS_u, JS_v)
	
		JS1_1 = utils.createJuanshaCurve(p_JS1_1, b1_02, JS_b2, m, h1_02, h_02, direc1)
	
		JS1_C1 = Surface.ByPatch(JS1_1)
		#9
		result = List.AddItemToEnd(JS1_C1, result)
	
		##JS1_2
		p_JS1_2 = Surface.PointAtParameter(UPlane1_S, JS_u, JS_mv)
	
		JS1_2 = utils.createJuanshaCurve(p_JS1_2, b1_02, JS_b2, m, h1_02, h_02, direc1)
	
		JS1_C2 = Surface.ByPatch(JS1_2)
		#10
		result = List.AddItemToEnd(JS1_C2, result)
	
		JS1 = []
	
		JS1 = List.AddItemToEnd(JS1_1, JS1)
		JS1 = List.AddItemToEnd(JS1_2, JS1)
		JS1_S = Surface.ByLoft(JS1)
		#11
		result = List.AddItemToEnd(JS1_S, result)
	
		###JS2
		direc2 = "y+"
		##JS2_1
		p_JS2_1 = Surface.PointAtParameter(UPlane2_S, JS_u, JS_v)
	
		JS2_1 = utils.createJuanshaCurve(p_JS2_1, b1_02, JS_b2, m, h1_02, h_02, direc2)
	
		JS2_C1 = Surface.ByPatch(JS2_1)
		#12
		result = List.AddItemToEnd(JS2_C1, result)
	
		##JS2_2
		p_JS2_2 = Surface.PointAtParameter(UPlane2_S, JS_u, JS_mv)
	
		JS2_2 = utils.createJuanshaCurve(p_JS2_2, b1_02, JS_b2, m, h1_02, h_02, direc2)
	
		JS2_C2 = Surface.ByPatch(JS2_2)
		#13
		result = List.AddItemToEnd(JS2_C2, result)
	
		JS2 = []
	
		JS2 = List.AddItemToEnd(JS2_1, JS2)
		JS2 = List.AddItemToEnd(JS2_2, JS2)
		JS2_S = Surface.ByLoft(JS2)
		#14
		result = List.AddItemToEnd(JS2_S, result)
	
		###JS3
		direc3 = "x+"
		##JS3_1
		p_JS3_1 = Surface.PointAtParameter(UPlane3_S, JS_u, JS_v)
	
		JS3_1 = utils.createJuanshaCurve(p_JS3_1, b1_02, JS_b2, m, h1_02, h_02, direc3)
	
		JS3_C1 = Surface.ByPatch(JS3_1)
		#15
		result = List.AddItemToEnd(JS3_C1, result)
	
		##JS3_2
		p_JS3_2 = Surface.PointAtParameter(UPlane3_S, JS_u, JS_mv)
	
		JS3_2 = utils.createJuanshaCurve(p_JS3_2, b1_02, JS_b2, m, h1_02, h_02, direc3)
	
		JS3_C2 = Surface.ByPatch(JS3_2)
		#16
		result = List.AddItemToEnd(JS3_C2, result)
	
		JS3 = []
	
		JS3 = List.AddItemToEnd(JS3_1, JS3)
		JS3 = List.AddItemToEnd(JS3_2, JS3)
		JS3_S = Surface.ByLoft(JS3)
		#17
		result = List.AddItemToEnd(JS3_S, result)
	
		###JS4
		direc4 = "x-"
		##JS4_1
		p_JS4_1 = Surface.PointAtParameter(UPlane4_S, JS_u, JS_v)
	
		JS4_1 = utils.createJuanshaCurve(p_JS4_1, b1_02, JS_b2, m, h1_02, h_02, direc4)
	
		JS4_C1 = Surface.ByPatch(JS4_1)
		#18
		result = List.AddItemToEnd(JS4_C1, result)
	
		##JS4_2
		p_JS4_2 = Surface.PointAtParameter(UPlane4_S, JS_u, JS_mv)
	
		JS4_2 = utils.createJuanshaCurve(p_JS4_2, b1_02, JS_b2, m, h1_02, h_02, direc4)
	
		JS4_C2 = Surface.ByPatch(JS4_2)
		#19
		result = List.AddItemToEnd(JS4_C2, result)
	
		JS4 = []
	
		JS4 = List.AddItemToEnd(JS4_1, JS4)
		JS4 = List.AddItemToEnd(JS4_2, JS4)
		JS4_S = Surface.ByLoft(JS4)
		#20
		result = List.AddItemToEnd(JS4_S, result)
	
		return result
	
############createFirst End############

############createSecond############

	#create second tiao
	
	def createSecond(self, JS1_C1, JS2_C1, JS3_C1, b_07, b2_01, b1_04, b_02, b2_04,
	h_04, h2_04, h2_05, h1_04, b_04, b_06, b1_06, h1_06, h_06, m, b2_08, b_08):

		utils = Util()
		result = []
	
		#create quad translate dx
		Q_d_x = b2_01 / 2
		#create quad translate dy
		Q_d_y = b2_04 / 2
		#create quad -- r
		Q_r = b1_04 / 2
		#create Trape -- d
		T_d = (b_04 - b1_04) / 2
		#create U palne -- h1
		U_h1 = (h_04 - h1_04)
		#create JS -- u
		JS_u = h2_04 / U_h1
		#create JS -- v
		JS_v = (((b_04 - b2_04) / 2) + b2_04) / b_04
		#create JS -- mv
		JS_mv = 1 - ((((b_04 - b2_04) / 2) + b2_04) / b_04)
		#create JS -- b2_12
		JS_b2_12 = ((b_06 - 2 * b1_06) - b_02 - 2 * T_d) / 2
		#create JS -- b2_34
		JS_b2_34 = ((b_07 - 2 * b1_06) - b2_01 - 2 * T_d) / 2
		#create JS -- b2_5
		JS_b2_5 = b2_08 - b1_06 - (b_04 - (((b_04 - b2_04) / 2) + b2_04))
		#create Cuboid -- width
		Cub_w = b_08 - b1_06 - JS_b2_5
		#######JS1
		###create quad
		p_Q1 = Surface.PointAtParameter(JS1_C1, 1.0, 0.0)
	
		p_Q1_trans = Geometry.Translate(p_Q1, Q_d_x, Q_d_y, 0.0)
	
		Quad1 = utils.createQuadCenter(p_Q1_trans, Q_r)
	
		Quad_1S = Surface.ByPatch(Quad1)
	
		result = List.AddItemToEnd(Quad_1S, result)
	
		###JS2
		###create quad
		p_Q2 = Surface.PointAtParameter(JS2_C1, 0.0, 1.0)
	
		p_Q2_trans = Geometry.Translate(p_Q2, Q_d_x, -Q_d_y, 0.0)
	
		Quad2 = utils.createQuadCenter(p_Q2_trans, Q_r)
	
		Quad_2S = Surface.ByPatch(Quad2)
	
		result = List.AddItemToEnd(Quad_2S, result)
	
		###JS3
		###create quad
		p_Q3 = Surface.PointAtParameter(JS3_C1, 0.0, 1.0)
	
		p_Q3_trans = Geometry.Translate(p_Q3, -Q_d_x, Q_d_y, 0.0)
	
		Quad3 = utils.createQuadCenter(p_Q3_trans, Q_r)
	
		Quad_3S = Surface.ByPatch(Quad3)
	
		result = List.AddItemToEnd(Quad_3S, result)
	
		#######JS1
		###create Trape
		#T1
		_1_p_T1 = Surface.PointAtParameter(Quad_1S, 0.5, 0.0)
	
		_1_direc1 = "y-"
		_1_T1 = utils.createTrape(_1_p_T1, b1_04, b_04, h1_04, T_d, _1_direc1)
	
		_1_T1_S = Surface.ByPatch(_1_T1)
	
		result = List.AddItemToEnd(_1_T1_S, result)
	
		#T2
		_1_p_T2 = Surface.PointAtParameter(Quad_1S, 0.5, 1.0)
	
		_1_direc2 = "y+"
		_1_T2 = utils.createTrape(_1_p_T2, b1_04, b_04, h1_04, T_d, _1_direc2)
	
		_1_T2_S = Surface.ByPatch(_1_T2)
	
		result = List.AddItemToEnd(_1_T2_S, result)
	
		#T3
		_1_p_T3 = Surface.PointAtParameter(Quad_1S, 1.0, 0.5)
	
		_1_direc3 = "x+"
		_1_T3 = utils.createTrape(_1_p_T3, b1_04, b_04, h1_04, T_d, _1_direc3)
	
		_1_T3_S = Surface.ByPatch(_1_T3)
	
		result = List.AddItemToEnd(_1_T3_S, result)
	
		#T4
		_1_p_T4 = Surface.PointAtParameter(Quad_1S, 0.0, 0.5)
	
		_1_direc4 = "x-"
		_1_T4 = utils.createTrape(_1_p_T4, b1_04, b_04, h1_04, T_d, _1_direc4)
	
		_1_T4_S = Surface.ByPatch(_1_T4)
	
		result = List.AddItemToEnd(_1_T4_S, result)
	
		#######JS2
		###create Trape
		#T1
		_2_p_T1 = Surface.PointAtParameter(Quad_2S, 0.5, 0.0)
	
		_2_direc1 = "y-"
		_2_T1 = utils.createTrape(_2_p_T1, b1_04, b_04, h1_04, T_d, _2_direc1)
	
		_2_T1_S = Surface.ByPatch(_2_T1)
	
		result = List.AddItemToEnd(_2_T1_S, result)
	
		#T2
		_2_p_T2 = Surface.PointAtParameter(Quad_2S, 0.5, 1.0)
	
		_2_direc2 = "y+"
		_2_T2 = utils.createTrape(_2_p_T2, b1_04, b_04, h1_04, T_d, _2_direc2)
	
		_2_T2_S = Surface.ByPatch(_2_T2)
	
		result = List.AddItemToEnd(_2_T2_S, result)
	
		#T3
		_2_p_T3 = Surface.PointAtParameter(Quad_2S, 1.0, 0.5)
	
		_2_direc3 = "x+"
		_2_T3 = utils.createTrape(_2_p_T3, b1_04, b_04, h1_04, T_d, _2_direc3)
	
		_2_T3_S = Surface.ByPatch(_2_T3)
	
		result = List.AddItemToEnd(_2_T3_S, result)
	
		#T4
		_2_p_T4 = Surface.PointAtParameter(Quad_2S, 0.0, 0.5)
	
		_2_direc4 = "x-"
		_2_T4 = utils.createTrape(_2_p_T4, b1_04, b_04, h1_04, T_d, _2_direc4)
	
		_2_T4_S = Surface.ByPatch(_2_T4)
	
		result = List.AddItemToEnd(_2_T4_S, result)
	
		#######JS3
		###create Trape
		#T1
		_3_p_T1 = Surface.PointAtParameter(Quad_3S, 0.5, 0.0)
	
		_3_direc1 = "y-"
		_3_T1 = utils.createTrape(_3_p_T1, b1_04, b_04, h1_04, T_d, _3_direc1)
	
		_3_T1_S = Surface.ByPatch(_3_T1)
	
		result = List.AddItemToEnd(_3_T1_S, result)
	
		#T2
		_3_p_T2 = Surface.PointAtParameter(Quad_3S, 0.5, 1.0)
	
		_3_direc2 = "y+"
		_3_T2 = utils.createTrape(_3_p_T2, b1_04, b_04, h1_04, T_d, _3_direc2)
	
		_3_T2_S = Surface.ByPatch(_3_T2)
	
		result = List.AddItemToEnd(_3_T2_S, result)
	
		#T3
		_3_p_T3 = Surface.PointAtParameter(Quad_3S, 1.0, 0.5)
	
		_3_direc3 = "x+"
		_3_T3 = utils.createTrape(_3_p_T3, b1_04, b_04, h1_04, T_d, _3_direc3)
	
		_3_T3_S = Surface.ByPatch(_3_T3)
	
		result = List.AddItemToEnd(_3_T3_S, result)
	
		#T4
		_3_p_T4 = Surface.PointAtParameter(Quad_3S, 0.0, 0.5)
	
		_3_direc4 = "x-"
		_3_T4 = utils.createTrape(_3_p_T4, b1_04, b_04, h1_04, T_d, _3_direc4)
	
		_3_T4_S = Surface.ByPatch(_3_T4)
	
		result = List.AddItemToEnd(_3_T4_S, result)
	
		#######JS1
		#######create U plane
		_1_direc12 = "x"
		#U1
		_1_p_U1 = Surface.PointAtParameter(_1_T1_S, 0.5, 0.0)
	
		_1_U1 = utils.createUPlane(_1_p_U1, b_04, b2_04, U_h1, h2_04, _1_direc12)
	
		_1_U1_S = Surface.ByPatch(_1_U1)
	
		result = List.AddItemToEnd(_1_U1_S, result)
	
		#U2
		_1_p_U2 = Surface.PointAtParameter(_1_T2_S, 0.5, 1.0)
	
		_1_U2 = utils.createUPlane(_1_p_U2, b_04, b2_04, U_h1, h2_04, _1_direc12)
	
		_1_U2_S = Surface.ByPatch(_1_U2)
	
		result = List.AddItemToEnd(_1_U2_S, result)
	
		_1_direc34 = "y"
		#U3
		_1_p_U3 = Surface.PointAtParameter(_1_T3_S, 0.0, 0.5)
	
		_1_U3 = utils.createUPlane(_1_p_U3, b_04, b2_04, U_h1, h2_04, _1_direc34)
	
		_1_U3_S = Surface.ByPatch(_1_U3)
	
		result = List.AddItemToEnd(_1_U3_S, result)
	
		#U4
		_1_p_U4 = Surface.PointAtParameter(_1_T4_S, 0.0, 0.5)
	
		_1_U4 = utils.createUPlane(_1_p_U4, b_04, b2_04, U_h1, h2_04, _1_direc34)
	
		_1_U4_S = Surface.ByPatch(_1_U4)
	
		result = List.AddItemToEnd(_1_U4_S, result)
	
		##########JS2
		#######create U plane
		_2_direc12 = "x"
		#U1
		_2_p_U1 = Surface.PointAtParameter(_2_T1_S, 0.5, 0.0)
	
		_2_U1 = utils.createUPlane(_2_p_U1, b_04, b2_04, U_h1, h2_04, _2_direc12)
	
		_2_U1_S = Surface.ByPatch(_2_U1)
	
		result = List.AddItemToEnd(_2_U1_S, result)
	
		#U2
		_2_p_U2 = Surface.PointAtParameter(_2_T2_S, 0.5, 1.0)
	
		_2_U2 = utils.createUPlane(_2_p_U2, b_04, b2_04, U_h1, h2_04, _2_direc12)
	
		_2_U2_S = Surface.ByPatch(_2_U2)
	
		result = List.AddItemToEnd(_2_U2_S, result)
	
		_2_direc34 = "y"
		#U3
		_2_p_U3 = Surface.PointAtParameter(_2_T3_S, 0.0, 0.5)
	
		_2_U3 = utils.createUPlane(_2_p_U3, b_04, b2_04, U_h1, h2_04, _2_direc34)
	
		_2_U3_S = Surface.ByPatch(_2_U3)
	
		result = List.AddItemToEnd(_2_U3_S, result)
	
		#U4
		_2_p_U4 = Surface.PointAtParameter(_2_T4_S, 0.0, 0.5)
	
		_2_U4 = utils.createUPlane(_2_p_U4, b_04, b2_04, U_h1, h2_04, _2_direc34)
	
		_2_U4_S = Surface.ByPatch(_2_U4)
	
		result = List.AddItemToEnd(_2_U4_S, result)
	
		#########JS3
		#######create U plane
		_3_direc12 = "x"
		#U1
		_3_p_U1 = Surface.PointAtParameter(_3_T1_S, 0.5, 0.0)
	
		_3_U1 = utils.createUPlane(_3_p_U1, b_04, b2_04, U_h1, h2_04, _3_direc12)
	
		_3_U1_S = Surface.ByPatch(_3_U1)
	
		result = List.AddItemToEnd(_3_U1_S, result)
	
		#U2
		_3_p_U2 = Surface.PointAtParameter(_3_T2_S, 0.5, 1.0)
	
		_3_U2 = utils.createUPlane(_3_p_U2, b_04, b2_04, U_h1, h2_04, _3_direc12)
	
		_3_U2_S = Surface.ByPatch(_3_U2)
	
		result = List.AddItemToEnd(_3_U2_S, result)
	
		_3_direc34 = "y"
		#U3
		_3_p_U3 = Surface.PointAtParameter(_3_T3_S, 0.0, 0.5)
	
		_3_U3 = utils.createUPlane(_3_p_U3, b_04, b2_04, U_h1, h2_04, _3_direc34)
	
		_3_U3_S = Surface.ByPatch(_3_U3)
	
		result = List.AddItemToEnd(_3_U3_S, result)
	
		#U4
		_3_p_U4 = Surface.PointAtParameter(_3_T4_S, 0.0, 0.5)
	
		_3_U4 = utils.createUPlane(_3_p_U4, b_04, b2_04, U_h1, h2_04, _3_direc34)
	
		_3_U4_S = Surface.ByPatch(_3_U4)
	
		result = List.AddItemToEnd(_3_U4_S, result)
	
		#######_1_JS
		_1_direc = "y-"
		#JS_C1
		_1_JS_C1_p = Surface.PointAtParameter(_1_U1_S, JS_u, JS_v)
	
		_1_JS_C1 = utils.createJuanshaCurve(_1_JS_C1_p, b1_06, JS_b2_12, m, h1_06,
		h_06, _1_direc)
	
		_1_JS_C1_S = Surface.ByPatch(_1_JS_C1)
	
		result = List.AddItemToEnd(_1_JS_C1_S, result)
	
		#JS_C2
		_1_JS_C2_p = Surface.PointAtParameter(_1_U1_S, JS_u, JS_mv)
	
		_1_JS_C2 = utils.createJuanshaCurve(_1_JS_C2_p, b1_06, JS_b2_12, m, h1_06,
		h_06, _1_direc)
	
		_1_JS_C2_S = Surface.ByPatch(_1_JS_C2)
	
		result = List.AddItemToEnd(_1_JS_C2_S, result)
	
		_1_JS = []
		_1_JS = List.AddItemToEnd(_1_JS_C1, _1_JS)
		_1_JS = List.AddItemToEnd(_1_JS_C2, _1_JS)
		_1_JS_S = PolySurface.ByLoft(_1_JS)
	
		result = List.AddItemToEnd(_1_JS_S, result)
	
		#######_2_JS
		_2_direc = "y+"
		#JS_C1
		_2_JS1_C1_p = Surface.PointAtParameter(_2_U2_S, JS_u, JS_v)
	
		_2_JS_C1 = utils.createJuanshaCurve(_2_JS1_C1_p, b1_06, JS_b2_12, m, h1_06,
		h_06, _2_direc)
	
		_2_JS_C1_S = Surface.ByPatch(_2_JS_C1)
	
		result = List.AddItemToEnd(_2_JS_C1_S, result)
	
		#JS_C2
		_2_JS1_C2_p = Surface.PointAtParameter(_2_U2_S, JS_u, JS_mv)
	
		_2_JS_C2 = utils.createJuanshaCurve(_2_JS1_C2_p, b1_06, JS_b2_12, m, h1_06,
		h_06, _2_direc)
	
		_2_JS_C2_S = Surface.ByPatch(_2_JS_C2)
	
		result = List.AddItemToEnd(_2_JS_C2_S, result)
	
		_2_JS = []
		_2_JS = List.AddItemToEnd(_2_JS_C1, _2_JS)
		_2_JS = List.AddItemToEnd(_2_JS_C2, _2_JS)
		_2_JS_S = PolySurface.ByLoft(_2_JS)
	
		result = List.AddItemToEnd(_2_JS_S, result)
	
		#######_3_JS
		_3_direc = "y-"
		#JS_C1
		_3_JS1_C1_p = Surface.PointAtParameter(_3_U1_S, JS_u, JS_v)
	
		_3_JS_C1 = utils.createJuanshaCurve(_3_JS1_C1_p, b1_06, JS_b2_34, m, h1_06,
		h_06, _3_direc)
	
		_3_JS_C1_S = Surface.ByPatch(_3_JS_C1)
	
		result = List.AddItemToEnd(_3_JS_C1_S, result)
	
		#JS_C2
		_3_JS1_C2_p = Surface.PointAtParameter(_3_U1_S, JS_u, JS_mv)
	
		_3_JS_C2 = utils.createJuanshaCurve(_3_JS1_C2_p, b1_06, JS_b2_34, m, h1_06,
		h_06, _3_direc)
	
		_3_JS_C2_S = Surface.ByPatch(_3_JS_C2)
	
		result = List.AddItemToEnd(_3_JS_C2_S, result)
	
		_3_JS = []
		_3_JS = List.AddItemToEnd(_3_JS_C1, _3_JS)
		_3_JS = List.AddItemToEnd(_3_JS_C2, _3_JS)
		_3_JS_S = PolySurface.ByLoft(_3_JS)
	
		result = List.AddItemToEnd(_3_JS_S, result)
	
		#######_4_JS
		_4_direc = "y+"
		#JS_C1
		_4_JS1_C1_p = Surface.PointAtParameter(_3_U2_S, JS_u, JS_v)
	
		_4_JS_C1 = utils.createJuanshaCurve(_4_JS1_C1_p, b1_06, JS_b2_34, m, h1_06,
		h_06, _4_direc)
	
		_4_JS_C1_S = Surface.ByPatch(_4_JS_C1)
	
		result = List.AddItemToEnd(_4_JS_C1_S, result)
	
		#JS_C2
		_4_JS1_C2_p = Surface.PointAtParameter(_3_U2_S, JS_u, JS_mv)
	
		_4_JS_C2 = utils.createJuanshaCurve(_4_JS1_C2_p, b1_06, JS_b2_34, m, h1_06,
		h_06, _4_direc)
	
		_4_JS_C2_S = Surface.ByPatch(_4_JS_C2)
	
		result = List.AddItemToEnd(_4_JS_C2_S, result)
	
		_4_JS = []
		_4_JS = List.AddItemToEnd(_4_JS_C1, _4_JS)
		_4_JS = List.AddItemToEnd(_4_JS_C2, _4_JS)
		_4_JS_S = PolySurface.ByLoft(_4_JS)
	
		result = List.AddItemToEnd(_4_JS_S, result)
	
		#######_5_JS
		_5_direc = "x+"
		#JS_C1
		_5_JS1_C1_p = Surface.PointAtParameter(_3_U3_S, JS_u, JS_v)
	
		_5_JS_C1 = utils.createJuanshaCurve(_5_JS1_C1_p, b1_06, JS_b2_5, m, h1_06,
		h_06, _5_direc)
	
		_5_JS_C1_S = Surface.ByPatch(_5_JS_C1)
	
		result = List.AddItemToEnd(_5_JS_C1_S, result)
	
		#JS_C2
		_5_JS1_C2_p = Surface.PointAtParameter(_3_U3_S, JS_u, JS_mv)
	
		_5_JS_C2 = utils.createJuanshaCurve(_5_JS1_C2_p, b1_06, JS_b2_5, m, h1_06,
		h_06, _5_direc)
	
		_5_JS_C2_S = Surface.ByPatch(_5_JS_C2)
	
		result = List.AddItemToEnd(_5_JS_C2_S, result)
	
		_5_JS = []
		_5_JS = List.AddItemToEnd(_5_JS_C1, _5_JS)
		_5_JS = List.AddItemToEnd(_5_JS_C2, _5_JS)
		_5_JS_S = PolySurface.ByLoft(_5_JS)
	
		result = List.AddItemToEnd(_5_JS_S, result)
	
		#######create cuboid
		_1_JS_Ss = PolySurface.Surfaces(_1_JS_S)
		_1_JS_S7 = List.GetItemAtIndex(_1_JS_Ss, 7)
	
		_1_JS_C7 = Surface.PerimeterCurves(_1_JS_S7)
	
		_1_JS_PC7 = PolyCurve.ByJoinedCurves(_1_JS_C7)
	
		_2_JS_Ss = PolySurface.Surfaces(_2_JS_S)
		_2_JS_S7 = List.GetItemAtIndex(_2_JS_Ss, 7)
	
		_2_JS_C7 = Surface.PerimeterCurves(_2_JS_S7)
	
		_2_JS_PC7 = PolyCurve.ByJoinedCurves(_2_JS_C7)
	
		_1_Cub = []
	
		_1_Cub = List.AddItemToEnd(_1_JS_PC7, _1_Cub)
		_1_Cub = List.AddItemToEnd(_2_JS_PC7, _1_Cub)
		_1_Cub_S = PolySurface.ByLoft(_1_Cub)
	
		result = List.AddItemToEnd(_1_Cub_S, result)
	
	
		#######create cuboid
		_5_JS_Ss = PolySurface.Surfaces(_5_JS_S)
		_5_JS_S7 = List.GetItemAtIndex(_5_JS_Ss, 7)
	
		_5_JS_C7 = Surface.PerimeterCurves(_5_JS_S7)
	
		_5_JS_C7_0 = List.GetItemAtIndex(_5_JS_C7, 0)
		_5_JS_C7_1 = List.GetItemAtIndex(_5_JS_C7, 1)
		_5_JS_C7_2 = List.GetItemAtIndex(_5_JS_C7, 2)
		_5_JS_C7_3 = List.GetItemAtIndex(_5_JS_C7, 3)
	
		_5_JS_PC_f_1 = PolyCurve.ByJoinedCurves(_5_JS_C7)
	
		direc = "x-"
	
		_5_JS_PC0 = utils.createCubiod(_5_JS_C7_0, Cub_w, direc)
		_5_JS_PC1 = utils.createCubiod(_5_JS_C7_1, Cub_w, direc)
		_5_JS_PC2 = utils.createCubiod(_5_JS_C7_2, Cub_w, direc)
		_5_JS_PC3 = utils.createCubiod(_5_JS_C7_3, Cub_w, direc)
	
		_5_JS_0_4 = []
	
		_5_JS_0_4 = List.AddItemToEnd(_5_JS_PC0, _5_JS_0_4)
		_5_JS_0_4 = List.AddItemToEnd(_5_JS_PC1, _5_JS_0_4)
		_5_JS_0_4 = List.AddItemToEnd(_5_JS_PC2, _5_JS_0_4)
		_5_JS_0_4 = List.AddItemToEnd(_5_JS_PC3, _5_JS_0_4)
	
		_5_JS_PC_f_2 = PolyCurve.ByJoinedCurves(_5_JS_0_4)
	
		_5_JS_Cub = []
	
		_5_JS_Cub = List.AddItemToEnd(_5_JS_PC_f_1, _5_JS_Cub)
		_5_JS_Cub = List.AddItemToEnd(_5_JS_PC_f_2, _5_JS_Cub)
	
		_5_JS_Cub_S = Solid.ByLoft(_5_JS_Cub)
	
		result = List.AddItemToEnd(_5_JS_Cub_S, result)
	
	
	
		return result
	
############createSecond End############

############createThird############

	#create third
	
	def createThird(self, _2_1_JS_S, _2_2_JS_S, _2_3_JS_S, _2_4_JS_S, _2_5_JS_S, b2_01, b1_04, b2_04, h_04, h2_04, h2_05, h1_04, b_04,
	 b_07, m, t_08, b_10, b1_10,h1_10, h_10, b_11, b2_12, b_12, h_12, h_09, t_09, b_09):
	
		utils = Util()
		result = []
	
		#create quad translate dx
		Q_d_x = b2_01 / 2
		#create quad translate dy
		Q_d_y = b2_04 / 2
		#create quad -- r
		Q_r = b1_04 / 2
		#create Trape -- d
		T_d = (b_04 - b1_04) / 2
		#create U palne -- h1
		U_h1 = (h_04 - h1_04)
		#create JS -- u
		JS_u = h2_04 / U_h1
		#create JS -- v
		JS_v = (((b_04 - b2_04) / 2) + b2_04) / b_04
		#create JS -- mv
		JS_mv = 1 - ((((b_04 - b2_04) / 2) + b2_04) / b_04)
		#create JS -- b2_12
		JS_b2_12 = ((b_10 - 2 * b1_10) - b_07 - 2 * T_d) / 2
		#create JS -- b2_34
		JS_b2_34 = ((b_11 - 2 * b1_10) - t_08 - 2 * T_d) / 2
		#create JS -- b2_5
		JS_b2_5 = b2_12 - b1_10 - (b_04 - (((b_04 - b2_04) / 2) + b2_04))
		#create Cuboid -- width
		Cub_w = b_12 - b1_10 - JS_b2_5
		#####JS1
		###create quad
		_1_JS_Ss = PolySurface.Surfaces(_2_1_JS_S)
	
		_1_JS_S6 = List.GetItemAtIndex(_1_JS_Ss, 6)
	
		_1_Q_p = Surface.PointAtParameter(_1_JS_S6, 0.0, 1.0)
	
		_1_Q_p_trans = Geometry.Translate(_1_Q_p, Q_d_x, Q_d_y, 0.0)
	
		_1_Q = utils.createQuadCenter(_1_Q_p_trans, Q_r)
	
		_1_Q_S = Surface.ByPatch(_1_Q)
		#1
		result = List.AddItemToEnd(_1_Q_S, result)
	
		#####JS_2
		###*create quad
		_2_JS_Ss = PolySurface.Surfaces(_2_2_JS_S)
	
		_2_JS_S6 = List.GetItemAtIndex(_2_JS_Ss, 6)
	
		_2_Q_p = Surface.PointAtParameter(_2_JS_S6, 0.0, 1.0)
	
		_2_Q_p_trans = Geometry.Translate(_2_Q_p, Q_d_x, -Q_d_y, 0.0)
	
		_2_Q = utils.createQuadCenter(_2_Q_p_trans, Q_r)
	
		_2_Q_S = Surface.ByPatch(_2_Q)
		#2
		result = List.AddItemToEnd(_2_Q_S, result)
	
		#####JS_3
		###create quad
		_3_JS_Ss = PolySurface.Surfaces(_2_3_JS_S)
	
		_3_JS_S6 = List.GetItemAtIndex(_3_JS_Ss, 6)
	
		_3_Q_p = Surface.PointAtParameter(_3_JS_S6, 0.0, 1.0)
	
		_3_Q_p_trans = Geometry.Translate(_3_Q_p, Q_d_x, Q_d_y, 0.0)
	
		_3_Q = utils.createQuadCenter(_3_Q_p_trans, Q_r)
	
		_3_Q_S = Surface.ByPatch(_3_Q)
		#3
		result = List.AddItemToEnd(_3_Q_S, result)
	
		#####JS_4
		###create quad
		_4_JS_Ss = PolySurface.Surfaces(_2_4_JS_S)
	
		_4_JS_S6 = List.GetItemAtIndex(_4_JS_Ss, 6)
	
		_4_Q_p = Surface.PointAtParameter(_4_JS_S6, 0.0, 1.0)
	
		_4_Q_p_trans = Geometry.Translate(_4_Q_p, Q_d_x, -Q_d_y, 0.0)
	
		_4_Q = utils.createQuadCenter(_4_Q_p_trans, Q_r)
	
		_4_Q_S = Surface.ByPatch(_4_Q)
		#4
		result = List.AddItemToEnd(_4_Q_S, result)
	
		#####JS_5
		###create quad
		_5_JS_Ss = PolySurface.Surfaces(_2_5_JS_S)
	
		_5_JS_S6 = List.GetItemAtIndex(_5_JS_Ss, 6)
	
		_5_Q_p = Surface.PointAtParameter(_5_JS_S6, 0.0, 1.0)
	
		_5_Q_p_trans = Geometry.Translate(_5_Q_p, -Q_d_x, Q_d_y, 0.0)
	
		_5_Q = utils.createQuadCenter(_5_Q_p_trans, Q_r)
	
		_5_Q_S = Surface.ByPatch(_5_Q)
		#5
		result = List.AddItemToEnd(_5_Q_S, result)
	
		#####JS1
		###create Trape
		#T1
		_3_1_p_T1 = Surface.PointAtParameter(_1_Q_S, 0.5, 0.0)
	
		_3_1_direc1 = "y-"
		_3_1_T1 = utils.createTrape(_3_1_p_T1, b1_04, b_04, h1_04, T_d, _3_1_direc1)
	
		_3_1_T1_S = Surface.ByPatch(_3_1_T1)
		#6
		result = List.AddItemToEnd(_3_1_T1_S, result)
	
		#T2
		_3_1_p_T2 = Surface.PointAtParameter(_1_Q_S, 0.5, 1.0)
	
		_3_1_direc2 = "y+"
		_3_1_T2 = utils.createTrape(_3_1_p_T2, b1_04, b_04, h1_04, T_d, _3_1_direc2)
	
		_3_1_T2_S = Surface.ByPatch(_3_1_T2)
		#7
		result = List.AddItemToEnd(_3_1_T2_S, result)
	
		#T3
		_3_1_p_T3 = Surface.PointAtParameter(_1_Q_S, 1.0, 0.5)
	
		_3_1_direc3 = "x+"
		_3_1_T3 = utils.createTrape(_3_1_p_T3, b1_04, b_04, h1_04, T_d, _3_1_direc3)
	
		_3_1_T3_S = Surface.ByPatch(_3_1_T3)
		#8
		result = List.AddItemToEnd(_3_1_T3_S, result)
	
		#T4
		_3_1_p_T4 = Surface.PointAtParameter(_1_Q_S, 0.0, 0.5)
	
		_3_1_direc4 = "x-"
		_3_1_T4 = utils.createTrape(_3_1_p_T4, b1_04, b_04, h1_04, T_d, _3_1_direc4)
	
		_3_1_T4_S = Surface.ByPatch(_3_1_T4)
		#9
		result = List.AddItemToEnd(_3_1_T4_S, result)
	
		#####JS2
		###create Trape
		#T1
		_3_2_p_T1 = Surface.PointAtParameter(_2_Q_S, 0.5, 0.0)
	
		_3_2_direc1 = "y-"
		_3_2_T1 = utils.createTrape(_3_2_p_T1, b1_04, b_04, h1_04, T_d, _3_2_direc1)
	
		_3_2_T1_S = Surface.ByPatch(_3_2_T1)
		#10
		result = List.AddItemToEnd(_3_2_T1_S, result)
	
		#T2
		_3_2_p_T2 = Surface.PointAtParameter(_2_Q_S, 0.5, 1.0)
	
		_3_2_direc2 = "y+"
		_3_2_T2 = utils.createTrape(_3_2_p_T2, b1_04, b_04, h1_04, T_d, _3_2_direc2)
	
		_3_2_T2_S = Surface.ByPatch(_3_2_T2)
	
		result = List.AddItemToEnd(_3_2_T2_S, result)
	
		#T3
		_3_2_p_T3 = Surface.PointAtParameter(_2_Q_S, 1.0, 0.5)
	
		_3_2_direc3 = "x+"
		_3_2_T3 = utils.createTrape(_3_2_p_T3, b1_04, b_04, h1_04, T_d, _3_2_direc3)
	
		_3_2_T3_S = Surface.ByPatch(_3_2_T3)
	
		result = List.AddItemToEnd(_3_2_T3_S, result)
	
		#T4
		_3_2_p_T4 = Surface.PointAtParameter(_2_Q_S, 0.0, 0.5)
	
		_3_2_direc4 = "x-"
		_3_2_T4 = utils.createTrape(_3_2_p_T4, b1_04, b_04, h1_04, T_d, _3_2_direc4)
	
		_3_2_T4_S = Surface.ByPatch(_3_2_T4)
	
		result = List.AddItemToEnd(_3_2_T4_S, result)
	
		#####JS3
		###create Trape
		#T1
		_3_3_p_T1 = Surface.PointAtParameter(_3_Q_S, 0.5, 0.0)
	
		_3_3_direc1 = "y-"
		_3_3_T1 = utils.createTrape(_3_3_p_T1, b1_04, b_04, h1_04, T_d, _3_3_direc1)
	
		_3_3_T1_S = Surface.ByPatch(_3_3_T1)
	
		result = List.AddItemToEnd(_3_3_T1_S, result)
	
		#T2
		_3_3_p_T2 = Surface.PointAtParameter(_3_Q_S, 0.5, 1.0)
	
		_3_3_direc2 = "y+"
		_3_3_T2 = utils.createTrape(_3_3_p_T2, b1_04, b_04, h1_04, T_d, _3_3_direc2)
	
		_3_3_T2_S = Surface.ByPatch(_3_3_T2)
	
		result = List.AddItemToEnd(_3_3_T2_S, result)
	
		#T3
		_3_3_p_T3 = Surface.PointAtParameter(_3_Q_S, 1.0, 0.5)
	
		_3_3_direc3 = "x+"
		_3_3_T3 = utils.createTrape(_3_3_p_T3, b1_04, b_04, h1_04, T_d, _3_3_direc3)
	
		_3_3_T3_S = Surface.ByPatch(_3_3_T3)
	
		result = List.AddItemToEnd(_3_3_T3_S, result)
	
		#T4
		_3_3_p_T4 = Surface.PointAtParameter(_3_Q_S, 0.0, 0.5)
	
		_3_3_direc4 = "x-"
		_3_3_T4 = utils.createTrape(_3_3_p_T4, b1_04, b_04, h1_04, T_d, _3_3_direc4)
	
		_3_3_T4_S = Surface.ByPatch(_3_3_T4)
	
		result = List.AddItemToEnd(_3_3_T4_S, result)
	
		#####JS4
		###create Trape
		#T1
		_3_4_p_T1 = Surface.PointAtParameter(_4_Q_S, 0.5, 0.0)
	
		_3_4_direc1 = "y-"
		_3_4_T1 = utils.createTrape(_3_4_p_T1, b1_04, b_04, h1_04, T_d, _3_4_direc1)
	
		_3_4_T1_S = Surface.ByPatch(_3_4_T1)
	
		result = List.AddItemToEnd(_3_4_T1_S, result)
	
		#T2
		_3_4_p_T2 = Surface.PointAtParameter(_4_Q_S, 0.5, 1.0)
	
		_3_4_direc2 = "y+"
		_3_4_T2 = utils.createTrape(_3_4_p_T2, b1_04, b_04, h1_04, T_d, _3_4_direc2)
	
		_3_4_T2_S = Surface.ByPatch(_3_4_T2)
	
		result = List.AddItemToEnd(_3_4_T2_S, result)
	
		#T3
		_3_4_p_T3 = Surface.PointAtParameter(_4_Q_S, 1.0, 0.5)
	
		_3_4_direc3 = "x+"
		_3_4_T3 = utils.createTrape(_3_4_p_T3, b1_04, b_04, h1_04, T_d, _3_4_direc3)
	
		_3_4_T3_S = Surface.ByPatch(_3_4_T3)
	
		result = List.AddItemToEnd(_3_4_T3_S, result)
	
		#T4
		_3_4_p_T4 = Surface.PointAtParameter(_4_Q_S, 0.0, 0.5)
	
		_3_4_direc4 = "x-"
		_3_4_T4 = utils.createTrape(_3_4_p_T4, b1_04, b_04, h1_04, T_d, _3_4_direc4)
	
		_3_4_T4_S = Surface.ByPatch(_3_4_T4)
	
		result = List.AddItemToEnd(_3_4_T4_S, result)
	
		#####JS5
		###create Trape
		#T1
		_3_5_p_T1 = Surface.PointAtParameter(_5_Q_S, 0.5, 0.0)
	
		_3_5_direc1 = "y-"
		_3_5_T1 = utils.createTrape(_3_5_p_T1, b1_04, b_04, h1_04, T_d, _3_5_direc1)
	
		_3_5_T1_S = Surface.ByPatch(_3_5_T1)
	
		result = List.AddItemToEnd(_3_5_T1_S, result)
	
		#T2
		_3_5_p_T2 = Surface.PointAtParameter(_5_Q_S, 0.5, 1.0)
	
		_3_5_direc2 = "y+"
		_3_5_T2 = utils.createTrape(_3_5_p_T2, b1_04, b_04, h1_04, T_d, _3_5_direc2)
	
		_3_5_T2_S = Surface.ByPatch(_3_5_T2)
	
		result = List.AddItemToEnd(_3_5_T2_S, result)
	
		#T3
		_3_5_p_T3 = Surface.PointAtParameter(_5_Q_S, 1.0, 0.5)
	
		_3_5_direc3 = "x+"
		_3_5_T3 = utils.createTrape(_3_5_p_T3, b1_04, b_04, h1_04, T_d, _3_5_direc3)
	
		_3_5_T3_S = Surface.ByPatch(_3_5_T3)
	
		result = List.AddItemToEnd(_3_5_T3_S, result)
	
		#T4
		_3_5_p_T4 = Surface.PointAtParameter(_5_Q_S, 0.0, 0.5)
	
		_3_5_direc4 = "x-"
		_3_5_T4 = utils.createTrape(_3_5_p_T4, b1_04, b_04, h1_04, T_d, _3_5_direc4)
	
		_3_5_T4_S = Surface.ByPatch(_3_5_T4)
	
		result = List.AddItemToEnd(_3_5_T4_S, result)
	
		#####JS1
		###create U plane
		_3_1_direc12 = "x"
		#U1
		_3_1_p_U1 = Surface.PointAtParameter(_3_1_T1_S, 0.5, 0.0)
	
		_3_1_U1 = utils.createUPlane(_3_1_p_U1, b_04, b2_04, U_h1, h2_04, _3_1_direc12)
	
		_3_1_U1_S = Surface.ByPatch(_3_1_U1)
	
		result = List.AddItemToEnd(_3_1_U1_S, result)
	
		#U2
		_3_1_p_U2 = Surface.PointAtParameter(_3_1_T2_S, 0.5, 1.0)
	
		_3_1_U2 = utils.createUPlane(_3_1_p_U2, b_04, b2_04, U_h1, h2_04, _3_1_direc12)
	
		_3_1_U2_S = Surface.ByPatch(_3_1_U2)
	
		result = List.AddItemToEnd(_3_1_U2_S, result)
	
		_3_1_direc34 = "y"
		#U3
		_3_1_p_U3 = Surface.PointAtParameter(_3_1_T3_S, 0.0, 0.5)
	
		_3_1_U3 = utils.createUPlane(_3_1_p_U3, b_04, b2_04, U_h1, h2_04, _3_1_direc34)
	
		_3_1_U3_S = Surface.ByPatch(_3_1_U3)
	
		result = List.AddItemToEnd(_3_1_U3_S, result)
	
		#U4
		_3_1_p_U4 = Surface.PointAtParameter(_3_1_T4_S, 0.0, 0.5)
	
		_3_1_U4 = utils.createUPlane(_3_1_p_U4, b_04, b2_04, U_h1, h2_04, _3_1_direc34)
	
		_3_1_U4_S = Surface.ByPatch(_3_1_U4)
	
		result = List.AddItemToEnd(_3_1_U4_S, result)
	
		#####JS2
		###create U plane
		_3_2_direc12 = "x"
		#U1
		_3_2_p_U1 = Surface.PointAtParameter(_3_2_T1_S, 0.5, 0.0)
	
		_3_2_U1 = utils.createUPlane(_3_2_p_U1, b_04, b2_04, U_h1, h2_04, _3_2_direc12)
	
		_3_2_U1_S = Surface.ByPatch(_3_2_U1)
	
		result = List.AddItemToEnd(_3_2_U1_S, result)
	
		#U2
		_3_2_p_U2 = Surface.PointAtParameter(_3_2_T2_S, 0.5, 1.0)
	
		_3_2_U2 = utils.createUPlane(_3_2_p_U2, b_04, b2_04, U_h1, h2_04, _3_2_direc12)
	
		_3_2_U2_S = Surface.ByPatch(_3_2_U2)
	
		result = List.AddItemToEnd(_3_2_U2_S, result)
	
		_3_2_direc34 = "y"
		#U3
		_3_2_p_U3 = Surface.PointAtParameter(_3_2_T3_S, 0.0, 0.5)
	
		_3_2_U3 = utils.createUPlane(_3_2_p_U3, b_04, b2_04, U_h1, h2_04, _3_2_direc34)
	
		_3_2_U3_S = Surface.ByPatch(_3_2_U3)
	
		result = List.AddItemToEnd(_3_2_U3_S, result)
	
		#U4
		_3_2_p_U4 = Surface.PointAtParameter(_3_2_T4_S, 0.0, 0.5)
	
		_3_2_U4 = utils.createUPlane(_3_2_p_U4, b_04, b2_04, U_h1, h2_04, _3_2_direc34)
	
		_3_2_U4_S = Surface.ByPatch(_3_2_U4)
	
		result = List.AddItemToEnd(_3_2_U4_S, result)
	
		#####JS3
		###create U plane
		_3_3_direc12 = "x"
		#U1
		_3_3_p_U1 = Surface.PointAtParameter(_3_3_T1_S, 0.5, 0.0)
	
		_3_3_U1 = utils.createUPlane(_3_3_p_U1, b_04, b2_04, U_h1, h2_04, _3_3_direc12)
	
		_3_3_U1_S = Surface.ByPatch(_3_3_U1)
	
		result = List.AddItemToEnd(_3_3_U1_S, result)
	
		#U2
		_3_3_p_U2 = Surface.PointAtParameter(_3_3_T2_S, 0.5, 1.0)
	
		_3_3_U2 = utils.createUPlane(_3_3_p_U2, b_04, b2_04, U_h1, h2_04, _3_3_direc12)
	
		_3_3_U2_S = Surface.ByPatch(_3_3_U2)
	
		result = List.AddItemToEnd(_3_3_U2_S, result)
	
		_3_3_direc34 = "y"
		#U3
		_3_3_p_U3 = Surface.PointAtParameter(_3_3_T3_S, 0.0, 0.5)
	
		_3_3_U3 = utils.createUPlane(_3_3_p_U3, b_04, b2_04, U_h1, h2_04, _3_3_direc34)
	
		_3_3_U3_S = Surface.ByPatch(_3_3_U3)
	
		result = List.AddItemToEnd(_3_3_U3_S, result)
	
		#U4
		_3_3_p_U4 = Surface.PointAtParameter(_3_3_T4_S, 0.0, 0.5)
	
		_3_3_U4 = utils.createUPlane(_3_3_p_U4, b_04, b2_04, U_h1, h2_04, _3_3_direc34)
	
		_3_3_U4_S = Surface.ByPatch(_3_3_U4)
	
		result = List.AddItemToEnd(_3_3_U4_S, result)
	
		#####JS4
		###create U plane
		_3_4_direc12 = "x"
		#U1
		_3_4_p_U1 = Surface.PointAtParameter(_3_4_T1_S, 0.5, 0.0)
	
		_3_4_U1 = utils.createUPlane(_3_4_p_U1, b_04, b2_04, U_h1, h2_04, _3_4_direc12)
	
		_3_4_U1_S = Surface.ByPatch(_3_4_U1)
	
		result = List.AddItemToEnd(_3_4_U1_S, result)
	
		#U2
		_3_4_p_U2 = Surface.PointAtParameter(_3_4_T2_S, 0.5, 1.0)
	
		_3_4_U2 = utils.createUPlane(_3_4_p_U2, b_04, b2_04, U_h1, h2_04, _3_4_direc12)
	
		_3_4_U2_S = Surface.ByPatch(_3_4_U2)
	
		result = List.AddItemToEnd(_3_4_U2_S, result)
	
		_3_4_direc34 = "y"
		#U3
		_3_4_p_U3 = Surface.PointAtParameter(_3_4_T3_S, 0.0, 0.5)
	
		_3_4_U3 = utils.createUPlane(_3_4_p_U3, b_04, b2_04, U_h1, h2_04, _3_4_direc34)
	
		_3_4_U3_S = Surface.ByPatch(_3_4_U3)
	
		result = List.AddItemToEnd(_3_4_U3_S, result)
	
		#U4
		_3_4_p_U4 = Surface.PointAtParameter(_3_4_T4_S, 0.0, 0.5)
	
		_3_4_U4 = utils.createUPlane(_3_4_p_U4, b_04, b2_04, U_h1, h2_04, _3_4_direc34)
	
		_3_4_U4_S = Surface.ByPatch(_3_4_U4)
	
		result = List.AddItemToEnd(_3_4_U4_S, result)
	
		#####JS5
		###create U plane
		_3_5_direc12 = "x"
		#U1
		_3_5_p_U1 = Surface.PointAtParameter(_3_5_T1_S, 0.5, 0.0)
	
		_3_5_U1 = utils.createUPlane(_3_5_p_U1, b_04, b2_04, U_h1, h2_04, _3_5_direc12)
	
		_3_5_U1_S = Surface.ByPatch(_3_5_U1)
	
		result = List.AddItemToEnd(_3_5_U1_S, result)
	
		#U2
		_3_5_p_U2 = Surface.PointAtParameter(_3_5_T2_S, 0.5, 1.0)
	
		_3_5_U2 = utils.createUPlane(_3_5_p_U2, b_04, b2_04, U_h1, h2_04, _3_5_direc12)
	
		_3_5_U2_S = Surface.ByPatch(_3_5_U2)
	
		result = List.AddItemToEnd(_3_5_U2_S, result)
	
		_3_5_direc34 = "y"
		#U3
		_3_5_p_U3 = Surface.PointAtParameter(_3_5_T3_S, 0.0, 0.5)
	
		_3_5_U3 = utils.createUPlane(_3_5_p_U3, b_04, b2_04, U_h1, h2_04, _3_5_direc34)
	
		_3_5_U3_S = Surface.ByPatch(_3_5_U3)
	
		result = List.AddItemToEnd(_3_5_U3_S, result)
	
		#U4
		_3_5_p_U4 = Surface.PointAtParameter(_3_5_T4_S, 0.0, 0.5)
	
		_3_5_U4 = utils.createUPlane(_3_5_p_U4, b_04, b2_04, U_h1, h2_04, _3_5_direc34)
	
		_3_5_U4_S = Surface.ByPatch(_3_5_U4)
	
		result = List.AddItemToEnd(_3_5_U4_S, result)
	
		#####_1_JS
		_3_1_direc = "y-"
		#JS_C1
		_3_1_JS_C1_p = Surface.PointAtParameter(_3_3_U1_S, JS_u, JS_v)
	
		_3_1_JS_C1 = utils.createJuanshaCurve(_3_1_JS_C1_p, b1_10, JS_b2_12, m, h1_10,
		h_10, _3_1_direc)
	
		_3_1_JS_C1_S = Surface.ByPatch(_3_1_JS_C1)
	
		result = List.AddItemToEnd(_3_1_JS_C1_S, result)
	
		#JS_C2
		_3_1_JS_C2_p = Surface.PointAtParameter(_3_3_U1_S, JS_u, JS_mv)
	
		_3_1_JS_C2 = utils.createJuanshaCurve(_3_1_JS_C2_p, b1_10, JS_b2_12, m, h1_10,
		h_10, _3_1_direc)
	
		_3_1_JS_C2_S = Surface.ByPatch(_3_1_JS_C2)
	
		result = List.AddItemToEnd(_3_1_JS_C2_S, result)
	
		_3_1_JS = []
		_3_1_JS = List.AddItemToEnd(_3_1_JS_C1, _3_1_JS)
		_3_1_JS = List.AddItemToEnd(_3_1_JS_C2, _3_1_JS)
		_3_1_JS_S = PolySurface.ByLoft(_3_1_JS)
	
		result = List.AddItemToEnd(_3_1_JS_S, result)
	
		#####_2_JS
		_3_2_direc = "y+"
		#JS_C1
		_3_2_JS1_C1_p = Surface.PointAtParameter(_3_4_U2_S, JS_u, JS_v)
	
		_3_2_JS_C1 = utils.createJuanshaCurve(_3_2_JS1_C1_p, b1_10, JS_b2_12, m, h1_10,
		h_10, _3_2_direc)
	
		_3_2_JS_C1_S = Surface.ByPatch(_3_2_JS_C1)
	
		result = List.AddItemToEnd(_3_2_JS_C1_S, result)
	
		#JS_C2
		_3_2_JS1_C2_p = Surface.PointAtParameter(_3_4_U2_S, JS_u, JS_mv)
	
		_3_2_JS_C2 = utils.createJuanshaCurve(_3_2_JS1_C2_p, b1_10, JS_b2_12, m, h1_10,
		h_10, _3_2_direc)
	
		_3_2_JS_C2_S = Surface.ByPatch(_3_2_JS_C2)
	
		result = List.AddItemToEnd(_3_2_JS_C2_S, result)
	
		_3_2_JS = []
		_3_2_JS = List.AddItemToEnd(_3_2_JS_C1, _3_2_JS)
		_3_2_JS = List.AddItemToEnd(_3_2_JS_C2, _3_2_JS)
		_3_2_JS_S = PolySurface.ByLoft(_3_2_JS)
	
		result = List.AddItemToEnd(_3_2_JS_S, result)
	
		#####_3_JS
		_3_3_direc = "y-"
		#JS_C1
		_3_3_JS1_C1_p = Surface.PointAtParameter(_3_5_U1_S, JS_u, JS_v)
	
		_3_3_JS_C1 = utils.createJuanshaCurve(_3_3_JS1_C1_p, b1_10, JS_b2_34, m, h1_10,
		h_10, _3_3_direc)
	
		_3_3_JS_C1_S = Surface.ByPatch(_3_3_JS_C1)
	
		result = List.AddItemToEnd(_3_3_JS_C1_S, result)
	
		#JS_C2
		_3_3_JS1_C2_p = Surface.PointAtParameter(_3_5_U1_S, JS_u, JS_mv)
	
		_3_3_JS_C2 = utils.createJuanshaCurve(_3_3_JS1_C2_p, b1_10, JS_b2_34, m, h1_10,
		h_10, _3_3_direc)
	
		_3_3_JS_C2_S = Surface.ByPatch(_3_3_JS_C2)
	
		result = List.AddItemToEnd(_3_3_JS_C2_S, result)
	
		_3_3_JS = []
		_3_3_JS = List.AddItemToEnd(_3_3_JS_C1, _3_3_JS)
		_3_3_JS = List.AddItemToEnd(_3_3_JS_C2, _3_3_JS)
		_3_3_JS_S = PolySurface.ByLoft(_3_3_JS)
	
		result = List.AddItemToEnd(_3_3_JS_S, result)
	
		#####_4_JS
		_3_4_direc = "y+"
		#JS_C1
		_3_4_JS1_C1_p = Surface.PointAtParameter(_3_5_U2_S, JS_u, JS_v)
	
		_3_4_JS_C1 = utils.createJuanshaCurve(_3_4_JS1_C1_p, b1_10, JS_b2_34, m, h1_10,
		h_10, _3_4_direc)
	
		_3_4_JS_C1_S = Surface.ByPatch(_3_4_JS_C1)
	
		result = List.AddItemToEnd(_3_4_JS_C1_S, result)
	
		#JS_C2
		_3_4_JS1_C2_p = Surface.PointAtParameter(_3_5_U2_S, JS_u, JS_mv)
	
		_3_4_JS_C2 = utils.createJuanshaCurve(_3_4_JS1_C2_p, b1_10, JS_b2_34, m, h1_10,
		h_10, _3_4_direc)
	
		_3_4_JS_C2_S = Surface.ByPatch(_3_4_JS_C2)
	
		result = List.AddItemToEnd(_3_4_JS_C2_S, result)
	
		_3_4_JS = []
		_3_4_JS = List.AddItemToEnd(_3_4_JS_C1, _3_4_JS)
		_3_4_JS = List.AddItemToEnd(_3_4_JS_C2, _3_4_JS)
		_3_4_JS_S = PolySurface.ByLoft(_3_4_JS)
	
		result = List.AddItemToEnd(_3_4_JS_S, result)
	
		#####_5_JS
		_3_5_direc = "x+"
		#JS_C1
		_3_5_JS_C1_p = Surface.PointAtParameter(_3_5_U3_S, JS_u, JS_v)
	
		_3_5_JS_C1 = utils.createJuanshaCurve(_3_5_JS_C1_p, b1_10, JS_b2_5, m, h1_10,
		h_10, _3_5_direc)
	
		_3_5_JS_C1_S = Surface.ByPatch(_3_5_JS_C1)
	
		result = List.AddItemToEnd(_3_5_JS_C1_S, result)
	
		#JS_C2
		_3_5_JS_C2_p = Surface.PointAtParameter(_3_5_U3_S, JS_u, JS_mv)
	
		_3_5_JS_C2 = utils.createJuanshaCurve(_3_5_JS_C2_p, b1_10, JS_b2_5, m, h1_10,
		h_10, _3_5_direc)
	
		_3_5_JS_C2_S = Surface.ByPatch(_3_5_JS_C2)
	
		result = List.AddItemToEnd(_3_5_JS_C2_S, result)
	
		_3_5_JS = []
		_3_5_JS = List.AddItemToEnd(_3_5_JS_C1, _3_5_JS)
		_3_5_JS = List.AddItemToEnd(_3_5_JS_C2, _3_5_JS)
		_3_5_JS_S = PolySurface.ByLoft(_3_5_JS)
	
		result = List.AddItemToEnd(_3_5_JS_S, result)
	
		#####create cuboid 1
		_3_1_JS_Ss = PolySurface.Surfaces(_3_1_JS_S)
		_3_1_JS_S7 = List.GetItemAtIndex(_3_1_JS_Ss, 7)
	
		_3_1_JS_C7 = Surface.PerimeterCurves(_3_1_JS_S7)
	
		_3_1_JS_PC7 = PolyCurve.ByJoinedCurves(_3_1_JS_C7)
	
		_3_2_JS_Ss = PolySurface.Surfaces(_3_2_JS_S)
		_3_2_JS_S7 = List.GetItemAtIndex(_3_2_JS_Ss, 7)
	
		_3_2_JS_C7 = Surface.PerimeterCurves(_3_2_JS_S7)
	
		_3_2_JS_PC7 = PolyCurve.ByJoinedCurves(_3_2_JS_C7)
	
		_3_1_Cub = []
	
		_3_1_Cub = List.AddItemToEnd(_3_1_JS_PC7, _3_1_Cub)
		_3_1_Cub = List.AddItemToEnd(_3_2_JS_PC7, _3_1_Cub)
		_3_1_Cub_S = PolySurface.ByLoft(_3_1_Cub)
	
		result = List.AddItemToEnd(_3_1_Cub_S, result)
	
		#####create cuboid 2
		_3_3_JS_Ss = PolySurface.Surfaces(_3_3_JS_S)
		_3_3_JS_S7 = List.GetItemAtIndex(_3_3_JS_Ss, 7)
	
		_3_3_JS_C7 = Surface.PerimeterCurves(_3_3_JS_S7)
	
		_3_3_JS_PC7 = PolyCurve.ByJoinedCurves(_3_3_JS_C7)
	
		_3_4_JS_Ss = PolySurface.Surfaces(_3_4_JS_S)
		_3_4_JS_S7 = List.GetItemAtIndex(_3_4_JS_Ss, 7)
	
		_3_4_JS_C7 = Surface.PerimeterCurves(_3_4_JS_S7)
	
		_3_4_JS_PC7 = PolyCurve.ByJoinedCurves(_3_4_JS_C7)
	
		_3_2_Cub = []
	
		_3_2_Cub = List.AddItemToEnd(_3_3_JS_PC7, _3_2_Cub)
		_3_2_Cub = List.AddItemToEnd(_3_4_JS_PC7, _3_2_Cub)
		_3_2_Cub_S = PolySurface.ByLoft(_3_2_Cub)
	
		result = List.AddItemToEnd(_3_2_Cub_S, result)
	
		###create cuboid
		_3_5_JS_Ss = PolySurface.Surfaces(_3_5_JS_S)
		_3_5_JS_S7 = List.GetItemAtIndex(_3_5_JS_Ss, 7)
	
		_3_5_JS_C7 = Surface.PerimeterCurves(_3_5_JS_S7)
	
		_3_5_JS_C7_0 = List.GetItemAtIndex(_3_5_JS_C7, 0)
		_3_5_JS_C7_1 = List.GetItemAtIndex(_3_5_JS_C7, 1)
		_3_5_JS_C7_2 = List.GetItemAtIndex(_3_5_JS_C7, 2)
		_3_5_JS_C7_3 = List.GetItemAtIndex(_3_5_JS_C7, 3)
	
		_3_5_JS_PC_f_1 = PolyCurve.ByJoinedCurves(_3_5_JS_C7)
	
		direc = "x-"
	
		_3_5_JS_PC0 = utils.createCubiod(_3_5_JS_C7_0, Cub_w, direc)
		_3_5_JS_PC1 = utils.createCubiod(_3_5_JS_C7_1, Cub_w, direc)
		_3_5_JS_PC2 = utils.createCubiod(_3_5_JS_C7_2, Cub_w, direc)
		_3_5_JS_PC3 = utils.createCubiod(_3_5_JS_C7_3, Cub_w, direc)
	
		_3_5_JS_0_4 = []
	
		_3_5_JS_0_4 = List.AddItemToEnd(_3_5_JS_PC0, _3_5_JS_0_4)
		_3_5_JS_0_4 = List.AddItemToEnd(_3_5_JS_PC1, _3_5_JS_0_4)
		_3_5_JS_0_4 = List.AddItemToEnd(_3_5_JS_PC2, _3_5_JS_0_4)
		_3_5_JS_0_4 = List.AddItemToEnd(_3_5_JS_PC3, _3_5_JS_0_4)
	
		_3_5_JS_PC_f_2 = PolyCurve.ByJoinedCurves(_3_5_JS_0_4)
	
		_3_5_JS_Cub = []
	
		_3_5_JS_Cub = List.AddItemToEnd(_3_5_JS_PC_f_1, _3_5_JS_Cub)
		_3_5_JS_Cub = List.AddItemToEnd(_3_5_JS_PC_f_2, _3_5_JS_Cub)
	
		_3_5_JS_Cub_S = Solid.ByLoft(_3_5_JS_Cub)
	
		result = List.AddItemToEnd(_3_5_JS_Cub_S, result)
	
		#####create fang
		_3_S_pC = Surface.PointAtParameter(_3_2_U2_S, JS_u, JS_v)
	
		_3_S_pD = Solid.Centroid(_3_5_JS_Cub_S)
	
		_3_F_pC = utils.getNDGFangCenterPoint(_3_S_pC, _3_S_pD, h_12 / 2)
	
		_3_F_Cub = Cuboid.ByLengths(_3_F_pC, t_09, b_09, h_09)
	
		result = List.AddItemToEnd(_3_F_Cub, result)
	
	
		return result
	
############createThird End############

############createFourth############

	#create fourth
	
	def createFourth(self, _3_1_Q_S, _3_2_Q_S, _3_1_JS_S, _3_2_JS_S, _3_3_JS_S, _3_4_JS_S, _3_5_JS_S, b2_01, b1_04, h_09, b2_04, h_04, h2_04, h2_05, h1_04,
	b_04, h_13, w_13, l_13, w_14, l_14, b1_15, t_15, b_15, h_15, centerPoint, h_01, h_16, r_16):
	
		utils = Util()
		result = []
		
		#create quad -- dz
		_4_Q_dz = (h_04 - h2_04) + h_09
		#create quad -- dx
		_4_Q_dx = b2_04 / 2
		#create quad -- dy
		_4_Q_dy = b2_01 / 2
		#create quad -- r
		_4_Q_r = b1_04 / 2
		#create Trape -- d
		_4_T_d = (b_04 - b1_04) / 2
		#create U palne -- h1
		_4_U_h1 = (h_04 - h1_04)
		#create MidPoint -- dh
		_4_MP_dh = h_04 - h1_04 - h2_04
		#create Fang -- dz
		_4_F_dz = h_04 - h2_04 + h_13 / 2
		#create JS -- u
		_4_JS_u = h2_04 / _4_U_h1
		#create JS -- v
		_4_JS_v = (((b_04 - b2_04) / 2) + b2_04) / b_04
		#create Fang db
		_4_F_db = b1_15 - (b_04 - _4_JS_v)
		#####Direct 1
		###create quad
		_4_1_Q_p = Surface.PointAtParameter(_3_1_Q_S, 0.5, 0.5)
	
		_4_1_Q_p_trans = Geometry.Translate(_4_1_Q_p, 0.0, 0.0, _4_Q_dz)
	
		_4_1_Q = utils.createQuadCenter(_4_1_Q_p_trans, _4_Q_r)
	
		_4_1_Q_S = Surface.ByPatch(_4_1_Q)
	
		result = List.AddItemToEnd(_4_1_Q_S, result)
	
		#####Direct 2
		###create quad
		_4_2_Q_p = Surface.PointAtParameter(_3_2_Q_S, 0.5, 0.5)
	
		_4_2_Q_p_trans = Geometry.Translate(_4_2_Q_p, 0.0, 0.0, _4_Q_dz)
	
		_4_2_Q = utils.createQuadCenter(_4_2_Q_p_trans, _4_Q_r)
	
		_4_2_Q_S = Surface.ByPatch(_4_2_Q)
	
		result = List.AddItemToEnd(_4_2_Q_S, result)
	
		#####Direct 3
		###create quad
		_3_1_JS_Ss = PolySurface.Surfaces(_3_1_JS_S)
	
		_3_1_JS_S6 = List.GetItemAtIndex(_3_1_JS_Ss, 6)
	
		_4_3_Q_p = Surface.PointAtParameter(_3_1_JS_S6, 0.0, 1.0)
	
		_4_3_Q_p_trans = Geometry.Translate(_4_3_Q_p, _4_Q_dx, _4_Q_dy, 0.0)
	
		_4_3_Q = utils.createQuadCenter(_4_3_Q_p_trans, _4_Q_r)
	
		_4_3_Q_S = Surface.ByPatch(_4_3_Q)
	
		result = List.AddItemToEnd(_4_3_Q_S, result)
	
		#####Direct 4
		###create quad
		_3_2_JS_Ss = PolySurface.Surfaces(_3_2_JS_S)
	
		_3_2_JS_S6 = List.GetItemAtIndex(_3_2_JS_Ss, 6)
	
		_4_4_Q_p = Surface.PointAtParameter(_3_2_JS_S6, 0.0, 1.0)
	
		_4_4_Q_p_trans = Geometry.Translate(_4_4_Q_p, _4_Q_dx, -_4_Q_dy, 0.0)
	
		_4_4_Q = utils.createQuadCenter(_4_4_Q_p_trans, _4_Q_r)
	
		_4_4_Q_S = Surface.ByPatch(_4_4_Q)
	
		result = List.AddItemToEnd(_4_4_Q_S, result)
	
		#####Direct 5
		###create quad
		_3_3_JS_Ss = PolySurface.Surfaces(_3_3_JS_S)
	
		_3_3_JS_S6 = List.GetItemAtIndex(_3_3_JS_Ss, 6)
	
		_4_5_Q_p = Surface.PointAtParameter(_3_3_JS_S6, 0.0, 1.0)
	
		_4_5_Q_p_trans = Geometry.Translate(_4_5_Q_p, _4_Q_dx, _4_Q_dy, 0.0)
	
		_4_5_Q = utils.createQuadCenter(_4_5_Q_p_trans, _4_Q_r)
	
		_4_5_Q_S = Surface.ByPatch(_4_5_Q)
	
		result = List.AddItemToEnd(_4_5_Q_S, result)
	
		#####Direct 6
		###create quad
		_3_4_JS_Ss = PolySurface.Surfaces(_3_4_JS_S)
	
		_3_4_JS_S6 = List.GetItemAtIndex(_3_4_JS_Ss, 6)
	
		_4_6_Q_p = Surface.PointAtParameter(_3_4_JS_S6, 0.0, 1.0)
	
		_4_6_Q_p_trans = Geometry.Translate(_4_6_Q_p, _4_Q_dx, -_4_Q_dy, 0.0)
	
		_4_6_Q = utils.createQuadCenter(_4_6_Q_p_trans, _4_Q_r)
	
		_4_6_Q_S = Surface.ByPatch(_4_6_Q)
	
		result = List.AddItemToEnd(_4_6_Q_S, result)
	
		#####Direct 7
		###create quad
		_3_5_JS_Ss = PolySurface.Surfaces(_3_5_JS_S)
	
		_3_5_JS_S6 = List.GetItemAtIndex(_3_5_JS_Ss, 6)
	
		_4_7_Q_p = Surface.PointAtParameter(_3_5_JS_S6, 0.0, 1.0)
	
		_4_7_Q_p_trans = Geometry.Translate(_4_7_Q_p, -_4_Q_dx, _4_Q_dy, 0.0)
	
		_4_7_Q = utils.createQuadCenter(_4_7_Q_p_trans, _4_Q_r)
	
		_4_7_Q_S = Surface.ByPatch(_4_7_Q)
	
		result = List.AddItemToEnd(_4_7_Q_S, result)
	
		#####JS1
		###create Trape
		#T1
		_4_1_p_T1 = Surface.PointAtParameter(_4_1_Q_S, 0.5, 0.0)
	
		_4_1_direc1 = "y-"
		_4_1_T1 = utils.createTrape(_4_1_p_T1, b1_04, b_04, h1_04, _4_T_d, _4_1_direc1)
	
		_4_1_T1_S = Surface.ByPatch(_4_1_T1)
		#6
		result = List.AddItemToEnd(_4_1_T1_S, result)
	
		#T2
		_4_1_p_T2 = Surface.PointAtParameter(_4_1_Q_S, 0.5, 1.0)
	
		_4_1_direc2 = "y+"
		_4_1_T2 = utils.createTrape(_4_1_p_T2, b1_04, b_04, h1_04, _4_T_d, _4_1_direc2)
	
		_4_1_T2_S = Surface.ByPatch(_4_1_T2)
		#7
		result = List.AddItemToEnd(_4_1_T2_S, result)
	
		#T3
		_4_1_p_T3 = Surface.PointAtParameter(_4_1_Q_S, 1.0, 0.5)
	
		_4_1_direc3 = "x+"
		_4_1_T3 = utils.createTrape(_4_1_p_T3, b1_04, b_04, h1_04, _4_T_d, _4_1_direc3)
	
		_4_1_T3_S = Surface.ByPatch(_4_1_T3)
		#8
		result = List.AddItemToEnd(_4_1_T3_S, result)
	
		#T4
		_4_1_p_T4 = Surface.PointAtParameter(_4_1_Q_S, 0.0, 0.5)
	
		_4_1_direc4 = "x-"
		_4_1_T4 = utils.createTrape(_4_1_p_T4, b1_04, b_04, h1_04, _4_T_d, _4_1_direc4)
	
		_4_1_T4_S = Surface.ByPatch(_4_1_T4)
		#9
		result = List.AddItemToEnd(_4_1_T4_S, result)
	
		#####JS2
		###create Trape
		#T1
		_4_2_p_T1 = Surface.PointAtParameter(_4_2_Q_S, 0.5, 0.0)
	
		_4_2_direc1 = "y-"
		_4_2_T1 = utils.createTrape(_4_2_p_T1, b1_04, b_04, h1_04, _4_T_d, _4_2_direc1)
	
		_4_2_T1_S = Surface.ByPatch(_4_2_T1)
		#10
		result = List.AddItemToEnd(_4_2_T1_S, result)
	
		#T2
		_4_2_p_T2 = Surface.PointAtParameter(_4_2_Q_S, 0.5, 1.0)
	
		_4_2_direc2 = "y+"
		_4_2_T2 = utils.createTrape(_4_2_p_T2, b1_04, b_04, h1_04, _4_T_d, _4_2_direc2)
	
		_4_2_T2_S = Surface.ByPatch(_4_2_T2)
	
		result = List.AddItemToEnd(_4_2_T2_S, result)
	
		#T3
		_4_2_p_T3 = Surface.PointAtParameter(_4_2_Q_S, 1.0, 0.5)
	
		_4_2_direc3 = "x+"
		_4_2_T3 = utils.createTrape(_4_2_p_T3, b1_04, b_04, h1_04, _4_T_d, _4_2_direc3)
	
		_4_2_T3_S = Surface.ByPatch(_4_2_T3)
	
		result = List.AddItemToEnd(_4_2_T3_S, result)
	
		#T4
		_4_2_p_T4 = Surface.PointAtParameter(_4_2_Q_S, 0.0, 0.5)
	
		_4_2_direc4 = "x-"
		_4_2_T4 = utils.createTrape(_4_2_p_T4, b1_04, b_04, h1_04, _4_T_d, _4_2_direc4)
	
		_4_2_T4_S = Surface.ByPatch(_4_2_T4)
	
		result = List.AddItemToEnd(_4_2_T4_S, result)
	
		#####JS3
		###create Trape
		#T1
		_4_3_p_T1 = Surface.PointAtParameter(_4_3_Q_S, 0.5, 0.0)
	
		_4_3_direc1 = "y-"
		_4_3_T1 = utils.createTrape(_4_3_p_T1, b1_04, b_04, h1_04, _4_T_d, _4_3_direc1)
	
		_4_3_T1_S = Surface.ByPatch(_4_3_T1)
	
		result = List.AddItemToEnd(_4_3_T1_S, result)
	
		#T2
		_4_3_p_T2 = Surface.PointAtParameter(_4_3_Q_S, 0.5, 1.0)
	
		_4_3_direc2 = "y+"
		_4_3_T2 = utils.createTrape(_4_3_p_T2, b1_04, b_04, h1_04, _4_T_d, _4_3_direc2)
	
		_4_3_T2_S = Surface.ByPatch(_4_3_T2)
	
		result = List.AddItemToEnd(_4_3_T2_S, result)
	
		#T3
		_4_3_p_T3 = Surface.PointAtParameter(_4_3_Q_S, 1.0, 0.5)
	
		_4_3_direc3 = "x+"
		_4_3_T3 = utils.createTrape(_4_3_p_T3, b1_04, b_04, h1_04, _4_T_d, _4_3_direc3)
	
		_4_3_T3_S = Surface.ByPatch(_4_3_T3)
	
		result = List.AddItemToEnd(_4_3_T3_S, result)
	
		#T4
		_4_3_p_T4 = Surface.PointAtParameter(_4_3_Q_S, 0.0, 0.5)
	
		_4_3_direc4 = "x-"
		_4_3_T4 = utils.createTrape(_4_3_p_T4, b1_04, b_04, h1_04, _4_T_d, _4_3_direc4)
	
		_4_3_T4_S = Surface.ByPatch(_4_3_T4)
	
		result = List.AddItemToEnd(_4_3_T4_S, result)
	
		#####JS4
		###create Trape
		#T1
		_4_4_p_T1 = Surface.PointAtParameter(_4_4_Q_S, 0.5, 0.0)
	
		_4_4_direc1 = "y-"
		_4_4_T1 = utils.createTrape(_4_4_p_T1, b1_04, b_04, h1_04, _4_T_d, _4_4_direc1)
	
		_4_4_T1_S = Surface.ByPatch(_4_4_T1)
	
		result = List.AddItemToEnd(_4_4_T1_S, result)
	
		#T2
		_4_4_p_T2 = Surface.PointAtParameter(_4_4_Q_S, 0.5, 1.0)
	
		_4_4_direc2 = "y+"
		_4_4_T2 = utils.createTrape(_4_4_p_T2, b1_04, b_04, h1_04, _4_T_d, _4_4_direc2)
	
		_4_4_T2_S = Surface.ByPatch(_4_4_T2)
	
		result = List.AddItemToEnd(_4_4_T2_S, result)
	
		#T3
		_4_4_p_T3 = Surface.PointAtParameter(_4_4_Q_S, 1.0, 0.5)
	
		_4_4_direc3 = "x+"
		_4_4_T3 = utils.createTrape(_4_4_p_T3, b1_04, b_04, h1_04, _4_T_d, _4_4_direc3)
	
		_4_4_T3_S = Surface.ByPatch(_4_4_T3)
	
		result = List.AddItemToEnd(_4_4_T3_S, result)
	
		#T4
		_4_4_p_T4 = Surface.PointAtParameter(_4_4_Q_S, 0.0, 0.5)
	
		_4_4_direc4 = "x-"
		_4_4_T4 = utils.createTrape(_4_4_p_T4, b1_04, b_04, h1_04, _4_T_d, _4_4_direc4)
	
		_4_4_T4_S = Surface.ByPatch(_4_4_T4)
	
		result = List.AddItemToEnd(_4_4_T4_S, result)
	
		#####JS5
		###create Trape
		#T1
		_4_5_p_T1 = Surface.PointAtParameter(_4_5_Q_S, 0.5, 0.0)
	
		_4_5_direc1 = "y-"
		_4_5_T1 = utils.createTrape(_4_5_p_T1, b1_04, b_04, h1_04, _4_T_d, _4_5_direc1)
	
		_4_5_T1_S = Surface.ByPatch(_4_5_T1)
	
		result = List.AddItemToEnd(_4_5_T1_S, result)
	
		#T2
		_4_5_p_T2 = Surface.PointAtParameter(_4_5_Q_S, 0.5, 1.0)
	
		_4_5_direc2 = "y+"
		_4_5_T2 = utils.createTrape(_4_5_p_T2, b1_04, b_04, h1_04, _4_T_d, _4_5_direc2)
	
		_4_5_T2_S = Surface.ByPatch(_4_5_T2)
	
		result = List.AddItemToEnd(_4_5_T2_S, result)
	
		#T3
		_4_5_p_T3 = Surface.PointAtParameter(_4_5_Q_S, 1.0, 0.5)
	
		_4_5_direc3 = "x+"
		_4_5_T3 = utils.createTrape(_4_5_p_T3, b1_04, b_04, h1_04, _4_T_d, _4_5_direc3)
	
		_4_5_T3_S = Surface.ByPatch(_4_5_T3)
	
		result = List.AddItemToEnd(_4_5_T3_S, result)
	
		#T4
		_4_5_p_T4 = Surface.PointAtParameter(_4_5_Q_S, 0.0, 0.5)
	
		_4_5_direc4 = "x-"
		_4_5_T4 = utils.createTrape(_4_5_p_T4, b1_04, b_04, h1_04, _4_T_d, _4_5_direc4)
	
		_4_5_T4_S = Surface.ByPatch(_4_5_T4)
	
		result = List.AddItemToEnd(_4_5_T4_S, result)
	
		#####JS6
		###create Trape
		#T1
		_4_6_p_T1 = Surface.PointAtParameter(_4_6_Q_S, 0.5, 0.0)
	
		_4_6_direc1 = "y-"
		_4_6_T1 = utils.createTrape(_4_6_p_T1, b1_04, b_04, h1_04, _4_T_d, _4_6_direc1)
	
		_4_6_T1_S = Surface.ByPatch(_4_6_T1)
	
		result = List.AddItemToEnd(_4_6_T1_S, result)
	
		#T2
		_4_6_p_T2 = Surface.PointAtParameter(_4_6_Q_S, 0.5, 1.0)
	
		_4_6_direc2 = "y+"
		_4_6_T2 = utils.createTrape(_4_6_p_T2, b1_04, b_04, h1_04, _4_T_d, _4_6_direc2)
	
		_4_6_T2_S = Surface.ByPatch(_4_6_T2)
	
		result = List.AddItemToEnd(_4_6_T2_S, result)
	
		#T3
		_4_6_p_T3 = Surface.PointAtParameter(_4_6_Q_S, 1.0, 0.5)
	
		_4_6_direc3 = "x+"
		_4_6_T3 = utils.createTrape(_4_6_p_T3, b1_04, b_04, h1_04, _4_T_d, _4_6_direc3)
	
		_4_6_T3_S = Surface.ByPatch(_4_6_T3)
	
		result = List.AddItemToEnd(_4_6_T3_S, result)
	
		#T4
		_4_6_p_T4 = Surface.PointAtParameter(_4_6_Q_S, 0.0, 0.5)
	
		_4_6_direc4 = "x-"
		_4_6_T4 = utils.createTrape(_4_6_p_T4, b1_04, b_04, h1_04, _4_T_d, _4_6_direc4)
	
		_4_6_T4_S = Surface.ByPatch(_4_6_T4)
	
		result = List.AddItemToEnd(_4_6_T4_S, result)
	
		#####JS7
		###create Trape
		#T1
		_4_7_p_T1 = Surface.PointAtParameter(_4_7_Q_S, 0.5, 0.0)
	
		_4_7_direc1 = "y-"
		_4_7_T1 = utils.createTrape(_4_7_p_T1, b1_04, b_04, h1_04, _4_T_d, _4_7_direc1)
	
		_4_7_T1_S = Surface.ByPatch(_4_7_T1)
	
		result = List.AddItemToEnd(_4_7_T1_S, result)
	
		#T2
		_4_7_p_T2 = Surface.PointAtParameter(_4_7_Q_S, 0.5, 1.0)
	
		_4_7_direc2 = "y+"
		_4_7_T2 = utils.createTrape(_4_7_p_T2, b1_04, b_04, h1_04, _4_T_d, _4_7_direc2)
	
		_4_7_T2_S = Surface.ByPatch(_4_7_T2)
	
		result = List.AddItemToEnd(_4_7_T2_S, result)
	
		#T3
		_4_7_p_T3 = Surface.PointAtParameter(_4_7_Q_S, 1.0, 0.5)
	
		_4_7_direc3 = "x+"
		_4_7_T3 = utils.createTrape(_4_7_p_T3, b1_04, b_04, h1_04, _4_T_d, _4_7_direc3)
	
		_4_7_T3_S = Surface.ByPatch(_4_7_T3)
	
		result = List.AddItemToEnd(_4_7_T3_S, result)
	
		#T4
		_4_7_p_T4 = Surface.PointAtParameter(_4_7_Q_S, 0.0, 0.5)
	
		_4_7_direc4 = "x-"
		_4_7_T4 = utils.createTrape(_4_7_p_T4, b1_04, b_04, h1_04, _4_T_d, _4_7_direc4)
	
		_4_7_T4_S = Surface.ByPatch(_4_7_T4)
	
		result = List.AddItemToEnd(_4_7_T4_S, result)
	
		#####JS1
		###create U plane
		_4_1_direc12 = "x"
		#U1
		_4_1_p_U1 = Surface.PointAtParameter(_4_1_T1_S, 0.5, 0.0)
	
		_4_1_U1 = utils.createUPlane(_4_1_p_U1, b_04, b2_04, _4_U_h1, h2_04, _4_1_direc12)
	
		_4_1_U1_S = Surface.ByPatch(_4_1_U1)
	
		result = List.AddItemToEnd(_4_1_U1_S, result)
	
		#U2
		_4_1_p_U2 = Surface.PointAtParameter(_4_1_T2_S, 0.5, 1.0)
	
		_4_1_U2 = utils.createUPlane(_4_1_p_U2, b_04, b2_04, _4_U_h1, h2_04, _4_1_direc12)
	
		_4_1_U2_S = Surface.ByPatch(_4_1_U2)
	
		result = List.AddItemToEnd(_4_1_U2_S, result)
	
		_4_1_direc34 = "y"
		#U3
		_4_1_p_U3 = Surface.PointAtParameter(_4_1_T3_S, 0.0, 0.5)
	
		_4_1_U3 = utils.createUPlane(_4_1_p_U3, b_04, b2_04, _4_U_h1, h2_04, _4_1_direc34)
	
		_4_1_U3_S = Surface.ByPatch(_4_1_U3)
	
		result = List.AddItemToEnd(_4_1_U3_S, result)
	
		#U4
		_4_1_p_U4 = Surface.PointAtParameter(_4_1_T4_S, 0.0, 0.5)
	
		_4_1_U4 = utils.createUPlane(_4_1_p_U4, b_04, b2_04, _4_U_h1, h2_04, _4_1_direc34)
	
		_4_1_U4_S = Surface.ByPatch(_4_1_U4)
	
		result = List.AddItemToEnd(_4_1_U4_S, result)
	
		#####JS2
		###create U plane
		_4_2_direc12 = "x"
		#U1
		_4_2_p_U1 = Surface.PointAtParameter(_4_2_T1_S, 0.5, 0.0)
	
		_4_2_U1 = utils.createUPlane(_4_2_p_U1, b_04, b2_04, _4_U_h1, h2_04, _4_2_direc12)
	
		_4_2_U1_S = Surface.ByPatch(_4_2_U1)
	
		result = List.AddItemToEnd(_4_2_U1_S, result)
	
		#U2
		_4_2_p_U2 = Surface.PointAtParameter(_4_2_T2_S, 0.5, 1.0)
	
		_4_2_U2 = utils.createUPlane(_4_2_p_U2, b_04, b2_04, _4_U_h1, h2_04, _4_2_direc12)
	
		_4_2_U2_S = Surface.ByPatch(_4_2_U2)
	
		result = List.AddItemToEnd(_4_2_U2_S, result)
	
		_4_2_direc34 = "y"
		#U3
		_4_2_p_U3 = Surface.PointAtParameter(_4_2_T3_S, 0.0, 0.5)
	
		_4_2_U3 = utils.createUPlane(_4_2_p_U3, b_04, b2_04, _4_U_h1, h2_04, _4_2_direc34)
	
		_4_2_U3_S = Surface.ByPatch(_4_2_U3)
	
		result = List.AddItemToEnd(_4_2_U3_S, result)
	
		#U4
		_4_2_p_U4 = Surface.PointAtParameter(_4_2_T4_S, 0.0, 0.5)
	
		_4_2_U4 = utils.createUPlane(_4_2_p_U4, b_04, b2_04, _4_U_h1, h2_04, _4_2_direc34)
	
		_4_2_U4_S = Surface.ByPatch(_4_2_U4)
	
		result = List.AddItemToEnd(_4_2_U4_S, result)
	
		#####JS3
		###create U plane
		_4_3_direc12 = "x"
		#U1
		_4_3_p_U1 = Surface.PointAtParameter(_4_3_T1_S, 0.5, 0.0)
	
		_4_3_U1 = utils.createUPlane(_4_3_p_U1, b_04, b2_04, _4_U_h1, h2_04, _4_3_direc12)
	
		_4_3_U1_S = Surface.ByPatch(_4_3_U1)
	
		result = List.AddItemToEnd(_4_3_U1_S, result)
	
		#U2
		_4_3_p_U2 = Surface.PointAtParameter(_4_3_T2_S, 0.5, 1.0)
	
		_4_3_U2 = utils.createUPlane(_4_3_p_U2, b_04, b2_04, _4_U_h1, h2_04, _4_3_direc12)
	
		_4_3_U2_S = Surface.ByPatch(_4_3_U2)
	
		result = List.AddItemToEnd(_4_3_U2_S, result)
	
		_4_3_direc34 = "y"
		#U3
		_4_3_p_U3 = Surface.PointAtParameter(_4_3_T3_S, 0.0, 0.5)
	
		_4_3_U3 = utils.createUPlane(_4_3_p_U3, b_04, b2_04, _4_U_h1, h2_04, _4_3_direc34)
	
		_4_3_U3_S = Surface.ByPatch(_4_3_U3)
	
		result = List.AddItemToEnd(_4_3_U3_S, result)
	
		#U4
		_4_3_p_U4 = Surface.PointAtParameter(_4_3_T4_S, 0.0, 0.5)
	
		_4_3_U4 = utils.createUPlane(_4_3_p_U4, b_04, b2_04, _4_U_h1, h2_04, _4_3_direc34)
	
		_4_3_U4_S = Surface.ByPatch(_4_3_U4)
	
		result = List.AddItemToEnd(_4_3_U4_S, result)
	
		#####JS4
		###create U plane
		_4_4_direc12 = "x"
		#U1
		_4_4_p_U1 = Surface.PointAtParameter(_4_4_T1_S, 0.5, 0.0)
	
		_4_4_U1 = utils.createUPlane(_4_4_p_U1, b_04, b2_04, _4_U_h1, h2_04, _4_4_direc12)
	
		_4_4_U1_S = Surface.ByPatch(_4_4_U1)
	
		result = List.AddItemToEnd(_4_4_U1_S, result)
	
		#U2
		_4_4_p_U2 = Surface.PointAtParameter(_4_4_T2_S, 0.5, 1.0)
	
		_4_4_U2 = utils.createUPlane(_4_4_p_U2, b_04, b2_04, _4_U_h1, h2_04, _4_4_direc12)
	
		_4_4_U2_S = Surface.ByPatch(_4_4_U2)
	
		result = List.AddItemToEnd(_4_4_U2_S, result)
	
		_4_4_direc34 = "y"
		#U3
		_4_4_p_U3 = Surface.PointAtParameter(_4_4_T3_S, 0.0, 0.5)
	
		_4_4_U3 = utils.createUPlane(_4_4_p_U3, b_04, b2_04, _4_U_h1, h2_04, _4_4_direc34)
	
		_4_4_U3_S = Surface.ByPatch(_4_4_U3)
	
		result = List.AddItemToEnd(_4_4_U3_S, result)
	
		#U4
		_4_4_p_U4 = Surface.PointAtParameter(_4_4_T4_S, 0.0, 0.5)
	
		_4_4_U4 = utils.createUPlane(_4_4_p_U4, b_04, b2_04, _4_U_h1, h2_04, _4_4_direc34)
	
		_4_4_U4_S = Surface.ByPatch(_4_4_U4)
	
		result = List.AddItemToEnd(_4_4_U4_S, result)
	
		#####JS5
		###create U plane
		_4_5_direc12 = "x"
		#U1
		_4_5_p_U1 = Surface.PointAtParameter(_4_5_T1_S, 0.5, 0.0)
	
		_4_5_U1 = utils.createUPlane(_4_5_p_U1, b_04, b2_04, _4_U_h1, h2_04, _4_5_direc12)
	
		_4_5_U1_S = Surface.ByPatch(_4_5_U1)
	
		result = List.AddItemToEnd(_4_5_U1_S, result)
	
		#U2
		_4_5_p_U2 = Surface.PointAtParameter(_4_5_T2_S, 0.5, 1.0)
	
		_4_5_U2 = utils.createUPlane(_4_5_p_U2, b_04, b2_04, _4_U_h1, h2_04, _4_5_direc12)
	
		_4_5_U2_S = Surface.ByPatch(_4_5_U2)
	
		result = List.AddItemToEnd(_4_5_U2_S, result)
	
		_4_5_direc34 = "y"
		#U3
		_4_5_p_U3 = Surface.PointAtParameter(_4_5_T3_S, 0.0, 0.5)
	
		_4_5_U3 = utils.createUPlane(_4_5_p_U3, b_04, b2_04, _4_U_h1, h2_04, _4_5_direc34)
	
		_4_5_U3_S = Surface.ByPatch(_4_5_U3)
	
		result = List.AddItemToEnd(_4_5_U3_S, result)
	
		#U4
		_4_5_p_U4 = Surface.PointAtParameter(_4_5_T4_S, 0.0, 0.5)
	
		_4_5_U4 = utils.createUPlane(_4_5_p_U4, b_04, b2_04, _4_U_h1, h2_04, _4_5_direc34)
	
		_4_5_U4_S = Surface.ByPatch(_4_5_U4)
	
		result = List.AddItemToEnd(_4_5_U4_S, result)
	
		#####JS6
		###create U plane
		_4_6_direc12 = "x"
		#U1
		_4_6_p_U1 = Surface.PointAtParameter(_4_6_T1_S, 0.5, 0.0)
	
		_4_6_U1 = utils.createUPlane(_4_6_p_U1, b_04, b2_04, _4_U_h1, h2_04, _4_6_direc12)
	
		_4_6_U1_S = Surface.ByPatch(_4_6_U1)
	
		result = List.AddItemToEnd(_4_6_U1_S, result)
	
		#U2
		_4_6_p_U2 = Surface.PointAtParameter(_4_6_T2_S, 0.5, 1.0)
	
		_4_6_U2 = utils.createUPlane(_4_6_p_U2, b_04, b2_04, _4_U_h1, h2_04, _4_6_direc12)
	
		_4_6_U2_S = Surface.ByPatch(_4_6_U2)
	
		result = List.AddItemToEnd(_4_6_U2_S, result)
	
		_4_6_direc34 = "y"
		#U3
		_4_6_p_U3 = Surface.PointAtParameter(_4_6_T3_S, 0.0, 0.5)
	
		_4_6_U3 = utils.createUPlane(_4_6_p_U3, b_04, b2_04, _4_U_h1, h2_04, _4_6_direc34)
	
		_4_6_U3_S = Surface.ByPatch(_4_6_U3)
	
		result = List.AddItemToEnd(_4_6_U3_S, result)
	
		#U4
		_4_6_p_U4 = Surface.PointAtParameter(_4_6_T4_S, 0.0, 0.5)
	
		_4_6_U4 = utils.createUPlane(_4_6_p_U4, b_04, b2_04, _4_U_h1, h2_04, _4_6_direc34)
	
		_4_6_U4_S = Surface.ByPatch(_4_6_U4)
	
		result = List.AddItemToEnd(_4_6_U4_S, result)
	
		#####JS7
		###create U plane
		_4_7_direc12 = "x"
		#U1
		_4_7_p_U1 = Surface.PointAtParameter(_4_7_T1_S, 0.5, 0.0)
	
		_4_7_U1 = utils.createUPlane(_4_7_p_U1, b_04, b2_04, _4_U_h1, h2_04, _4_7_direc12)
	
		_4_7_U1_S = Surface.ByPatch(_4_7_U1)
	
		result = List.AddItemToEnd(_4_7_U1_S, result)
	
		#U2
		_4_7_p_U2 = Surface.PointAtParameter(_4_7_T2_S, 0.5, 1.0)
	
		_4_7_U2 = utils.createUPlane(_4_7_p_U2, b_04, b2_04, _4_U_h1, h2_04, _4_7_direc12)
	
		_4_7_U2_S = Surface.ByPatch(_4_7_U2)
	
		result = List.AddItemToEnd(_4_7_U2_S, result)
	
		_4_7_direc34 = "y"
		#U3
		_4_7_p_U3 = Surface.PointAtParameter(_4_7_T3_S, 0.0, 0.5)
	
		_4_7_U3 = utils.createUPlane(_4_7_p_U3, b_04, b2_04, _4_U_h1, h2_04, _4_7_direc34)
	
		_4_7_U3_S = Surface.ByPatch(_4_7_U3)
	
		result = List.AddItemToEnd(_4_7_U3_S, result)
	
		#U4
		_4_7_p_U4 = Surface.PointAtParameter(_4_7_T4_S, 0.0, 0.5)
	
		_4_7_U4 = utils.createUPlane(_4_7_p_U4, b_04, b2_04, _4_U_h1, h2_04, _4_7_direc34)
	
		_4_7_U4_S = Surface.ByPatch(_4_7_U4)
	
		result = List.AddItemToEnd(_4_7_U4_S, result)
	
		#####create fang 1
	
		_4_1_p2 = Surface.PointAtParameter(_4_1_Q_S, 0.5, 0.5)
	
		_4_1_p1 = Surface.PointAtParameter(_4_2_Q_S, 0.5, 0.5)
	
		_4_1_F_p = utils.getMidPoint(_4_1_p1, _4_1_p2, h1_04, _4_MP_dh, h_13)
	
		_4_1_F_Cub = Cuboid.ByLengths(_4_1_F_p, w_13, l_13, h_13)
	
		result = List.AddItemToEnd(_4_1_F_Cub, result)
	
		#####create fang 2
	
		_4_2_p2 = Surface.PointAtParameter(_4_3_Q_S, 0.5, 0.5)
	
		_4_2_p1 = Surface.PointAtParameter(_4_4_Q_S, 0.5, 0.5)
	
		_4_2_F_p = utils.getMidPoint(_4_2_p1, _4_2_p2, h1_04, _4_MP_dh, h_13)
	
		_4_2_F_Cub = Cuboid.ByLengths(_4_2_F_p, w_14, l_14, h_13)
	
		result = List.AddItemToEnd(_4_2_F_Cub, result)
	
		#####create fang 3
	
		_4_3_p2 = Surface.PointAtParameter(_4_5_Q_S, 0.5, 0.5)
	
		_4_3_p1 = Surface.PointAtParameter(_4_6_Q_S, 0.5, 0.5)
	
		_4_3_F_p = utils.getMidPoint(_4_3_p1, _4_3_p2, h1_04, _4_MP_dh, h_13)
	
		_4_3_F_Cub = Cuboid.ByLengths(_4_3_F_p, w_14, l_14, h_13)
	
		result = List.AddItemToEnd(_4_3_F_Cub, result)
	
		#####create fang 4
	
		_4_4_p = Surface.PointAtParameter(_4_7_Q_S, 0.5, 0.5)
	
		_4_4_p_trans = Geometry.Translate(_4_4_p, 0.0, 0.0, _4_F_dz)
	
		_4_4_F_Cub = Cuboid.ByLengths(_4_4_p_trans, w_14, l_14, h_13)
	
		result = List.AddItemToEnd(_4_4_F_Cub, result)
	
		#####*create fang 5
	
		_4_5_p = Surface.PointAtParameter(_4_7_U3_S, _4_JS_u, _4_JS_v)
	
		_4_5_F_Cub = utils.getHGFang(_4_5_p, _4_F_db, t_15, b_15, h_15)
	
		result = List.AddItemToEnd(_4_5_F_Cub, result)
	
		#####create chazhu
	
		_4_1_CZ_startP = Point.ByCoordinates(0.0, 0.0, h_16)
	
		_4_1_CZ_endP = Geometry.Translate(centerPoint, 0.0, 0.0, h_01)
	
		_4_1_CZ = Cylinder.ByPointsRadius(_4_1_CZ_startP, _4_1_CZ_endP, r_16)
	
		result = List.AddItemToEnd(_4_1_CZ, result)
	
	
		return result
	
############createFourth End############

########################class ExtendUtil End########################

########################class FinalUtil########################

class FinalUtil:

	############createDouGong############

	#create dougong
	#@staticmethod
	def craeteDouGong(self, centerPoint, b1_01, h1_01, b_01, b2_01, h_01, h2_01, m, b_02, b1_02, h1_02, h_02, b_07, b1_04, b2_04, 
	h_04, h2_04, h2_05, h1_04, b_04, b_06, b1_06, h1_06, h_06, b2_08, b_08, t_08, b_10, b1_10, h1_10, h_10, b_11, b2_12, b_12, h_12, h_09, t_09, b_09,
	h_13, w_13, l_13, w_14, l_14, b1_15, t_15, b_15, h_15, h_16, r_16):
	

		exUtils = ExtendUtil()
		result = []
	
		first = exUtils.createFirst(centerPoint, b1_01, h1_01, b_01, b2_01, h_01, h2_01, m, b_02, b1_02, h1_02, h_02)
	
		#result = List.AddItemToEnd(first, result)
	
		second = exUtils.createSecond(first[9], first[12], first[15], b_07, b2_01, b1_04, b_02, b2_04,h_04, h2_04, 
		h2_05, h1_04, b_04, b_06, b1_06, h1_06, h_06, m, b2_08, b_08)
	
		#result = List.AddItemToEnd(second, result)
	
		third = exUtils.createThird(second[29], second[32], second[35], second[38], second[41], b2_01, b1_04, b2_04, 
		h_04, h2_04, h2_05, h1_04, b_04, b_07, m, t_08, b_10, b1_10, h1_10, h_10, b_11, b2_12, b_12, h_12, h_09, t_09, b_09)
	
		#result = List.AddItemToEnd(third, result)
	
		fourth = exUtils.createFourth(third[0], third[1], third[47], third[50], third[53], third[56], third[59], b2_01, b1_04, 
		h_09, b2_04, h_04, h2_04, h2_05, h1_04, b_04, h_13, w_13, l_13, w_14, l_14, b1_15, t_15, b_15, h_15, centerPoint, h_01, h_16, r_16)
	
		#result = List.AddItemToEnd(fourth, result)
	
		#result = List.Join(first)
		#result = List.Join(second)
		#result = List.Join(third)
		#result = List.Join(fourth)
	
		result = List.Join([first, second, third, fourth])
	
		return result

############createDouGong End############

########################class FinalUtil End########################

test = FinalUtil()
#test = ExtendUtil()
#test = Util()
#result_final = []

#first = test.createFirst(centerPoint, b1_01, h1_01, b_01, b2_01, h_01, h2_01, m, b_02, b1_02, h1_02, h_02)

#second = test.createSecond(first[9], first[12], first[15], b_07, b2_01, b1_04, b_02, b2_04,h_04, h2_04, h2_05, h1_04, 
#b_04, b_06, b1_06, h1_06, h_06, m, b2_08, b_08)

#third = test.createThird(second[29], second[32], second[35], second[38], second[41], b2_01, b1_04, b2_04, h_04, h2_04, h2_05, h1_04, b_04,
#b_07, m, t_08, b_10, b1_10, h1_10, h_10, b_11, b2_12, b_12, h_12, h_09, t_09, b_09)

#fourth = test.createFourth(third[0], third[1], third[47], third[50], third[53], third[56], third[59], b2_01, b1_04, h_09, b2_04, h_04, h2_04, h2_05, 
#h1_04, b_04, h_13, w_13, l_13, w_14, l_14, b1_15, t_15, b_15, h_15, centerPoint, h_01, h_16, r_16)

#result_final = List.Join([first, second, third, fourth])

result_final = test.craeteDouGong(centerPoint, b1_01, h1_01, b_01, b2_01, h_01, h2_01, m, b_02, b1_02, h1_02, h_02, b_07, b1_04, b2_04, 
h_04, h2_04, h2_05, h1_04, b_04, b_06, b1_06, h1_06, h_06, b2_08, b_08, t_08, b_10, b1_10, h1_10, h_10, b_11, b2_12, b_12, h_12, h_09, t_09, b_09, 
h_13, w_13, l_13, w_14, l_14, b1_15, t_15, b_15, h_15, h_16, r_16)


#将输出内容指定给 OUT 变量。
OUT = result_final
#u1 = test.createUPlane(centerPoint, 120, 40, 50, 36, "x")
#OUT = Surface.ByPatch(u1)