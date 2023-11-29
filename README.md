Solving heat eqaution and advective equation using python

1D heat equation $$\frac{\partial T(x,t)}{\partial t} = \alpha \frac{\partial^{2} T(x,t)}{\partial^{2} x}$$

forward difference in time  $$\frac{\partial T(x,t)}{\partial t} = \frac{T_{i}^{n+1} - T_{i}^{n}}{\Delta t}$$
And central difference in space  $$\frac{\partial^{2} T(x,t)}{\partial^{2} x} = \frac{T_{i+1}^{n} -2 T_{i}^{n} + T_{i-1}^{n}}{(\Delta x)^{2}} $$
Discritized 1D heat equation is $$T_{i}^{n+1} = K (T_{i+1}^{n} + T_{i-1}^{n}) + (1- 2K) T_{i}^{n}$$ 
where $$K =  \frac{\alpha \Delta t}{\Delta x^{2}}$$
Similarly for 2D heat equation  $$\frac{\partial T(x,y,t)}{\partial t} = \alpha ( \frac{\partial^{2} T(x,y,t)}{\partial^{2} x} +  \frac{\partial^{2} T(x,y,t)}{\partial^{2} y} )$$

