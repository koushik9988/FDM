import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 1
b = 1
Lx = 2 * a      # Length along x-axis
Ly = b          # Length along y-axis

Nx = 100        # Number of grid points along x-axis
Ny = 100        # Number of grid points along y-axis

dx = Lx / (Nx - 1)  # Length element
dy = Ly / (Ny - 1)  # Length element

dx2 = dx * dx
dy2 = dy * dy

x = np.linspace(-a, a, Nx)
y = np.linspace(0, b, Ny)
X, Y = np.meshgrid(x, y)
u = np.zeros([Nx, Ny])
efx = np.zeros([Nx, Ny])
efy = np.zeros([Nx, Ny])
u_prev = np.zeros([Nx, Ny])

rho = np.zeros([Nx, Ny])
rho[5][5] = 0
rho[25][25] = 0

epsilon = 8.85e-12

# Set boundary conditions
u[:, 0] = -10     # Left boundary
u[:, Ny - 1] = -5  # Right boundary
u[0, :] = -10      # Top boundary
u[Nx - 1, :] = -5  # Bottom boundary

conv_threshold = 1e-4
it = 0
#while True:
while it <60000: 
    u_prev = np.copy(u)
    u[1:Nx - 1, 1:Ny - 1] = (0.5 / ((1 / dx2) + (1 / dy2))) * (
            (u[1:Nx - 1, 2:Ny] + u[1:Nx - 1, 0:Ny - 2]) / dy2 + (u[2:Nx, 1:Ny - 1] + u[0:Nx - 2, 1:Ny - 1]) / dx2 +
            rho[1:Nx - 1, 1:Ny - 1] / epsilon)

    
    if (it%50 == 0):
        R = - u[1:Nx - 1, 1:Ny - 1]*((1 / dx2) + (1 / dy2))*2 +  (
            (u[1:Nx - 1, 2:Ny] + u[1:Nx - 1, 0:Ny - 2]) / dy2 + (u[2:Nx, 1:Ny - 1] + u[0:Nx - 2, 1:Ny - 1]) / dx2 +
            rho[1:Nx - 1, 1:Ny - 1] / epsilon)
        L2 = np.sqrt(np.sum(R**2) / ((Nx*Ny)))
        print(L2)
        if L2 < conv_threshold:
            break
    it += 1

efx[1:Nx-1, :] = (u[0:Nx-2, :] - u[2:Nx+1, :]) / (2 * dx)
efy[:, 1:Ny-1] = (u[:, 0:Ny-2] - u[:, 2:Ny+1]) / (2 * dy)

    # one-sided difference on boundaries
efx[0, :] = (u[0, :] - u[1, :]) / dx
efx[Nx-1, :] = (u[-2, :] - u[-1, :]) / dx
efy[:, 0] = (u[:, 0] - u[:, 1]) / dy
efy[:, Ny-1] = (u[:, -2] - u[:, -1]) / dy

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, u.T, cmap='viridis')

#ax = fig.add_subplot(111)
#ax.contour(X, Y, efx.T, cmap='viridis',levels = 200)
#ax.contour(X, Y, u.T, cmap='viridis',levels = 200)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
#plt.plot(efx,efy)
#ax.set_zlabel('Potential (u)')
plt.show()

