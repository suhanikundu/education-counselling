// Countdown function
function initializeCountdown() {
    // Select all countdown elements
    const countdownElements = document.querySelectorAll('[data-countdown]');

    countdownElements.forEach(element => {
        const endDate = new Date(element.getAttribute('data-countdown')).getTime();
        
        function updateCountdown() {
            const now = new Date().getTime();
            const distance = endDate - now;

            // Calculate time components
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Update the HTML of countdown elements
            element.querySelector('[data-days]').innerText = days.toString().padStart(2, '0');
            element.querySelector('[data-hours]').innerText = hours.toString().padStart(2, '0');
            element.querySelector('[data-minuts]').innerText = minutes.toString().padStart(2, '0');
            element.querySelector('[data-seconds]').innerText = seconds.toString().padStart(2, '0');

            // If the countdown is over, display a message
            if (distance < 0) {
                clearInterval(interval);
                element.innerHTML = "Expired";
            }
        }

        // Update countdown every second
        const interval = setInterval(updateCountdown, 1000);

        // Initial call to display countdown immediately
        updateCountdown();
    });
}

// Initialize countdown on document load
document.addEventListener('DOMContentLoaded', initializeCountdown);
