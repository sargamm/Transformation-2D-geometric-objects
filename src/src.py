#assuming rotation to be done with respect to the origin
from math import *
import time
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import copy
plt.ion()
def matrix_multiply(a,b):
	c=[0,0,0]
	for i in range(3):
		for j in range(3):
				c[i]+=a[i][j]*b[j]
	return c
class disc:
	def __init__(self,centre,r):
		self.centre=centre
		self.x=0
		self.r=r
		self.X=[]
		self.Y=[]
		self.translate=[]
		self.scale=[]
		self.rotate=[]
		self.parametric()
	def translation(self,dx,dy):
		self.translate=[[1,0,dx],[0,1,dy],[0,0,1]]
		self.centre=matrix_multiply(self.translate,self.centre)

		for i in range(361):
			a=matrix_multiply(self.translate,[self.X[i],self.Y[i],1])
			self.X[i]=a[0]
			self.Y[i]=a[1]
	def rotation(self,x):
		self.x=3.14*x/180
		self.rotate=[[cos(self.x),-sin(self.x),0],[sin(self.x),cos(self.x),0],[0,0,1]]
		self.centre=matrix_multiply(self.rotate,self.centre)
		for i in range(361):
			a=matrix_multiply(self.rotate,[self.X[i],self.Y[i],1])
			self.X[i]=a[0]
			self.Y[i]=a[1]
	def scaling(self,sx,sy):
		self.scale=[[sx,0,0],[0,sy,0],[0,0,1]]
		self.r=matrix_multiply(self.scale,self.r)
		self.parametric()
	def parametric(self):
		self.X=[]
		self.Y=[]
		for i in range(361):
			self.X.append(self.centre[0]+self.r[0]*cos(i))
			self.Y.append(self.centre[1]+self.r[1]*sin(i))
	def show(self):
		plt.close()
		self.parametric()
		plt.ion()
		#patches.Ellipse((self.centre[0],self.centre[1]),self.r[0]*2,self.r[1]*2,self.x)
		#print(a,' ',b,' ',self.r[0],' ',self.r[1])
		#plt.plot([1,2,3,4],[1,4,9,16],'ro')
		plt.axis([-5,10,-5,10])
		plt.plot(self.X,self.Y)
		#plt.show()
		plt.pause(0.001)
		print(a,' ',b,' ',self.r[0],' ',self.r[1])
class polygon:
	def __init__(self,vertices):
		self.vertices=vertices
		self.translate=[]
		self.scale=[]
		self.rotate=[]
	def translation(self,dx,dy):
		self.translate=[[1,0,dx],[0,1,dy],[0,0,1]]
		for i in range(len(self.vertices)):
			self.vertices[i]=matrix_multiply(self.translate,self.vertices[i])
	def rotation(self,x):
		self.x=3.14*x/180
		self.rotate=[[cos(self.x),-sin(self.x),0],[sin(self.x),cos(self.x),0],[0,0,1]]
		for i in range(len(self.vertices)):
			self.vertices[i]=matrix_multiply(self.rotate,self.vertices[i])
			for j in range(len(self.vertices[i])):
				self.vertices[i][j]=round(self.vertices[i][j],2)
		#print(self.vertices)
	def scaling(self,sx,sy):
		self.scale=[[sx,0,0],[0,sy,0],[0,0,1]]
		for i in range(len(self.vertices)):
			self.vertices[i]=matrix_multiply(self.scale,self.vertices[i])
	def show_vertices(self):
		s=''
		t=''
		for i in self.vertices:
			s+=str(i[0])+' '
		for i in self.vertices:
			t+=str(i[1])+' '
		print(s)
		print(t)
		plt.close()
		#print(self.vertices)
		X,Y,z=zip(*self.vertices)
		X=list(X)
		Y=list(Y)
		X.append(X[0])
		Y.append(Y[0])
		plt.ion()
		plt.axis([-5,10,-5,10])
		plt.plot(X,Y)
		plt.show()
		plt.pause(0.001)
option=input()
if option=='polygon':
	X=input().split(' ')
	Y=input().split(' ')
	vertices=[]
	for i in range(len(X)):
		vertices.append([])
		n=len(vertices)
		vertices[n-1].append(int(X[i]))
		vertices[n-1].append(int(Y[i]))
		vertices[n-1].append(1)
		p=polygon(vertices)
	while option!='quit':
		op=option[0]
		option=option[2:]
		if op=='S':
			sx,sy=map(int,option.split(' '))
			p.scaling(sx,sy)
			p.show_vertices()
		elif op=='R':
			x=int(option)
			p.rotation(x)
			p.show_vertices()
		elif op=='T':
			dx,dy=map(int,option.split(' '))
			p.translation(dx,dy)
			p.show_vertices()
		option=input()

elif option=='disc':
	a,b,r=map(int,input().split(' '))
	centre=[a,b,1]
	radii=[]
	radii.append(copy.deepcopy(r))
	radii.append(copy.deepcopy(r))
	radii.append(1)
	d=disc(centre,radii)
	while option!='quit':
		op=option[0]
		option=option[2:]
		if op=='S':
			sx,sy=map(int,option.split(' '))
			d.scaling(sx,sy)
			d.show()
		elif op=='R':
			x=int(option)
			d.rotation(x)
			d.show()
		elif op=='T':
			dx,dy=map(int,option.split(' '))
			d.translation(dx,dy)
			d.show()
		option=input()
#plt.axis([0,10,0,10])
#plt.show()
#time.sleep(15)
