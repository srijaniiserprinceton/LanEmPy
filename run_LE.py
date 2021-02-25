# {{{ Library imports
import numpy as np
import matplotlib.pyplot as plt 
import solve_LE
import plotter
# }}}

plt.ion()
plt.rcParams['font.size'] = 14

###############################
# simulation parameters
n_arr = np.linspace(2,4,8)      # array of polytropic index
h = 1e-3        # step length in non dimensional radius \xi
thres = 0      # threshold for stopping the ODE integration

###############################
# boundary conditions
theta0 = 1      # theta(\xi=0) = 1
dtheta0 = 0     # dtheta/dxi (\xi=0) = 0

if __name__ == "__main__":
    plt.figure(figsize=(12,6))
    for n in n_arr:
        solver = solve_LE.solve_LE(n,h,thres=thres)
        plt.plot(solver.xi_grid,solver.theta,label='n=%.3f'%n)
        print('xi_max = %.3f'%solver.xi)

    plt.xlim([0,None])
    plt.ylim([0,None])
    plt.xlabel('$\\xi$')
    plt.ylabel('$\\theta(\\xi)$')
    plt.title('Solutions to Lane-Emden equation')
    plt.legend()
    plt.grid(True,alpha=0.5)
    plt.tight_layout()

    plt.savefig('./output/HW2_p10.pdf')