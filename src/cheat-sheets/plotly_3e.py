"""
What is Plotly?
Data visualization involves exploring data through visual representations.
Plotly helps you make visually appealing representations of the data you're
working with. Plotly is particularly well suited for visualizations that will be
presented online, because it supports interactive elements. Plotly express lets
you see a basic version of your plot with just a few lines of code. Once you
know the plot works for your data, you can refine the style of your plot.
"""

"""
Line graphs, scatter plots, and bar graphs
To make a plot with Plotly Express, you specify the data and then create a fig
object. The call to fig.show() opens the plot in a new browser tab. You have a
plot in just two lines of code!
"""
# Making a line graph
import plotly.express as px

x_values = list(range(11))
squares = [x**2 for x in x_values]

fig = px.line(x=x_values, y=squares)
fig.show()

# Making a scatter plot
import plotly.express as px

x_values = list(range(11))
squares = [x**2 for x in x_values]

fig = px.scatter(x=x_values, y=squares)
fig.show()

# Making a bar graph
import plotly.express as px

x_values = list(range(11))
squares = [x**2 for x in x_values]

fig = px.bar(x=x_values, y=squares)
fig.show()