class SettingsManager {
    constructor() {
        this.defaultSettings = {
            confidenceThreshold: 75,
            processingSpeed: 'balanced',
            webhookUrl: '',
            enableAlerts: true,
            updateInterval: 5,
            enableCaching: true
        };
        
        this.initializeListeners();
        this.loadSettings();
    }

    initializeListeners() {
        // Confidence threshold slider
        const confidenceSlider = document.getElementById('confidenceThreshold');
        confidenceSlider.addEventListener('input', (e) => {
            e.target.nextElementSibling.textContent = `${e.target.value}%`;
        });

        // Save button
        document.querySelector('.save-button').addEventListener('click', () => this.saveSettings());
        
        // Reset button
        document.querySelector('.reset-button').addEventListener('click', () => this.resetSettings());
    }

    loadSettings() {
        const savedSettings = localStorage.getItem('orionSettings');
        const settings = savedSettings ? JSON.parse(savedSettings) : this.defaultSettings;

        document.getElementById('confidenceThreshold').value = settings.confidenceThreshold;
        document.getElementById('processingSpeed').value = settings.processingSpeed;
        document.getElementById('webhookUrl').value = settings.webhookUrl;
        document.getElementById('enableAlerts').checked = settings.enableAlerts;
        document.getElementById('updateInterval').value = settings.updateInterval;
        document.getElementById('enableCaching').checked = settings.enableCaching;
    }

    saveSettings() {
        const settings = {
            confidenceThreshold: document.getElementById('confidenceThreshold').value,
            processingSpeed: document.getElementById('processingSpeed').value,
            webhookUrl: document.getElementById('webhookUrl').value,
            enableAlerts: document.getElementById('enableAlerts').checked,
            updateInterval: document.getElementById('updateInterval').value,
            enableCaching: document.getElementById('enableCaching').checked
        };

        localStorage.setItem('orionSettings', JSON.stringify(settings));
        this.showNotification('Settings saved successfully!');
    }

    resetSettings() {
        if (confirm('Are you sure you want to reset all settings to defaults?')) {
            localStorage.removeItem('orionSettings');
            this.loadSettings();
            this.showNotification('Settings reset to defaults');
        }
    }

    showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.classList.add('fade-out');
            setTimeout(() => notification.remove(), 300);
        }, 2000);
    }
}

// Initialize settings manager
document.addEventListener('DOMContentLoaded', () => {
    window.settingsManager = new SettingsManager();
}); 