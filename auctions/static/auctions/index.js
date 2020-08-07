const active = document.querySelector('nav').dataset.active;

if(active){
    document.querySelector(`#${active}`).classList.add('active');
}