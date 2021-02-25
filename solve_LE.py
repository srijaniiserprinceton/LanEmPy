# {{{ Library imports
import numpy as np
# }}}

class solve_LE:
    '''
    Class to solve the Lane-Emden equations. 
    Different algorithms for solving the ODE may be included later.
    '''
    # {{{def __init__(n, theta0 = 1, dtheta0 = 0):
    def __init__(self, n, h, theta0 = 1, dtheta0 = 0, thres = 1e-6):
        '''
        The default values of theta(xi=0) = 1
        and dtheta/dxi(xi=0) = 0 for the polytropes to have
        the central density and pressure at the center
        and zero density and temperature at the surface.

        n = polytropic index
        h = step length in xi
        thres = threshold for theta(xi_1)
        '''

        self.n = n
        self.theta0 = theta0
        self.dtheta0 = dtheta0

        # the step length in \xi
        self.h = h

        # defines the threshold for the code to stop
        # when theta is <= thres (which is almost zero)
        self.thres = thres

        # list of theta
        self.theta = np.array([self.theta0])
        # list of dtheta
        self.dtheta = np.array([self.dtheta0])

        # xi initialzed at the center (increases by h with each step)
        self.xi = 0

        # the number of grid points (increases by 1 with each step)
        self.N = 0

        # for now doing this since this is the only coded algorithm 
        self.backward_FD()

        # making the xi grid after the simulation
        self.xi_grid = np.linspace(0,self.xi,self.N+1)

    # }}}def __init__(n, theta0 = 1, dtheta0 = 0):

    #{{{ def backward_FD(self):
    def backward_FD(self):
        '''
        solves in a backward finite difference sense
        meaning, it uses the values of theta and dtheta at 
        the previous grid point to evaluate the next grid point.
        '''

        # evaluating the first step specially since we 
        # do not want terms like 1/0 for 1/xi terms
        self.take_first_step()

        while(self.theta[-1] >= self.thres):
            theta_new = self.theta[-1] + self.dtheta[-1] \
                         * (self.h - self.h**2/self.xi) \
                            - 0.5 * self.h**2 * self.theta[-1]**self.n

            dtheta_new = self.dtheta[-1] * (1 - 2*self.h/self.xi) \
                                    - self.h * self.theta[-1]**self.n

            self.theta = np.append(self.theta, theta_new)
            self.dtheta = np.append(self.dtheta, dtheta_new)

            # incrementing xi and step number N
            self.xi += self.h
            self.N += 1 

    #}}} def backward_FD(self):

    # {{{def take_first_step(self):
    def take_first_step(self):
        theta_new = self.theta0 - 0.5 * self.h**2 * self.theta0**self.n
        dtheta_new = - self.h * self.theta0**self.n

        # appending to the list
        self.theta = np.append(self.theta, theta_new)
        self.dtheta = np.append(self.dtheta, dtheta_new)

        # incrementing xi and step number N
        self.xi += self.h
        self.N += 1
        
    # }}}def take_first_step(self):
