import matplotlib.pylab as plt
import numpy as np
from skimage import io
from skimage.morphology import skeletonize


def BFS(imagen):
    
    img = io.imread(imagen)

    print("Camino para un punto")
    
    x0,y0 = 460,460
    x1,y1 = 500,80 
    
    plt.plot(x0,y0,'gx',markersize = 7)
    plt.plot(x1,y1,'rx',markersize = 7)
    plt.show()

    thr_img = img[:,:,0] > 128
    esqueleto = skeletonize(thr_img)
    plt.figure(figsize=(7,7))
    plt.imshow(esqueleto)
    
    mapT = ~esqueleto
    plt.imshow(mapT)
    plt.plot(x0,x0,'gx', markersize=14)
    plt.plot(x1,y1, 'rx', markersize = 14)
    
    _mapt = np.copy(mapT)
    boxr= 30
    
    cpys, cpxs = np.where(_mapt[y1-boxr:y1+boxr, x1-boxr: x1+boxr]==0)
    cpys += y1-boxr
    cpxs += x1-boxr
    idx = np.argmin(np.sqrt((cpys-y1)**2 + (cpxs-x1)**2))
    y,x = cpys[idx], cpxs[idx]
    
    pts_x = [x]
    
    pts_y = [y]
    
    pts_c = [0]
    
    xmesh, ymesh = np.meshgrid(np.arange(-1,2),np.arange(-1,2))
    ymesh = ymesh.reshape(-1)
    xmesh = xmesh.reshape(-1)
    
    
    dst = np.zeros((thr_img.shape))
    
    #BFS
    
    while(True):
        idc = np.argmin(pts_c)
        ct = pts_c.pop(idc)
        x = pts_x.pop(idc)
        y = pts_y.pop(idc)
        
        ys,xs =  np.where(_mapt[y-1:y+2,x-1:x+2]==0)
        _mapt[ys+y-1,xs+x-1] = ct
        _mapt[y,x] = 9999999
        
        dst[ys+y-1,xs+x-1] = ct + 1 
        
        pts_x.extend(xs+x-1) 
        pts_y.extend(ys+y-1)
        pts_c.extend([ct+1]*xs.shape[0])
        
        if pts_x == []:
            break
        if np.sqrt((x-x0)**2 + (y-y0)**2) <boxr:
            edx = x
            edy = y
            break
    
    plt.figure(figsize=(14,14))
    plt.imshow(dst)
        
    path_x = []
    path_y = []
    
    y = edy
    x = edx
    
    while(True):
        nbh = dst[y-1:y+2,x-1:x+2]
        nbh[1,1] = 9999999
        nbh[nbh==0] = 9999999
        if np.min(nbh) == 9999999:
            break
        
        idx = np.argmin(nbh)
        y += ymesh[idx]
        x += xmesh[idx]
        
        if np.sqrt((x-x1)**2 + (y-y1)**2) < boxr:
            print("Route found")
            break
        
        path_y.append(y)
        path_x.append(x)
        
    plt.figure(figsize=(14,14))
    plt.imshow(img)
    plt.plot(path_x,path_y, 'r-', linewidth = 15)
    plt.savefig('route1_'+imagen)