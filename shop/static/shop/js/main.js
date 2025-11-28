// Small JS to toggle blinking on click (pause/resume)
document.addEventListener('DOMContentLoaded', ()=>{
const logo = document.getElementById('site-logo');
const heroImg = document.getElementById('hero-img');
function togglePause(el){
const state = getComputedStyle(el).animationPlayState;
el.style.animationPlayState = (state === 'paused') ? 'running' : 'paused';
}
if(logo) logo.addEventListener('click', ()=> togglePause(logo));
if(heroImg) heroImg.addEventListener('click', ()=> togglePause(heroImg));
});