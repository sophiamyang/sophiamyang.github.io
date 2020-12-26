# Python Visualization Landscape


Visualization is a big and hot topic. Many developers have their own solutions and contributed to many visualization packages in Python. Entering the Python visualization world, most people start with matplotlib. But matplotlib is limited in many ways. If you want to visualize a more complicated graph or with a lot more data, where can you go next? Which visualization library should you use? What does the Python visualization landscape look like? These are the questions I have pondered and there are many great resources out there to learn about the visualization landscape.

In PyCon 2017, Jake Vanderplas, core developer for Altair, presented a talk describing the history and landscape of Python visualization libraries (video: https://www.youtube.com/watch?v=FytuB8nFHPQ; slides: https://speakerdeck.com/jakevdp/pythons-visualization-landscape-pycon-2017). He visualized almost all of the Python visualization libraries in a connected graph showing the clusters and relationships among the tools. Nicolas P. Rougier later adapted the graph to the figure shown below. In November 2018, James Bednar, core developer for Bokeh, Holoviews, GeoViews, Datashader, Panel, and hvPlot, published an article further described the graph in details ([Bednar, 2018](https://www.anaconda.com/python-data-visualization-2018-why-so-many-libraries/)). Finally, in June 2019, Anaconda published pyviz.org as an open-platform to track and inform the public about the current python visualization tools and development. For any data scientists who try to understand the Python visualization landscape, I recommend you to start with pyviz.org.

![](landscape.png)
*Nicolas P. Rougier’s adaptation of the Python Visualization Landscape slide from Jake VanderPlas’ keynote at Pycon 2017*

To further understand the visualization landscape graph, in the Bednar article, he categories the libraries into two main groups:
- SciVis
- InfoVis

SciVis libraries including VisPy, glumpy, GT, Mayavi, ParaView, VTK, and yt primarily visualize three or four dimensions “physically situated data”. InfoVis libraries, including all the rest of the libraries, visualize “information in arbitrary spaces”. The Bednar article further grouped the InfoVis libraries the following subgroups:
- Matplotlib
- Matplotlib-based
- JavaScript
- JSON
- WebGL
- Other

## Matplotlib
Matplotlib was created by John D. Hunter in 2002 and released in 2003 for the purpose of better analyzing EEG data using 2D plots of arrays. John at the time was frustrated with the limitations of MATLAB and then emulated the MATLAB graphics commands to create the Python library Matplotlib. John D. Hunter wrote a brief history about Matplotlib, see https://matplotlib.org/3.1.0/users/history.html. The main advantage of Matplotlib is that it works well with any operating systems, supports many backends, and provides simple interface (https://pyvideo.org/scipy-2012/matplotlib-lessons-from-middle-age-or-how-you.html). However, there are several weaknesses of Matplotlib. As mentioned in Jake Vanderplas’s blog (http://jakevdp.github.io/blog/2013/03/23/matplotlib-and-the-future-of-visualization-in-python/), Matplotlib is not desirable for creating dynamic and interactive graphics, the syntax of Matplotlib is verbose, and the output shows age. Luckily, people have developed better tools around, or independent of Matplotlib to make Python visualization better.

## Matplotlib-based
Many Python packages are built on top of Matplotlib.

Cartopy was created in 2011 by the UK Met Office (Met Office, 2017). It is designed with a simple interface to plot maps using Matplotlib.

YT was released in 2008 by a group of astrophisical scholars. It is designed for astrophysical analysis and visualization (Turk, et al., 2010). It was initially developed to examine nested adaptive mesh refinement with Enzo, and has extended to work with various simulation methods.

seaborn was created by Michael Waskom in 2012, and first released in 2013. It is designed for statistical visualization. It is great for plotting distributions, relationships, and structure of the data.
Networkx was released in 2005 by Aric Hagberg, Pieter Swart, and Dan Schult. It is for visualizing, manipulating, and analyzing graphs and networks.

Pandas, the most popular data manipulation and analysis tool in Python, was created by Wes McKinney and was released in 2008. It provides plotting functions of pandas DataFrame using matplotlib.

Glue was created by the astronomy researchers, Chris Beaumont and Thomas Robitaille, in 2014. It is designed to explore relationships within and among related datasets with linked statistical graphics and linked datasets.

plotnine was released in 2017 and created by Hassan Kibirige. It is designed to improve the functionalities of ggpy by implementing a grammar of graphics in Python based on the ggplot2 library in R.

yellowbrick was released in 2016 and created by two professors Rebecca Bilbro and Benjamin Bengfort as teaching tool in a data science certificate program. It is designed for evaluating machine learning models and helping with the model selection and hyperparameter tuning process.

Scikit-plot was released in 2017 and created by Reiichiro Nakano to visualize scikit-learn objects. It is used to plot the results and performance of machine learning models.

Basemap was depreciated in favor of Cartopy.

ggpy is no longer maintained and developed.

## JavaScript
Matplotlib-based tools do not offer the interactivities I often desire in the plot. If I want interactive plots, the solution is Bokeh. Bokeh was released in 2013 and created by Bryan Van de Ven. It is using its JavaScript API, BokehJS, to provide dynamic and interactive visualization with large datasets in the browser. It also allows users to add custom JavaScript to display widget, hover, and other features in the plots. Another amazing feature of Bokeh is the Bokeh server, which can be used to create dashboard and apps.

Toyplot was released in 2014 and created by Timothy M. Shead from the Sandia National Laboratories. It is also built on JavaScript and also allows users to add and define their custom JavaScript modules. Similar to Bokeh, Toyplot provides many interactive visualization features such as creating animation plots.

Plotly was created by the Plotly software company, which was founded by Alex Johnson, Jack Parmer, Chris Parmer, and Matthew Sundquist in 2012. The Plotly Python API relies on its JavaScript API plotly.js, which built on d3.js. Similiar to Bokeh’s Bokeh server, Plotly has its own framework called Dash to create apps and dashboard. Unlike all the other Python visualization projects, Dash is not completely open sourced. It has an enterprise version to help clients deploy apps at scale.

bqplot was released and open-sourced in 2015 by Bloomberg. It is a “Grammar of Graphics-based interactive plotting framework for the Jupyter notebook” using d3.js and ipywidgets.(https://bqplot.readthedocs.io/en/latest/introduction.html).

Cufflinks was released in 2015 and created by Jorge Santos. It is built on top of Plotly and applied to pandas dataframe.

ipyleaflet was released in 2016 by Project Jupyter. It is designed to work with geospatial data to create interactive and dynamic Leaflet maps.

Lightining is no longer maintained and developed.

## JSON
Vega was created by a group of researchers from Stanford University and University of Washington in 2014 (Satyanarayan, Wongsuphasawat, & Heer, 2014). It is a visualization grammar on top of D3, with its specifications written in JSON format.

Vega-Lite was built on top of Vega with simplified specifications and automated visulization components. It is also developed by a group of researchers from Stanford University and University of Washington.
Altair is a declarative statistical visualization library, built on top of Vega and Vega-Lite. It was released by 2016 and created by Jake Vanderplas and Brian Granger. Altair translates simple Python code into the JSON-format Vega-Lite language.

vincent, d3po, and mpld3 are no longer maintained and developed.

## WebGL
The WebGL category includes the libraries that are built on JavaScript but targeting on the 3D viuliazation including ipyvolumn, ipyvolum, and Plotly.

ipyvolumn was released in 2017 by Maarten A. Breddels. It is specialized in invisualizing 3d volumes and glyphs in the Jupyter notebook.

pythreejs was released in 2015 and maintained by Jason Grout, Sylvain Corlay, and Vidar Tonaas Fauske. It is the Python version of the three.js API, which allows users to visualize and animate 3D objects.
Plotly was covered in the JavaScript section earlier.

## Other
Few other tools worth mentioning are datashader, holoviews, and hvplot.

Datashader was created by James Bednar in 2016. Datashader uses Numba and Dask to create a graphics pipeline system to represent big data quickly and effectively. It makes big data visualization possible.

Holoviews was released in 2015 and was created by Jean-Luc Stevens. Holoviews is a high-level tool built on top of Bokeh, matplotlib, and datashader. It provides a simple and concise interface for building Bokeh or matplotlib plots. By defining and describing your data in a metadata, Holoviews is able to plot the data effortlessly.

hvPlot was released in 2018 and created by Philipp Rudiger and James Bednar. It is an even higher-level plotting tool built on HoloViews. hvPlot makes plotting extremely easy with supported few data format — Pandas, XArray, DataArray, Dask, Streamz, and Intake. If you have need to plot a Pandas dataframe, hvPlot would be your ideal choice for easy interactive plots.

Among all of the Python visualization tools, my favorite are Bokeh, Holoviews, GeoViews, hvPlot, and datashader. Except for Bokeh, they are all part of [HoloViz](https://holoviz.org/). They make it easy to do interactive plots with any size of data. If you have not used Bokeh and HoloViz, make sure to check them out!

References:     
Bednar, J. (2018). Python Data Visualization 2018: Why So Many Libraries? https://www.anaconda.com/python-data-visualization-2018-why-so-many-libraries/     
Hunter, J. (2012). Matplotlib: Lessons from middle age. Or, how you too can turn a hundred lines of patch rejection into two hundred thousand lines of code. Scipy 2012. https://pyvideo.org/scipy-2012/matplotlib-lessons-from-middle-age-or-how-you.html     
Hunter, J. (2008). History. Matplotlib. https://matplotlib.org/3.1.0/users/history.html 
VanderPlas, J. (2013). Matplotlib and the Future of Visualization in Python. http://jakevdp.github.io/blog/2013/03/23/matplotlib-and-the-future-of-visualization-in-python/     
Met Office. (2017). SciTools: our history in a nutshell. https://www.ecmwf.int/sites/default/files/elibrary/2017/17850-scitools-our-history-nutshell.pdf     
Turk, M. J., Smith, B. D., Oishi, J. S., Skory, S., Skillman, S. W., Abel, T., & Norman, M. L. (2010). yt: A multi-code analysis toolkit for astrophysical simulation data. The Astrophysical Journal Supplement Series, 192(1), 9.     

By Sophia Yang on [October 24, 2019](https://sophiamyang.medium.com/python-visualization-landscape-3b95ede3d030)
