// Presentation controls for the welcome page. Account and camera APIs stay in the page.
(() => {
  const motionButton = document.getElementById('motion-toggle');
  motionButton.addEventListener('click', () => {
    const paused = document.body.classList.toggle('motion-paused');
    motionButton.setAttribute('aria-pressed', String(paused));
    document.getElementById('motion-label').textContent = paused ? 'Resume animation' : 'Pause animation';
  });

  document.querySelectorAll('[data-password-target]').forEach(button => {
    button.addEventListener('click', () => {
      const input = document.getElementById(button.dataset.passwordTarget);
      const reveal = input.type === 'password';
      input.type = reveal ? 'text' : 'password';
      button.setAttribute('aria-pressed', String(reveal));
      button.setAttribute('aria-label', reveal ? 'Hide password' : 'Show password');
    });
  });

  const cameraDetails = document.getElementById('face-check');
  cameraDetails.addEventListener('toggle', () => {
    if (cameraDetails.open) {
      setAppMode(currentAppMode);
    } else {
      stopLiteFaceLogin();
      stopEliteStressCamera();
    }
  });

  // Native forms handle required fields and Enter; the hidden view never takes focus.
  document.querySelectorAll('.modal-backdrop').forEach(modal => {
    let returnFocus = null;
    const observer = new MutationObserver(() => {
      if (modal.style.display === 'flex') {
        returnFocus = document.activeElement;
        (modal.querySelector('input, button') || modal).focus();
      } else if (returnFocus) {
        returnFocus.focus();
        returnFocus = null;
      }
    });
    observer.observe(modal, { attributes: true, attributeFilter: ['style'] });

    modal.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        if (modal.id === 'forgot-password-modal') closeForgotPasswordModal();
        else confirmStayHere();
      }
      if (event.key !== 'Tab') return;
      const controls = [...modal.querySelectorAll('input, button, a[href]')].filter(el => !el.disabled && !el.hidden);
      const first = controls[0];
      const last = controls[controls.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
  });

  window.addEventListener('pagehide', () => {
    stopLiteFaceLogin();
    stopEliteStressCamera();
    document.querySelectorAll('video').forEach(video => {
      if (video.srcObject) video.srcObject.getTracks().forEach(track => track.stop());
    });
  });
})();
