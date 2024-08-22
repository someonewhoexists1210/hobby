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
        if (questionDivs[currentQuestionIndex].querySelector('input[type="radio"]:checked')) {
            if (currentQuestionIndex < questionDivs.length - 1) {
                questionDivs[currentQuestionIndex].style.display = 'none';
                currentQuestionIndex++;
                questionDivs[currentQuestionIndex].style.display = 'block';
                updateProgressBar();
            }
        } else {
            alert('Please select an answer.');
        }
        updateButtons();
    };

    window.showPrevQuestion = function() {
        if (currentQuestionIndex > 0) {
            questionDivs[currentQuestionIndex].style.display = 'none';
            currentQuestionIndex--;
            questionDivs[currentQuestionIndex].style.display = 'block';
            updateProgressBar();
        }
        updateButtons();
    };

    function updateProgressBar() {
        let progressBar = document.getElementById('progressBar');
        let progress = (currentQuestionIndex + 1) / questionDivs.length * 100;
        progressBar.style.width = progress + '%';
        progressBar.style.backgroundColor = colors[currentQuestionIndex % colors.length + 1];
    }
    function handleRadioChange() {
        let questionDiv = questionDivs[currentQuestionIndex];
        let radioInputs = questionDiv.querySelectorAll('input[type="radio"]');
        radioInputs.forEach(function(input) {
            input.addEventListener('change', function() {
                updateButtons();
            });
        });
    }

    handleRadioChange();
    function updateButtons() {
        let questionDiv = questionDivs[currentQuestionIndex];
        questionDiv.style.backgroundColor = colors[currentQuestionIndex % colors.length];
        document.getElementById('prevBtn').style.display = currentQuestionIndex === 0 ? 'none' : 'inline';
        document.getElementById('nextBtn').style.display = currentQuestionIndex === questionDivs.length - 1 ? 'none' : 'inline';
        document.getElementById('submitBtn').style.display = currentQuestionIndex === questionDivs.length - 1 ? 'inline' : 'none';
    }

    updateButtons();
    updateProgressBar();
});

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    form = event.target;
    let submitBtn = document.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    form.submit();
});