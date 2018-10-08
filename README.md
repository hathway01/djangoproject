IPL Data Project
=================

IPL Data Project is a simple django app that takes a csv file and plots the graph for following questions using high charts:

Generate the following plots ...

1. Plot the number of matches played per year of all the years in IPL.
2. Plot a stacked bar chart of matches won of all teams over all the years of IPL.
3. For the year 2016 plot the extra runs conceded per team.
4. For the year 2015 plot the top economical bowlers.
5. Discuss a "Story" you want to tell with the given data. As with part 1, prepare the data structure and plot with matplotlib.



Quick start:
--------------

1. Add "project" to your INSTALLED_APPS setting like this::
	INSTALLED_APPS = [
		...
		'dataproject',
		...
		]
2. Make sure you have django-redis installed: use pip install django-redis
3. Include the project URLconf in your project urls.py like this::
	path('project/',include('project.urls')),

4. Run './manage.py migrate' to create the project models.

5. Start the development server and visit localhost:8000/admin to create project.
6. Visit localhost:8000/project/ to view the project.
