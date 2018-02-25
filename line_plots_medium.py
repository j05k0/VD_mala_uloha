import matplotlib.pyplot as plt
import pandas as pd
import csv

# Read the data into a pandas DataFrame.
# Dataset with 1000 records
vehicle_data = pd.read_csv("medium_dataset.csv")

# You typically want your plot to be ~1.33x wider than tall. This plot is a rare
# exception because of the number of lines being plotted on it.
# Common sizes: (10, 7.5) and (12, 9)
plt.figure(figsize=(12, 14))

# Remove the plot frame lines. They are unnecessary chartjunk.
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary chartjunk.
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# Limit the range of the plot to only where the data is.
# Avoid unnecessary whitespace.
plt.ylim(0, 160000)
plt.xlim(2007, 2017)

# Make sure your axis ticks are large enough to be easily read.
# You don't want your viewers squinting to read your plot.
plt.yticks(range(0, 160000, 10000), [str(x) for x in range(0, 160000, 10000)], fontsize=14)
plt.xticks(fontsize=14)

# Provide tick lines across the plot to help your viewers trace along
# the axis ticks. Make sure that the lines are light and small so they
# don't obscure the primary data lines.
for y in range(10000, 160000, 10000):
    plt.plot(range(2007, 2017), [y] * len(range(2007, 2017)), "--", lw=0.5, color="black", alpha=0.3)

# Remove the tick marks; they are unnecessary with the tick lines we just plotted.
plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="on", left="off", right="off", labelleft="on")

# Loading the names of the columns into list.
with open('medium_dataset.csv', 'rb') as medium:
    reader = csv.reader(medium)
    row = next(reader)
    majors = row[1:len(row)]

for rank, column in enumerate(majors):
    # Plot each line separately with its own color.
    plt.plot(vehicle_data.Year.values,
             vehicle_data[column].values,
             lw=2.5)

    # Add a text label to the right end of every line.
    y_pos = vehicle_data[column].values[-1] - 0.5

    # Again, make sure that all labels are large enough to be easily read
    # by the viewer.
    plt.text(2017.5, y_pos, column, fontsize=14)

plt.text(2013, 165000, "Yearly vehicle registration transfers by make in Australia, Queensland", fontsize=17, ha="center")

plt.text(2006, -10000,
         "Data source: https://data.qld.gov.au/dataset/vehicle-registration-transfers-by-year/resource/38ec1985-e8dd-485b-8d38-a08f93472e98",
         fontsize=10)

plt.savefig("vehicles_medium.png", bbox_inches="tight")
