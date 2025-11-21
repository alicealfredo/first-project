let content = document.querySelector("#content");
let child = content.children;

console.log(child[0]);

let select = document.querySelector("select");
console.log(select.value);

select.addEventListener("change", function() {
    console.log(select.value);
});

let container = document.querySelector("#container");
container.innerHTML += `
    <p id="child1">
        Filho 01
    </p>
    <p id="child2">
        Filho 02
    </p>
`
let child2 = document.querySelector("#child2");
child2.innerHTML = `
    <p id="child2">
        Filho 02 substituído
    </p>
`
let child1 = document.querySelector("#child1");
container.removeChild(child1);


