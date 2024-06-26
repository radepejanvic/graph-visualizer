var workspaceCount;
document.addEventListener("DOMContentLoaded", () => {

    let add = document.getElementById("add-workspace");
    add.addEventListener("click", addWorkspace);

    getWorkspacesCount();

});

function addWorkspaceToDOM (counter) {

    let a = document.createElement("a");
    a.setAttribute("href", `/workspace/${counter-1}`);

    let workspace = document.createElement("div");
    workspace.textContent = `Workspace ${counter}`;
    workspace.classList.add("workspace");

    a.appendChild(workspace);

    let footer = document.getElementsByTagName("footer")[0];
    footer.appendChild(a);
}

// TODO: Change to be POST request
function getWorkspacesCount() {
    // Make an AJAX request to the add_workspace endpoint
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "/workspace/get", true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Request was successful, do something with the response if needed
            workspaceCount = parseInt(JSON.parse(xhr.responseText).count);

            console.log(typeof workspaceCount)

            for (let i = 0; i < workspaceCount; i++) {
                console.log(typeof workspaceCount);
                addWorkspaceToDOM(i + 1);
            }
        }
    };
    xhr.send();
}

function addWorkspace() {
    const csrftoken = getCSRFToken();

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/workspace/add", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {

            workspaceCount++;
            addWorkspaceToDOM(workspaceCount);
            console.log(xhr.responseText);
        }
    };
    xhr.send(JSON.stringify({}));
}