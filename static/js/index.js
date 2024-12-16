document.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loading-screen');
    const mainContent = document.getElementById('main-content');
    const commandLines = document.querySelectorAll('.command-line');
    
    // Animate command lines
    commandLines.forEach((line, index) => {
        setTimeout(() => {
            line.classList.add('active');
        }, 1000 + (index * 800));
    });

    // Update stats periodically
    let load = 0;
    const statsInterval = setInterval(() => {
        if (load < 100) {
            load += Math.random() * 20;
            if (load > 100) load = 100;
            document.querySelector('.stat-value:nth-child(2)').textContent = `${Math.round(load)}%`;
        } else {
            clearInterval(statsInterval);
            // Show enter button after loading
            setTimeout(() => {
                loadingScreen.classList.add('loaded');
                mainContent.classList.remove('hidden');
            }, 1000);
        }
    }, 500);

    // Handle navigation transitions
    document.querySelectorAll('a, button[onclick]').forEach(element => {
        element.addEventListener('click', (e) => {
            if (element.getAttribute('target') !== '_blank') {
                e.preventDefault();
                const href = element.getAttribute('href') || 
                           element.getAttribute('onclick').match(/href='([^']+)'/)?.[1];
                
                if (href) {
                    document.body.classList.add('fade-out');
                    setTimeout(() => {
                        window.location.href = href;
                    }, 500);
                }
            }
        });
    });
});

// Add smooth fade-in on page load
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
}); 