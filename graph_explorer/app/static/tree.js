document.addEventListener("DOMContentLoaded", () => {
    let mainView = document.getElementById("main-view");
    let treeUl = document.getElementById("tree");


    if (mainView.children.length > 0) {
        for (let node of nodes) {
            // TODO: If node structure is changed, this should too
            treeUl.appendChild(createExpandableElement(node.name, "none"));
        }
    }
});

const Direction = {
    none: "none",
    inc: "inc",
    out: "out"
}


function createExpandableElement(node, direction) {
    let li = document.createElement("li");
    let details = document.createElement("details");
    let summary = document.createElement("summary");
    let span = document.createElement("span");
    let img = document.createElement("img")

    li.appendChild(details);
    details.appendChild(summary);
    summary.appendChild(span);
    span.appendChild(img);

    span.textContent = node;
    span.setAttribute("data-direction", direction);

    details.addEventListener("click", fetchChildNodes);
    details.setAttribute("data-visited", "false");
    details.setAttribute("data-node", node);

    return li;
}

function fetchChildNodes(event) {
    let node = getDetailsElement(event.target);

    if (node.getAttribute("data-visited") === "true") {
        return;
    }

    node.setAttribute("data-visited", "true");

    let csrf = getCSRFToken();
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () =>  {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let branches = JSON.parse(JSON.parse(xhr.responseText));
            appendBranches(branches, node);
        }
    };

    let url = `/tree/${node.getAttribute("data-node")}`;
    xhr.open("GET", url, true);
    xhr.setRequestHeader('X-CSRFToken', csrf);
    xhr.send();
}

function getDetailsElement(node) {
    while (!(node instanceof HTMLDetailsElement)) {
        node = node.parentNode;
    }
    return node
}


function appendBranches(branches, node) {
    let ul = document.createElement("ul");
    let nodeId = node.getAttribute("data-node");

    let child;
    let direction;

    node.appendChild(ul);

    branches.forEach((branch) => {
        console.log(branch);

        if (nodeId === branch.source) {
            child = branch.destination;
            direction = branch.directed ? Direction.out : Direction.none;
        } else {
            child = branch.source;
            direction = branch.directed ? Direction.inc : Direction.none;
        }

        ul.appendChild(createExpandableElement(child, direction));

    });
}


// TODO: Implement when non-expandable nodes will be needed
function createElement(content) {
    let li = document.createElement("li");
}

function getNodeIcon(direction) {
    switch (direction) {
        case "left": return "arrow.svg";
        case "right": return "arrow.svg";
        case "none": return "arrow.svg";
        default: return "arrow.svg";
    }
}

function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();

            if (cookie.substring(0, 10) === 'csrftoken=') {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}
