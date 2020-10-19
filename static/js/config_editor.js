(() => {
    var openEditor = ace.edit("open-editor");
    openEditor.setTheme("ace/theme/monokai");
    openEditor.session.setMode("ace/mode/javascript");

    var assistedEditor = ace.edit("assisted");
    assistedEditor.setTheme("ace/theme/monokai");
    assistedEditor.session.setMode("ace/mode/javascript");

    var solutionEditor = ace.edit("solution");
    solutionEditor.setTheme("ace/theme/monokai");
    solutionEditor.session.setMode("ace/mode/javascript");
}
)();
