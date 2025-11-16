# MapPlot.py
# Name: Tucker Quinn
# Date: November 16, 2025
# Assignment: Visualizations with 
import emissions
import matplotlib.pyplot as plt
emissions = emissions.get_emissions()
years = []
yearlyemissions = []
for i in range(43): # France & Monaco Data starts at 2623 (1970) and ends at 2665 (2012).
    year = ([emissions[2623 + i]["Year"]])
    co2emissions = (emissions[2623 + i]["Emissions"]["Type"]["CO2"])
    years.append(year)
    yearlyemissions.append(co2emissions)
plt.plot(years, yearlyemissions)
plt.savefig("output")
# My data shows the yearly CO2 emissions from Franch & Monaco, demonstrating their gradual reduction of emissions over time.