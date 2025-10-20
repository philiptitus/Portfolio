class Chatbot {
    constructor() {
        this.isOpen = false;
        this.isTyping = false;
        this.init();
    }

    init() {
        this.bindEvents();
        this.loadChatHistory();
    }

    bindEvents() {
        // Toggle chatbot
        document.getElementById('chatbot-toggle').addEventListener('click', () => {
            this.toggleChat();
        });

        // Close chatbot
        document.getElementById('chatbot-close').addEventListener('click', () => {
            this.closeChat();
        });

        // Send message
        document.getElementById('chatbot-send').addEventListener('click', () => {
            this.sendMessage();
        });

        // Enter key to send
        document.getElementById('chatbot-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            const modal = document.getElementById('chatbot-modal');
            const button = document.getElementById('chatbot-toggle');
            
            if (this.isOpen && !modal.contains(e.target) && !button.contains(e.target)) {
                this.closeChat();
            }
        });
    }

    toggleChat() {
        if (this.isOpen) {
            this.closeChat();
        } else {
            this.openChat();
        }
    }

    openChat() {
        const modal = document.getElementById('chatbot-modal');
        modal.classList.add('active');
        this.isOpen = true;
        
        // Hide Fiona button
        const fionaButton = document.querySelector('.fiona-fab');
        if (fionaButton) {
            fionaButton.style.display = 'none';
        }
        
        // Focus input
        setTimeout(() => {
            document.getElementById('chatbot-input').focus();
        }, 300);
        
        // Scroll to bottom
        this.scrollToBottom();
    }

    closeChat() {
        const modal = document.getElementById('chatbot-modal');
        modal.classList.remove('active');
        this.isOpen = false;
        
        // Show Fiona button
        const fionaButton = document.querySelector('.fiona-fab');
        if (fionaButton) {
            fionaButton.style.display = 'flex';
        }
    }

    async sendMessage() {
        const input = document.getElementById('chatbot-input');
        const message = input.value.trim();
        
        if (!message || this.isTyping) return;

        // Clear input
        input.value = '';

        // Add user message
        this.addMessage(message, 'user');

        // Show typing indicator
        this.showTyping();

        try {
            // Send to API
            const response = await fetch('https://mrphilip.pythonanywhere.com/api/chatbot/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCSRFToken()
                },
                body: JSON.stringify({ question: message })
            });

            const data = await response.json();

            // Hide typing indicator
            this.hideTyping();

            if (response.ok) {
                // Add bot response
                this.addMessage(data.answer, 'bot');
                
                // Save to history
                this.saveToHistory(message, data.answer);
            } else {
                // Show error
                this.addErrorMessage(data.error || 'Sorry, something went wrong. Please try again.');
            }
        } catch (error) {
            console.error('Chatbot error:', error);
            this.hideTyping();
            this.addErrorMessage('Sorry, I\'m having trouble connecting. Please check your internet connection and try again.');
        }
    }

    addMessage(text, sender) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;

        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        
        messageDiv.innerHTML = `
            <div class="message-content">
                <div class="message-avatar">
                    ${sender === 'bot' ? '🤖' : '👤'}
                </div>
                <div class="message-text">${this.escapeHtml(text)}</div>
            </div>
            <div class="message-time">${time}</div>
        `;

        messagesContainer.appendChild(messageDiv);
        this.scrollToBottom();
    }

    addErrorMessage(text) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const errorDiv = document.createElement('div');
        errorDiv.className = 'message bot-message';
        
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        
        errorDiv.innerHTML = `
            <div class="message-content">
                <div class="message-avatar">🤖</div>
                <div class="message-text error-message">${this.escapeHtml(text)}</div>
            </div>
            <div class="message-time">${time}</div>
        `;

        messagesContainer.appendChild(errorDiv);
        this.scrollToBottom();
    }

    showTyping() {
        this.isTyping = true;
        document.getElementById('chatbot-typing').style.display = 'flex';
        document.getElementById('chatbot-send').disabled = true;
        this.scrollToBottom();
    }

    hideTyping() {
        this.isTyping = false;
        document.getElementById('chatbot-typing').style.display = 'none';
        document.getElementById('chatbot-send').disabled = false;
    }

    scrollToBottom() {
        const messagesContainer = document.getElementById('chatbot-messages');
        setTimeout(() => {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }, 100);
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    getCSRFToken() {
        const name = 'csrftoken';
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    saveToHistory(question, answer) {
        const history = this.getChatHistory();
        history.push({
            question,
            answer,
            timestamp: new Date().toISOString()
        });
        
        // Keep only last 50 messages
        if (history.length > 50) {
            history.splice(0, history.length - 50);
        }
        
        localStorage.setItem('chatbot_history', JSON.stringify(history));
    }

    getChatHistory() {
        const history = localStorage.getItem('chatbot_history');
        return history ? JSON.parse(history) : [];
    }

    loadChatHistory() {
        const history = this.getChatHistory();
        if (history.length > 0) {
            // Show last 5 messages
            const recentHistory = history.slice(-5);
            recentHistory.forEach(item => {
                this.addMessage(item.question, 'user');
                this.addMessage(item.answer, 'bot');
            });
        }
    }

    // Public method to programmatically open chat
    open() {
        this.openChat();
    }

    // Public method to programmatically close chat
    close() {
        this.closeChat();
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.chatbot = new Chatbot();
});

// Export for global access
window.Chatbot = Chatbot; 