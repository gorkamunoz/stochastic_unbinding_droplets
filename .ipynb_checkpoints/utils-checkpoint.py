import numpy as np

def file_to_np(file, dim = 1):
    '''Transforms the data from the matlab files to numpy, merging the two dimensions 
    to have a longer single 1D trajectory'''
    if dim == 1:
        trajs = []
        for tt in np.unique(file[:,2]):
            x = file[file[:,2] == tt, 0]
            y = file[file[:,2] == tt, 1]
            y = y - y[0] + x[0]
            traj = np.append(x, y[1:])
            trajs.append(traj)  
        return trajs
    elif dim == 2:
        trajs = []
        for tt in np.unique(file[:,2]):
            x = file[file[:,2] == tt, 0]
            y = file[file[:,2] == tt, 1]
            trajs.append(np.vstack((x,y)))
        return trajs
        

def file_to_np_cut(file, T):
    '''Transforms the data from the matlab files to numpy, merging the two dimensions 
    to have a longer single 1D trajectory.
    In addition, it cuts all the trajectories to the same size T.'''
    trajs = np.zeros((file.shape[0], T))
    for idx, tt in enumerate(np.unique(file[:,2])):
        x = file[file[:,2] == tt, 0]
        y = file[file[:,2] == tt, 1]
        y = y - y[0] + x[0]
        traj = np.append(x, y[1:])
        if len(traj) >= T:
            trajs[idx,:] = traj[:T]
    trajs = trajs[trajs[:,0] != 0, :]
    return trajs

def TMSD(traj, t_lags):
    '''Calculate the time average mean squared displacement of a set of trajectories'''
    ttt = np.zeros_like(t_lags, dtype= float)
    for idx, t in enumerate(t_lags):        
        for p in range(len(traj)-t):
            ttt[idx] += (traj[p]-traj[p+t])**2            
        ttt[idx] /= len(traj)-t    
    return ttt

def diff_coeff(trajs):
    '''Calculates the 2-4 diffusion coefficient from a trivial fitting of the tMSD'''
    t_lag = np.array([2,3,4])    
    tmsd = []
    for t in trajs:
        tmsd.append(TMSD(t, t_lag))    
    D = []
    for t in tmsd:
        diff = -(t[0]-t[-1])/len(t)
        D.append(np.abs(diff))        
    return np.array(D)/4