document.addEventListener('DOMContentLoaded', function() {
    let questionDivs = document.querySelectorAll('.question_div');
    let currentQuestionIndex = 0;
    let colors = ['lightpink', 'lightgreen', 'lightblue', 'lightyellow', 'lavender', 'lightsalmon', 'lightcyan'];

    questionDivs[currentQuestionIndex].style.display = 'block';

    let questionIds = [];
    questionDivs.forEach(function(div) {
        let questionId = div.querySelector('input[type="radio"]').name.split('_')[1];
        questionIds.push(questionId);
    });
    document.getElementById('question_ids').value = questionIds.join(',');

    window.showNextQuestion = function() {
        if (currentQuestionIndex < questionDivs.length - 1) {
            questionDivs[currentQuestionIndex].style.display = 'none';
            currentQuestionIndex++;
            questionDivs[currentQuestionIndex].style.display = 'block';
        }
        updateButtons();
    };

    window.showPrevQuestion = function() {
        if (currentQuestionIndex > 0) {
            questionDivs[currentQuestionIndex].style.display = 'none';
            currentQuestionIndex--;
            questionDivs[currentQuestionIndex].style.display = 'block';
        }
        updateButtons();
    };

    function updateButtons() {
        let questionDiv = questionDivs[currentQuestionIndex];
        questionDiv.style.backgroundColor = colors[currentQuestionIndex % colors.length];
        document.getElementById('prevBtn').style.display = currentQuestionIndex === 0 ? 'none' : 'inline';
        document.getElementById('nextBtn').style.display = currentQuestionIndex === questionDivs.length - 1 ? 'none' : 'inline';
        document.getElementById('submitBtn').style.display = currentQuestionIndex === questionDivs.length - 1 ? 'inline' : 'none';
    }

    updateButtons();
});