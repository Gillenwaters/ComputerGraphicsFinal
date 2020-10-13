let editor = ace.edit("editor");

let button = document.getElementById("run");
button.addEventListener("click", () => {
    let code = editor.getValue();
    eval(code);
})