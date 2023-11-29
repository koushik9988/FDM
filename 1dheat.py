# 1d heat equation using numpy vectorization
import numpy as np
import matplotlib.pyplot as plt
import sys

L  = 2      # system lenght
N  = 10    # no  of node points
dx = L/(N-1) # lenght element
T  = 10    # total simulation time
dt = 0.001*dx*dx     # time step
Nt = int(T/dt)
alpha = 1 
k = (alpha*dt)/(dx*dx)
print("the vale of alpha*dt/dx^2:",k)

if k>0.5:
    print("Condition is False. Exiting program.")
    sys.exit()


t = 0
x = np.linspace(0,L,N)
u = np.zeros(N)
#print(u)
fig, ax = plt.subplots()

#initial conditio 
for i in range(N):
    if x[i]<0.5:
        u[i]=0
        continue
    if x[i]<=1.0 and x[i]>= 0.5:
        u[i]= 4*x[i]-1
        continue
    if x[i]>=1 and x[i]<=1.5:
        u[i] = 10 - 2*x[i]
        continue
    if x[i]>=1.5:
        u[i]=0
        u[0]=u[N-1]

    

u[0] = 0
u[N-1] = 0

for t in np.arange(0, T, dt):
#while t<T:
    u[1:N-1] = k*(u[2:N] + u[0:N-2]) + (1-2*k)*u[1:N-1]
    #print(u)
    t += dt

    ax.clear()
    ax.plot(x,u)
    ax.set_xlim([0,L])
    ax.set_ylim([-10,10])
    ax.set_title('Time Step: {:.2f}'.format(t))
    plt.pause(1e-1)
plt.show()


