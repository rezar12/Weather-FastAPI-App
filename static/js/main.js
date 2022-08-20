
const tog = document.querySelector('#toggle');

// function timedRefresh(timeoutPeriod) {
// 	setTimeout("location.reload(true);",timeoutPeriod);
// }

// window.onload = timedRefresh(5000);

console.log('hello')

tog.addEventListener("click",function(){
    const container = document.querySelector('.container');
    const circle = document.querySelector('.circle');
    const text = document.querySelector('#toggletext');
    if (container.style.filter === "invert(0)") {
        container.style.filter = 'invert(1)';
        circle.style.left = "18px";
        text.textContent = "Light Mode";
      } else {
        container.style.filter = 'invert(0)';
        circle.style.left = "0px";
        text.textContent = "Dark Mode";
      }
    
    
})
