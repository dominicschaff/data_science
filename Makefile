all: intro

intro:
	mypy intro/play.py

graphs:
	python3 intro/graph_bar.py
	python3 intro/graph_histogram.py
	python3 intro/graph_line.py
	python3 intro/graph_multi.py
	python3 intro/graph_scatter.py
	python3 intro/graph_scatter_equal.py

clean:
	rm intro/*.png
