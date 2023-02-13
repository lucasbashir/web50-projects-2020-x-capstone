document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#newalert').addEventListener('click', () => beep());
});


function beep() {
    alert("done")
}