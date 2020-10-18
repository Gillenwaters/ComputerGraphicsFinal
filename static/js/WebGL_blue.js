const main = () => {
    let canvas = document.getElementById('canvas');
    let gl = canvas.getContext("webgl"); 
        if (!gl) {
            alert("Failed to get WebGL context.\n"
            + "Your browser or device may not support WebGL.");
            return;
        }
    gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight);
    gl.clearColor(0, 0, 1, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);
}

main();