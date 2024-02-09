var workspaceCount = 1;

document.addEventListener("DOMContentLoaded", () => {

    let add = document.getElementById("add-workspace");
    add.addEventListener("click", addWorkspace);

    addWorkspace();
});

function addWorkspace () {
    let workspace = document.createElement("div");
    workspace.textContent = `Workspace ${workspaceCount}`;
    workspace.classList.add("workspace");
    workspace.addEventListener("click", switchWorkspace);

    let footer = document.getElementsByTagName("footer")[0];
    footer.appendChild(workspace);

    workspaceCount ++;
}

function switchWorkspace() {
    console.log("Switch workspace");

}