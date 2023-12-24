var counter = 0;

const elements = document.getElementsByName('btn-radio')
const elements_yt = document.getElementsByName('yt-btn-radio')

elements[0].checked = true;
elements_yt[0].checked = true;

setInterval(() => {
    proxSlide(elements[counter]);
    proxSlide(elements_yt[counter]);
}, 5000)

function proxSlide(element){
    element.checked = false;
    counter ++;

    if (counter > 2){
        counter = 0;
    }
    element.checked = true;
}

