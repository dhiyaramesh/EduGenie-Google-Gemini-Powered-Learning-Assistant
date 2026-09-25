document.addEventListener('DOMContentLoaded', () => {
    const taskSelector = document.getElementById('task-selector');
    const userInput = document.getElementById('user-input');
    const submitBtn = document.getElementById('submit-btn');
    const clearBtn = document.getElementById('clear-btn');
    const loadingState = document.getElementById('loading-state');
    const errorState = document.getElementById('error-state');
    const resultArea = document.getElementById('result-area');
    const resultContent = document.getElementById('result-content');
    const resultTitle = document.getElementById('result-title');
    const copyBtn = document.getElementById('copy-btn');
    const themeToggle = document.getElementById('theme-toggle');

    let currentQuizData = null;
    let currentQuestionIndex = 0;
    let quizScore = 0;

    // Theme logic
    const toggleTheme = () => {
        const isDark = document.body.getAttribute('data-theme') === 'dark';
        if (isDark) {
            document.body.removeAttribute('data-theme');
            document.getElementById('moon-icon').style.display = 'block';
            document.getElementById('sun-icon').style.display = 'none';
        } else {
            document.body.setAttribute('data-theme', 'dark');
            document.getElementById('moon-icon').style.display = 'none';
            document.getElementById('sun-icon').style.display = 'block';
        }
    };
    themeToggle.addEventListener('click', toggleTheme);
    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        toggleTheme();
    }

    // Task placeholders
    const taskConfig = {
        explain: {
            placeholder: "Enter a concept you want explained simply...",
            btnText: "Explain",
            endpoint: "/explain",
            paramName: "topic"
        },
        qa: {
            placeholder: "Ask EduGenie a question...",
            btnText: "Ask",
            endpoint: "/qa",
            paramName: "question"
        },
        quiz: {
            placeholder: "Enter a topic or paste educational text to generate a quiz...",
            btnText: "Generate Quiz",
            endpoint: "/quiz",
            paramName: "text"
        },
        summarize: {
            placeholder: "Paste the passage you want summarized...",
            btnText: "Summarize",
            endpoint: "/summarize",
            paramName: "text"
        },
        learning_path: {
            placeholder: "Enter the topic you want to learn (e.g. SQL)...",
            btnText: "Create Path",
            endpoint: "/learn/recommendations",
            paramName: "topic"
        }
    };

    taskSelector.addEventListener('change', (e) => {
        const config = taskConfig[e.target.value];
        userInput.placeholder = config.placeholder;
        submitBtn.textContent = config.btnText;
    });

    clearBtn.addEventListener('click', () => {
        userInput.value = '';
        userInput.focus();
    });

    copyBtn.addEventListener('click', () => {
        const text = resultContent.innerText;
        navigator.clipboard.writeText(text).then(() => {
            const originalTitle = copyBtn.title;
            copyBtn.title = "Copied!";
            setTimeout(() => copyBtn.title = originalTitle, 2000);
        });
    });

    submitBtn.addEventListener('click', async () => {
        const text = userInput.value.trim();
        if (!text) {
            showError("Please enter some text.");
            return;
        }

        const task = taskSelector.value;
        const config = taskConfig[task];
        
        hideError();
        showLoading();
        resultArea.style.display = 'none';
        
        try {
            const body = {};
            body[config.paramName] = text;
            
            const response = await fetch(config.endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body)
            });

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.detail || "Something went wrong.");
            }

            const data = await response.json();
            hideLoading();
            renderResult(task, data);

        } catch (err) {
            hideLoading();
            showError(err.message);
        }
    });

    function showLoading() {
        loadingState.style.display = 'flex';
        submitBtn.disabled = true;
    }

    function hideLoading() {
        loadingState.style.display = 'none';
        submitBtn.disabled = false;
    }

    function showError(msg) {
        errorState.textContent = msg;
        errorState.style.display = 'block';
    }

    function hideError() {
        errorState.style.display = 'none';
    }

    function renderResult(task, data) {
        resultArea.style.display = 'block';
        resultTitle.textContent = "Result";
        
        if (task === 'explain') {
            resultTitle.textContent = "Explanation";
            resultContent.innerHTML = marked.parse(data.explanation);
        } else if (task === 'qa') {
            resultTitle.textContent = "Answer";
            resultContent.innerHTML = marked.parse(data.answer);
        } else if (task === 'summarize') {
            resultTitle.textContent = "Summary";
            resultContent.innerHTML = marked.parse(data.summary);
        } else if (task === 'learning_path') {
            resultTitle.textContent = "Learning Path";
            resultContent.innerHTML = marked.parse(data.path);
        } else if (task === 'quiz') {
            resultTitle.textContent = "Interactive Quiz";
            currentQuizData = data.questions;
            currentQuestionIndex = 0;
            quizScore = 0;
            renderQuizQuestion();
        }
    }

    function renderQuizQuestion() {
        if (!currentQuizData || currentQuestionIndex >= currentQuizData.length) {
            // End of quiz
            resultContent.innerHTML = `
                <div class="quiz-score">
                    Quiz Complete!<br>
                    Score: ${quizScore} / ${currentQuizData.length}
                </div>
                <div style="text-align:center;">
                    <button class="btn btn-primary" onclick="location.reload()">Generate Another</button>
                </div>
            `;
            return;
        }

        const q = currentQuizData[currentQuestionIndex];
        
        let optionsHtml = '';
        q.options.forEach((opt, idx) => {
            optionsHtml += `<button class="quiz-option" data-idx="${idx}">${opt}</button>`;
        });

        resultContent.innerHTML = `
            <div class="quiz-question-container">
                <div class="quiz-question">Question ${currentQuestionIndex + 1}: ${q.question}</div>
                <div class="quiz-options" id="quiz-options">
                    ${optionsHtml}
                </div>
                <div id="quiz-feedback" class="quiz-feedback"></div>
                <button id="next-q-btn" class="btn btn-primary" style="display:none; margin-top: 1rem;">Next Question</button>
            </div>
        `;

        const optionsContainer = document.getElementById('quiz-options');
        const feedbackEl = document.getElementById('quiz-feedback');
        const nextBtn = document.getElementById('next-q-btn');

        optionsContainer.querySelectorAll('.quiz-option').forEach(btn => {
            btn.addEventListener('click', (e) => {
                // Disable all options
                optionsContainer.querySelectorAll('.quiz-option').forEach(b => b.disabled = true);
                
                const selectedText = e.target.textContent;
                const isCorrect = selectedText === q.correct_answer;
                
                if (isCorrect) {
                    e.target.classList.add('correct');
                    quizScore++;
                    feedbackEl.innerHTML = `<strong>Correct!</strong> ${q.explanation ? q.explanation : ''}`;
                    feedbackEl.style.color = 'var(--success-color)';
                } else {
                    e.target.classList.add('incorrect');
                    // Find and highlight correct answer
                    optionsContainer.querySelectorAll('.quiz-option').forEach(b => {
                        if (b.textContent === q.correct_answer) {
                            b.classList.add('correct');
                        }
                    });
                    feedbackEl.innerHTML = `<strong>Incorrect.</strong> The correct answer is: ${q.correct_answer}. <br> ${q.explanation ? q.explanation : ''}`;
                    feedbackEl.style.color = 'var(--error-color)';
                }
                
                feedbackEl.style.display = 'block';
                nextBtn.style.display = 'inline-block';
            });
        });

        nextBtn.addEventListener('click', () => {
            currentQuestionIndex++;
            renderQuizQuestion();
        });
    }
});
