document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;

    const errorDiv = document.getElementById('error');
    errorDiv.textContent = '';

    try {
        const response = await fetch('/api/token/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('access', data.access);
            localStorage.setItem('refresh', data.refresh);
            window.location.href = '/search.html';
        } else {
            errorDiv.textContent = 'Неверные данные для входа';
        }
    } catch {
        errorDiv.textContent = 'Ошибка соединения с сервером';
    }
});