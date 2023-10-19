import xarray as xr 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs
import numpy as np 
import matplotlib.gridspec as gridspec
import cmocean.cm as cmo    

path = 'dados_epgmet/modis_data/'
path1 = 'dados_epgmet/dados/'

dado1 = 'dt_global_allsat_phy_l4_20141022_20210726.nc'

ds_ssh = xr.open_dataset(path1 + dado1)

ds_ssh = ds_ssh.sel(latitude=slice(-10, 10), longitude=slice(-60, 10))

sla = ds_ssh.sla.values.squeeze() 
lat = ds_ssh.latitude.values
lon = ds_ssh.longitude.values


fig = plt.figure(figsize=(12, 6))
gs = gridspec.GridSpec(1, 1, figure=fig, wspace=0.1, hspace=0.1)


#levels = np.arange(np.min(sla), np.max(sla), 0.1)

ax1 = fig.add_subplot(gs[0], projection=ccrs.PlateCarree())

levels = np.linspace(np.nanmin(sla), np.nanmax(sla), 31)

csch = ax1.contourf(lon, lat, sla, transform=ccrs.PlateCarree(), cmap=cmo.balance, levels=levels)

ax1.coastlines()

gl = ax1.gridlines(crs=ccrs.PlateCarree(), color='gray', alpha=1.0, linestyle='--', linewidth=0.25, xlocs=np.arange(-180, 180, 5), ylocs=np.arange(-90, 90, 5), draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False


plt.colorbar(csch, shrink= 0.5, aspect= 20, label='m')

plt.show() 
