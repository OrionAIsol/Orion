class MonitorManager {
    constructor() {
        this.activeMonitors = new Map();
        this.maxMonitors = 10;
        this.initializeEventListeners();
        this.updateStats();
    }

    initializeEventListeners() {
        document.getElementById('monitorForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.createMonitor();
        });
    }

    createMonitor() {
        if (this.activeMonitors.size >= this.maxMonitors) {
            this.showNotification('Maximum monitor limit reached', 'error');
            return;
        }

        const config = {
            minVolume: parseFloat(document.getElementById('minVolume').value),
            minMcap: parseFloat(document.getElementById('minMcap').value) || 0,
            maxMcap: parseFloat(document.getElementById('maxMcap').value) || Infinity,
            webhookUrl: document.getElementById('webhookUrl').value,
            patterns: {
                pumps: document.getElementById('detectPumps').checked,
                dumps: document.getElementById('detectDumps').checked,
                accumulation: document.getElementById('detectAccumulation').checked
            }
        };

        const monitorId = 'mon_' + Math.random().toString(36).substr(2, 9);
        this.activeMonitors.set(monitorId, config);
        
        this.createMonitorCard(monitorId, config);
        this.updateStats();
        this.showNotification('Monitor created successfully', 'success');
    }

    createMonitorCard(monitorId, config) {
        const card = document.createElement('div');
        card.className = 'monitor-card';
        card.innerHTML = `
            <div class="monitor-header">
                <h3>Monitor ${this.activeMonitors.size}</h3>
                <button class="stop-button" onclick="monitorManager.stopMonitor('${monitorId}')">
                    <i class="fas fa-stop"></i>
                </button>
            </div>
            <div class="monitor-stats">
                <div class="stat">
                    <label>Min Volume:</label>
                    <span>${config.minVolume} SOL</span>
                </div>
                <div class="stat">
                    <label>Market Cap:</label>
                    <span>${config.minMcap} - ${config.maxMcap === Infinity ? '∞' : config.maxMcap}</span>
                </div>
            </div>
            <div class="monitor-status">
                <div class="status-indicator active"></div>
                <span>Active</span>
            </div>
        `;

        document.getElementById('activeMonitors').appendChild(card);
    }

    stopMonitor(monitorId) {
        const card = document.querySelector(`[data-monitor-id="${monitorId}"]`);
        if (card) {
            card.remove();
            this.activeMonitors.delete(monitorId);
            this.updateStats();
            this.showNotification('Monitor stopped', 'success');
        }
    }

    updateStats() {
        document.getElementById('activeMonitorCount').textContent = this.activeMonitors.size;
        document.getElementById('processingSpeed').textContent = '0.001ms';
        document.getElementById('neuralLoad').textContent = 
            Math.round((this.activeMonitors.size / this.maxMonitors) * 100) + '%';
    }

    showNotification(message, type = 'success') {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
            <span>${message}</span>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.classList.add('fade-out');
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }
}

// Initialize monitor manager
const monitorManager = new MonitorManager();

// Update stats periodically
setInterval(() => {
    monitorManager.updateStats();
}, 5000); 