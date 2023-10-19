import xarray as xr 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs
import numpy as np 
import matplotlib.gridspec as gridspec
import cmocean.cm as cmo    

path = 'dados_epgmet/modis_data/AQUA_MODIS.20221001_20221031.L3m.MO.SST4.sst4.9km.nc'
path1 = 'dados_epgmet/modis_data/AQUA_MODIS.20221001_20221031.L3m.MO.CHL.chlor_a.9km.nc'

ds_tsm = xr.open_dataset(path)
ds_chl = xr.open_dataset(path1)

lat = ds_tsm.lat.data
lon = ds_tsm.lon.data

#plt.pcolor(lon, lat, ds_tsm.sst4[:,:])

fig = plt.figure(figsize=(12, 6))
gs = gridspec.GridSpec(1, 2, figure=fig, wspace=0.1, hspace=0.1)


levels = np.linspace(0, 30, 31)

ax1 = fig.add_subplot(gs[0], projection=ccrs.PlateCarree())

cst = ax1.contourf(lon, lat, ds_tsm.sst4, transform=ccrs.PlateCarree(), cmap=cmo.thermal, levels=levels)

ax1.coastlines()
ax1.gridlines()
ax1.set_title('SST MODIS')

plt.colorbar(cst, shrink= 0.7, aspect= 20, label='SST (°C)')
#ax1.colorbar()

ax2 = fig.add_subplot(gs[1], projection=ccrs.PlateCarree())

#levels_ch = np.linspace(0, 10, 11)

#calculando chrolofilla em escala logaritmica
chl = np.log10(ds_chl.chlor_a)

levels_ch = np.arange(np.round(chl.min()), np.round(chl.max()), 0.5) 

csch = ax2.contourf(lon, lat, chl, transform=ccrs.PlateCarree(), cmap=cmo.algae, levels=levels_ch)

ax2.coastlines()

ax2.gridlines()

ax2.set_title('CHL MODIS')  

plt.colorbar(csch, shrink= 0.7, aspect= 40, label='CHL (mg/m3)')


plt.show() 

