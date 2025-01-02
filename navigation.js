var currentPage = 0;
var totalPages = {{ total_pages }} + 1;
var slideTimer = null;
var timerRunning = false;

function showPage(page) {
    document.querySelectorAll('.page').forEach(function(div, index) {
        div.classList.remove('actives');
        if (index === page) {
            div.classList.add('active');
        }
    });
}

function prevPage() {
    if (currentPage > 0) {
        currentPage--;
        showPage(currentPage);
    }
}

function nextPage() {
    if (currentPage < totalPages - 1) {
        currentPage++;
        showPage(currentPage);
    }
}

function goToFirstPage() {
    currentPage = 0;
    showPage(currentPage);
}

function goToLastPage() {
    currentPage = totalPages - 1;
    showPage(currentPage);
}

function showFlashMessage(message) {
  var flashMessage = document.getElementById("flash-message");
  flashMessage.textContent = message;
  flashMessage.classList.add("show");
  setTimeout(function () {
    flashMessage.classList.remove("show");
  }, 2000); // hide message after 2 seconds
}

function startTimer() {
  if (!timerRunning) {
    slideTimer = setInterval(() => {
      if (currentPage < totalPages - 1) {
        nextPage();
      } else {
        clearInterval(slideTimer);
        timerRunning = false;
      }
    }, 10000);
    timerRunning = true;
    console.log("Timer Started!");
    showFlashMessage("Timer Running...");
  }
}

function stopTimer() {
  if (timerRunning) {
    clearInterval(slideTimer);
    timerRunning = false;
    console.log("Timer Stopped!");
    showFlashMessage("Timer Stopped!");
  }
}

document.addEventListener("keydown", function (event) {
  if (event.key === "ArrowLeft") {
    prevPage();
  } else if (event.key === "ArrowRight") {
    nextPage();
  } else if (event.key === "Home") {
    goToFirstPage();
  } else if (event.key === "End") {
    goToLastPage();
  } else if (event.key === " ") {
    if (timerRunning) {
      stopTimer();
    } else {
      startTimer();
    }
  }
});

showPage(currentPage);