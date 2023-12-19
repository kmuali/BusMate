document.addEventListener('DOMContentLoaded', function () {
    const map = document.getElementById('map');
    const nodes = [];
    const edges = [];

    map.addEventListener('click', function (e) {
        const newNode = { id: nodes.length + 1, x: e.offsetX, y: e.offsetY };
        nodes.push(newNode);
        renderMap();
    });

    function renderMap() {
        map.innerHTML = '';
        nodes.forEach(node => {
            const nodeElement = document.createElement('div');
            nodeElement.style.position = 'absolute';
            nodeElement.style.left = node.x + 'px';
            nodeElement.style.top = node.y + 'px';
            nodeElement.style.width = '10px';
            nodeElement.style.height = '10px';
            nodeElement.style.backgroundColor = 'red';
            nodeElement.style.borderRadius = '50%';
            nodeElement.style.cursor = 'pointer';
            nodeElement.setAttribute('data-id', node.id);

            nodeElement.addEventListener('click', function (e) {
                e.stopPropagation();
                const nodeId = parseInt(this.getAttribute('data-id'));
                if (edges.length === 0 || edges[edges.length - 1].length === 2) {
                    edges.push([nodeId]);
                } else {
                    edges[edges.length - 1].push(nodeId);
                }
                renderMap();
                outputJSON();
            });

            map.appendChild(nodeElement);
        });
    }

    function outputJSON() {
        const jsonOutput = {
            nodes: nodes,
            edges: edges.filter(edge => edge.length === 2)
        };
        console.log(JSON.stringify(jsonOutput, null, 2));
    }
});
