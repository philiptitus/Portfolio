// Dedicated JS for portfolio detail page chatbot

document.addEventListener('DOMContentLoaded', function() {
  // Only enable on large screens
  if (window.innerWidth < 992) return;

  const chatbotBtn = document.querySelector('.chatbot-info-icon');
  const chatArea = document.getElementById('detail-chat-area');
  const chatMessages = document.getElementById('detail-chat-messages');
  const chatInput = document.getElementById('detail-chat-input');
  const chatSend = document.getElementById('detail-chat-send');

  // Helper to append messages
  function appendMessage(text, cls) {
    if (!chatMessages) return;
    const el = document.createElement('div');
    el.className = 'detail-chat-message ' + (cls || 'bot');
    el.textContent = text;
    chatMessages.appendChild(el);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // chat area is hidden by default (CSS). Keep aria-hidden=true until shown.
  if (chatArea) {
    chatArea.setAttribute('aria-hidden', 'true');
  }

  if (chatbotBtn) {
    chatbotBtn.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      // Toggle visibility: show when pressed
      if (!chatArea) return;
      const isVisible = chatArea.classList.contains('visible');
      if (isVisible) {
        chatArea.classList.remove('visible');
        chatArea.setAttribute('aria-hidden', 'true');
        return;
      }
      chatArea.classList.add('visible');
      chatArea.setAttribute('aria-hidden', 'false');
      // Show / focus chat input
      chatArea.scrollIntoView({ behavior: 'smooth', block: 'center' });
      if (chatInput) chatInput.focus();

      // set initial question and send
      const projectName = chatbotBtn.dataset.title || '';
      const question = `Tell me about the project "${projectName}".`;
      if (chatInput) chatInput.value = question;
      // send via same backend API used elsewhere
      if (chatSend) chatSend.click();
    });
  }

  // Send handler
  if (chatSend && chatInput) {
    chatSend.addEventListener('click', function(ev) {
      ev.preventDefault();
      ev.stopPropagation();
      const msg = chatInput.value || '';
      if (!msg.trim()) return;
      appendMessage(msg, 'user');
      // Show typing/loading
      const typingEl = document.getElementById('detail-chat-typing');
      if (typingEl) typingEl.style.display = 'flex';
      if (chatSend) chatSend.disabled = true;

      // Build request following homepage structure: send { question }
      const projectTitle = (chatArea && chatArea.dataset && chatArea.dataset.project) || (chatbotBtn && chatbotBtn.dataset && chatbotBtn.dataset.title) || '';
      let questionText = msg;
      if (projectTitle) {
        questionText = `Portfolio project Name: ${projectTitle}. ${msg}`;
      }
      const payload = { question: questionText };

      fetch('https://mrphilip.pythonanywhere.com/api/chatbot/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': (function getCSRFToken(){
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
          })()
        },
        body: JSON.stringify(payload)
      })
      .then(async res => {
        const data = await res.json().catch(() => ({}));
        // hide typing
        if (typingEl) typingEl.style.display = 'none';
        if (chatSend) chatSend.disabled = false;

        if (res.ok) {
          // homepage returns `answer`; accept `reply` as fallback
          const answer = data.answer || data.reply || 'No response.';
          appendMessage(answer, 'bot');
        } else {
          const errMsg = data.error || data.detail || 'Sorry, something went wrong.';
          appendMessage(errMsg, 'bot');
        }
      })
      .catch(err => {
        if (typingEl) typingEl.style.display = 'none';
        if (chatSend) chatSend.disabled = false;
        appendMessage('Error contacting server.', 'bot');
        console.error('Chat send error', err);
      });
      chatInput.value = '';
    });
  }
});
