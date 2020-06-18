#this function implements the Beeman algorithm to solve the vibratory eom
#of the vehicle
#inputs are initial displacement, velocity, acceleration, mass, damping, and stiffness matrix, FN(handle to get_ff) and forcing function data struct
#outputs are the times where the solutions are found, and the resulting
#displacement, velocity and accelerations

import numpy as np, math, ff_2014_7
import numpy.linalg
def Beeman(X0,V0,A0,M,C,K,FN,D):
    if ( np.isscalar(X0) or np.isscalar(V0) or (not isinstance(A0,np.ndarray)) or (not isinstance(M,np.ndarray)) or (not isinstance(C,np.ndarray)) or (not isinstance(K,np.ndarray)) or (not isinstance(D,dict))):
        return ValueError("inputs were not of the right type (Beeman)")
    dof = X0.shape[0]
    if(not (V0.shape[0] == dof)):
        return ValueError("length of vectors X0 and V0 must be equal")
    if(not(A0.shape[0] == dof)):
        return ValueError("length of A0,V0,and X0 must be the same")
    if(not (A0.shape[1] == 3)):
        return ValueError("A0 must be a DOFx3 matrix")
    r, c = M.shape
    if(not(r == dof) or not(c == dof)):
        return ValueError("mass matrix must have dimension DOFxDOF")
    r, c = C.shape
    if(not(r == dof) or not(c == dof)):
        return ValueError("damping matrix must have dimension DOFxDOF")
    r,c = K.shape
    if(not(r ==dof) or not(c == dof)):
        return ValueError("stiffness matrix must have dimension DOFxDOF")
    if(D["t_out"] <= D['t_in']):
        return ValueError("the final time Tin must be greater than T0")
    if(D['N'] < 1):
        return ValueError('Number of integration steps must > 0')
    h = (D['t_out'] - D['t_in'])/D['N']
    T = np.zeros((D['N']+1, 1))
    X = np.zeros((D['N']+1,dof))
    V = np.zeros((D['N']+1,dof))
    A = np.zeros((D['N']+1,dof))
    T[2] = D['t_in']
    for i in range(2,D['N']):
        T[i+1] = T[i] + h
        FF, Dobj = FN(T[i+1],D)
        print(A[i,:])
        X[i+1,:] = X0.conj().T + h*V0.conj().T + ((h**2/6) * (4*A[i,:] - A[i-1,:]))
        V[i+1,:] = V0.conj().T + (h/12) * (23* A[i,:] - 16*A[i-1,:] + 5 * A[i-2,:])
        A[i+1,:] = np.linalg.solve(M, (FF-C*V[i+1,:]-K*X[i+1,:]))[0]
        for j in range(0,1):
            X[i+1,:] = X0.conj().T + h*V0.conj().T + ((h**2)/6) * (A[i+1,:]+2*A[i,:])
            V[i+1,:] = V0.conj().T + (h/2) * (A[i+1,:]+A[i,:])
            A[i+1,:] = np.linalg.solve(M, (FF-C*V[i+1,:] - K*X[i+1,:]))[0]
        X0 = X[i+1,:]
        V0 = V[i+1,:]
        A[i-2,:] = A[i-1,:]
        A[i-1,:] = A[i,:]
        A[i,:] = A[i+1,:]
    return T, X, V, A

   
