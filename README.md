Solving heat eqautiona and advective equation using python

1D heat equation $$\frac{\partial T(x,t)}{\partial t} = k \frac{\partial^{2} T(x,t)}{\partial^{2} x}$$

forward difference in time  $$\frac{\partial T(x,t)}{\partial t} = \frac{T_{i}^{n+1} - T_{i}^{n}}{\Delta t}$$
And central difference in space  $$\frac{\partial^{2} T(x,t)}{\partial^{2} x} = \frac{T_{i+1}^{n} -2 T_{i}^{n} + T_{i-1}^{n}}{(\Delta x)^{2}} $$
