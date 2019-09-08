import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('DSCoreNodes')
from DSCore import *

#输入参数列表
input = IN

centerPoint = input[0]
b1_01 = input[1]
h1_01 = input[2]
b_01 = input[3]
b2_01 = input[4]
h_01 = input[5]
h2_01 = input[6]
m = input[7]
b_02 = input[8]
b1_02 = input[9]
h1_02 = input[10]
h_02 = input[11]

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
	


########################class ExtendUtil End########################

test = ExtendUtil()
#test = Util()


#将输出内容指定给 OUT 变量。
OUT = test.createFirst(centerPoint, b1_01, h1_01, b_01, b2_01, h_01, h2_01, m, b_02, b1_02, h1_02, h_02)
#u1 = test.createUPlane(centerPoint, 120, 40, 50, 36, "x")
#OUT = Surface.ByPatch(u1)