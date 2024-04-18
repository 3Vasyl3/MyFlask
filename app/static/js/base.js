const audio1 = document.querySelector("#sound1");
const audio2 = document.querySelector("#sound2");
const audio3 = document.querySelector("#sound3");

audio1.addEventListener("ended", function(){
    poverClass(".p1")
    document.querySelector(".p1").innerHTML="<svg width='32' height='32' fill='currentColor' class='bi' viewBox='0 0 16 16'><use xlink:href='#svgplay'/>";
    myAudio.currentTime = 0;
});

audio2.addEventListener("ended", function(){
    poverClass(".p2")
    document.querySelector(".p2").innerHTML="<svg width='32' height='32' fill='currentColor' class='bi' viewBox='0 0 16 16'><use xlink:href='#svgplay'/>";
  myAudio.currentTime = 0;
});

audio3.addEventListener("ended", function(){
    poverClass(".p3")
    document.querySelector(".p3").innerHTML="<svg width='32' height='32' fill='currentColor' class='bi' viewBox='0 0 16 16'><use xlink:href='#svgplay'/>";
    myAudio.currentTime = 0;
});

function poverClass(namer){
    document.querySelectorAll(namer).forEach((el) => {
        el.classList.remove('btn-outline-danger')
      })
      document.querySelectorAll(namer).forEach((el) => {
        el.classList.add('btn-outline-info')
      })
}

function togglePlay(namer, cl) {
  if (namer.paused == true) {
    document.querySelectorAll(cl).forEach((el) => {
        el.classList.remove('btn-outline-info')
      })
      document.querySelectorAll(cl).forEach((el) => {
        el.classList.add('btn-outline-danger')
      })
    namer.play();
    document.querySelector(cl).innerHTML='<svg width="32" height="32" fill="currentColor" class="bi" viewBox="0 0 16 16"><use xlink:href="#svgstop"/></svg>';
    }
  else {
    poverClass(cl)
    document.querySelector(cl).innerHTML="<svg width='32' height='32' fill='currentColor' class='bi' viewBox='0 0 16 16'><use xlink:href='#svgplay'/>";
    namer.currentTime = 0;
    namer.pause();
    }
}
