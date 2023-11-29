''' 
2D unsteady heat equation solution using Finite difference method.
@kaushik kalita
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


Lx = 1      #  lenght along x axis
Ly = 1      #  lenght along y axis
Nx = 51     # no of grid point along x asis
Ny = 51     # no of grid points along y axis
dx = Lx/(Nx-1) # lenght element
dy = Ly/(Ny-1) # lenght element
T  = 10        # total simulation time
dt = 0.1*dx*dx     # time step
Nt = int(T/dt)
k = 0.1
alpha = (k*dt)/(dx*dx)
beta  = (k*dt)/(dy*dy)
print("value of alpha is",alpha)
print("value of beta is ",beta)
t = 0
u = np.zeros([Ny,Nx])

u_prev = np.zeros([Ny,Nx])
#print(u)

x = np.linspace(0,Lx,Nx)
y = np.linspace(0,Ly,Ny)
[X,Y] = np.meshgrid(x,y)

#-------initial condition----------------------
#u_initial = np.sin(X)+np.cos(X)
u_initial =1*np.ones([Ny,Nx])

u = np.copy(u_initial)

#-----------boundary condition---------------
u[:,0]    =  5  # Left boundary
u[:,Ny-1] =  -5  # Right boundary
u[0,:]    =  5   # Top boundary
u[Nx-1,:] =  -5 # Bottom boundary


conv_threshold = 1e-4  # Convergence threshold for steady state
conv = False

fig, ax = plt.subplots()
#ax = plt.axes(projection ='3d') #for 3d plot


for t in np.arange(0, T, dt): # numpy broadcasting
  u[1:Ny-1, 1:Nx-1] = (1 - 2 * alpha - 2 * beta) * u[1:Ny-1, 1:Nx-1] 
   + alpha * u[1:Ny-1, 2:Nx] + alpha * u[1:Ny-1, 0:Nx-2] + beta * u[2:Ny, 1:Nx-1] 
   + beta * u[0:Ny-2, 1:Nx-1]
  # (numpy array slicing ->array[start:stop:step] includes start and excludes stop )
  t += dt

  ax.clear()
  #ax.contourf(X,Y,u,100,cmap="coolwarm")
  ax.contourf(X,Y,u,10,cmap="coolwarm")
  #cbar = plt.colorbar(c)
  #ax.plot_surface(X,Y,u,cmap="coolwarm")
  ax.set_xlim([0,Lx])
  ax.set_ylim([0,Ly])
  ax.set_title('Time Step: {:.2f}'.format(t))
  plt.pause(1e-1)

plt.show()
