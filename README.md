# jsonToCollapsed
Convert any json file to collapsed format used for flame graph.
Usage:
# Download flame graph git repo first to your local directory, say, work
git clone https://github.com/brendangregg/FlameGraph.git

# convert any.json to any.json.txt file
python convertJsonToCollapsed.py any.json

# Create flame graph
cat any.json.txt |perl ~/work/FlameGraph/flamegraph.pl --title "Tree Graph" > any.json.svg

To change the titile of graph, simple replace "Tree Graph" with "any title"

# Open any.json.svg in Chrome Browser
