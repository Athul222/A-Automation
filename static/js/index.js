const hamBtn = document.querySelector(".ham-list")
hamBtn.addEventListener("click", function (e) {
    var isActive = this.classList.contains("active");
    console.log(isActive);
    if (isActive) {
        hamBtn.classList.remove("active")
        document.querySelector(".expand-nav-items").style.display = "none";
    } else {
        hamBtn.classList.toggle("active");
        document.querySelector(".expand-nav-items").style.display = "block";
    }
    console.log("Clicked!")
});


const moreBtn = document.querySelector(".more-btn");
const closeBtn = document.querySelector(".close-btn")
const mainLeftPartContainer = document.querySelector(".main-left-part");

moreBtn.addEventListener("click", () => {
    moreBtn.style.display = "none";
    closeBtn.style.display = "block";
    mainLeftPartContainer.style.display = "block";
})

var windowWidth = window.innerWidth;

closeBtn.addEventListener("click", () => {
    closeBtn.style.display = "none"
    moreBtn.style.display = "block"
    mainLeftPartContainer.style.display = "none";
});