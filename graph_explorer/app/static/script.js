function redirect(baseUrl) {
    console.log(baseUrl)
    let visualizer = document.getElementById("visualizer_select").value;
    let data_source = document.getElementById("data_source_select").value;

    if (visualizer > 0 && data_source > 0) {
         window.location.href = `/main/${visualizer-1}/${data_source-1}`;
    }
}