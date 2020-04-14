
var questions = document.querySelectorAll(".question");

var tag_duoc_chon = document.querySelector("div[style='display: block;']");

if (tag_duoc_chon){
    window.scrollTo(0, tag_duoc_chon.getBoundingClientRect().top - 50);
}


function tra_loi(){
    for (var i = 0; i < questions.length; i++){
        questions[i].nextElementSibling.style.display = 'none';
        questions[i].style.color = 'blue';
        questions[i].querySelector("img").src = icon_question;
    }
    this.querySelector("img").src = icon_question_hover;
    this.style.color = 'black';
    this.nextElementSibling.style.display = 'block';
}

for (var i = 0; i < questions.length; i++){
    questions[i].addEventListener('click', tra_loi);
}