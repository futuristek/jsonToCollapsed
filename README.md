# jsonToCollapsed
Convert any json file to collapsed format used for flame graph.

Usage:
## Download flame graph git repo first to your local directory, say, /home/username/work
    git clone https://github.com/brendangregg/FlameGraph.git

## Convert any.json to any.json.txt file
    python convertJsonToCollapsed.py any.json

## Create flame graph
    cat any.json.txt |perl /home/usename/work/FlameGraph/flamegraph.pl --title "Tree Graph" > any.json.svg

To change the titile of graph, simple replace "Tree Graph" with "any title"

## Open any.json.svg in Chrome Browser

## Combine multiple SVG files into a single html report using combineSVG.py

    python combineSVG.py first.svg second.svg third.svg

## Open the resulting index.html in a web browser
