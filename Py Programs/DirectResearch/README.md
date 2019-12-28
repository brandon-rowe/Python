# Bro-Bat-Dash
Directed Research

<h4>Project overview</h4>
<p>
	<ul>
		<li>Use <a href="https://www.zeek.org/">Bro</a> to gather network data</li>
		<li>Use <a href="https://github.com/SuperCowPowers/bat">Bat</a> to organize and analyze network data</li>
		<li>Use <a href="https://plot.ly/">Plotly</a> to build a visual representation of the data</li>
	</ul>

<h5>Tools </h5>
	<ul>
		<li><a href="https://www.zeek.org/">Bro</a></li>
		<li><a href="https://github.com/SuperCowPowers/bat">Bat</a></li>
		<li><a href="https://plot.ly/">Plotly</a></li>
	</ul>
<h6>Links</h6>
	<ul>
		<li><a href="https://www.zeek.org/">Bro/Zeek</a></li>
		<li><a href="https://github.com/SuperCowPowers/bat">Bat</a></li>
		<li><a href="https://plot.ly/python/getting-started/">Plotly Python Documentation</a></li>
		<li><a href="https://plot.ly/~jackp/17500/your-first-dash-app/#/">Plotly Beginner</a></li>
		<li><a href="https://www.datacamp.com/community/tutorials/learn-build-dash-python">Plotly Tutorial</a></li>
		<li><a href="https://dash.plot.ly/?_ga=2.235153601.1123854720.1554688600-944203700.1554688600">Dash Tutorial</a></li>
		<li><a href="https://www.sciencedirect.com/science/article/pii/S2214579615000039">Research Paper (Layout)</a></li>	
	</ul>
	
</p>



<h6>Project Outline</h6>

<ol>
  <li>The data. We will focus on network traffic data. You can use the tool <a href="https://www.bro.org/">“Bro”</a> to monitor live traffic. Bro will output log files into the working directory. There are many log files including http log, dns log, connection log but we will be analyzing the http log file obtained from “Bro”.</li>
  <li>Machine Learning. Using machine learning to do anomaly detection will be the innovative part of the project. The http log file can be considered as the raw data and it has to be preprocessed in order to be used in python-based machine learning programs. You can use the tool <a href="https://github.com/SuperCowPowers/bat">“Bat”</a> to transform the http log file from Bro into something that python-based machine learning library can handle. A detailed example is <a href="https://nbviewer.jupyter.org/github/SuperCowPowers/bat/blob/master/notebooks/Anomaly_Detection.ipynb"> here</a>. You can do analysis on the data then. We will be using jupyter, python, etc. </li>
  <li>Visualization.  The tool we might want to use is <a href="https://plot.ly/">“plotly”</a>. We might want to use this tool to visualize the raw data or the results obtained in Step 2 in some creative way.</li>
</ol>
