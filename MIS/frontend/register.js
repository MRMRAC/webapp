document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const first_name = document.getElementById('first_name').value;
    const last_name = document.getElementById('last_name').value;
    const password = document.getElementById('password').value;
    const password_confirm = document.getElementById('password_confirm').value;

    if (password !== password_confirm) {
        document.getElementById('error').textContent = 'Пароли не совпадают';
        return;
    }

    try {
        const response = await fetch('/api/register/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, first_name, last_name, password, password_confirm })
        });
        if (response.ok) {
            alert('Регистрация успешна! Теперь войдите.');
            window.location.href = '/login.html';
        } else {
            const data = await response.json();
            document.getElementById('error').textContent = 'Ошибка: ' + JSON.stringify(data);
        }
    } catch (err) {
        document.getElementById('error').textContent = 'Ошибка соединения';
    }
});