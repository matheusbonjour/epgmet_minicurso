import glob 
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import cmocean.cm as cmo
import matplotlib.gridspec as gridspec
import dask 
import metpy.calc as mpcalc 





path1 = 'dados_epgmet/dados/'

dado = glob.glob(path1 + '*.nc')

# concatenate all netcdf data in a single dataset
ds = xr.open_mfdataset(dado)

# select the region of interest
ds_area = ds.sel(latitude=slice(-10, 10), longitude=slice(-60, 10))

# select the variable of interest
sla = ds_area.sla.values.squeeze()

# hovmoller diagram 

gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[1, 6], hspace=0.03)

fig = plt.figure(figsize=(10, 13)) 

# Tick labels
x_tick_labels = [u'0\N{DEGREE SIGN}E', u'90\N{DEGREE SIGN}E',
                 u'180\N{DEGREE SIGN}E', u'90\N{DEGREE SIGN}W',
                 u'0\N{DEGREE SIGN}E']

# Top plot for geographic reference (makes small map)
ax1 = fig.add_subplot(gs[0, 0], projection=ccrs.PlateCarree(central_longitude=180))
ax1.set_extent([-60, 10, -10, 10], ccrs.PlateCarree(central_longitude=180))
ax1.set_yticks([40, 60])
ax1.set_yticklabels([u'40\N{DEGREE SIGN}N', u'60\N{DEGREE SIGN}N'])
ax1.set_xticks([-60, -30, 0])
ax1.set_xticklabels(x_tick_labels)
ax1.grid(linestyle='dotted', linewidth=2)

# Add geopolitical boundaries for map reference
ax1.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax1.add_feature(cfeature.LAKES.with_scale('50m'), color='black', linewidths=0.5)

# Set some titles
plt.title('Hovmoller Diagram', loc='left')
plt.title('NCEP/NCAR Reanalysis', loc='right')

