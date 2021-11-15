let btnRandom1 = document.getElementById("italian");
let btnRandom2 = document.getElementById("chinese");
let btnRandom3 = document.getElementById("american");
let btnRandom4 = document.getElementById("mexican");
let btnRandom5 = document.getElementById("fastfood");
let result = document.querySelector('h1');
let italian = ["Villa Grande", "Mama Rosas", "Pizza Joes", "Foxs", "Pizza Pie", "Pizza Plus", "Pizza Hut", "Vocellis", "Dominos", "Tanis", "Anna Maries", "Penn Street Pizza", "Butler Penne"];
let chinese = ["China Gourmet", "China One", "China Palace"];
let american = ["It's Just Wings", "Monroe Hotel", "Rachels Roadhouse", "Chop Shop", "Snack-N-Pack", "Burger Hut", "Texas Roadhouse", "Upper Crust", "Cannella Cafe", "Hoagie Shop", "Chilis", "Applebees", "Butler Brew Works", "Macs Rt8 Cafe"];
let mexican = ["Rey Azteca", "Compadres"];
let fastfood= ["Mcdonalds", "Arbys", "Wendys", "Burger King", "Subway", "KFC", "Dairy Queen", "Taco Bell"];

function getRandomNumber(min, max) {
    let step1 = max - min + 1;
    let step2 = Math.random() * step1;
    let result = Math.floor(step2) + min;
    return result;
}

btnRandom1.addEventListener('click', () => {
    let index = getRandomNumber(0, italian.length-1);
    result.innerText = italian[index];
});
btnRandom2.addEventListener('click', () => {
    let index = getRandomNumber(0, chinese.length-1);
    result.innerText = chinese[index];
});
btnRandom3.addEventListener('click', () => {
    let index = getRandomNumber(0, american.length-1);
    result.innerText = american[index];
});
btnRandom4.addEventListener('click', () => {
    let index = getRandomNumber(0, mexican.length-1);
    result.innerText = mexican[index];
});
btnRandom5.addEventListener('click', () => {
    let index = getRandomNumber(0, fastfood.length-1);
    result.innerText = fastfood[index];
});