const accessToken = localStorage.getItem('access');
alert(accessToken);
if (!accessToken) {
    window.location.href = '/login.html';
}

document.getElementById('searchBtn').addEventListener('click', loadPatients);
document.getElementById('logoutBtn').addEventListener('click', logout);

async function loadPatients() {
    const query = document.getElementById('searchQuery').value.trim();
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    try {
        const response = await fetch(`/api/users/search/?q=${encodeURIComponent(query)}`, {
            headers: {
                'Authorization': 'Bearer ' + accessToken
            }
        });

        if (!response.ok) {
            logout();
            return;
        }

        const data = await response.json();

        if (data.length === 0) {
            resultsDiv.textContent = 'Пациенты не найдены';
            return;
        }

        data.forEach(user => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <i class="fas fa-user patient-icon"></i>
                <h3>${user.first_name} ${user.last_name}</h3>
                <p><strong>Логин:</strong> ${user.username}</p>
                <p><strong>Email:</strong> ${user.email}</p>
            `;
            resultsDiv.appendChild(card);
        });
    } catch {
        resultsDiv.textContent = 'Ошибка загрузки данных';
    }
}

function logout() {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    window.location.href = '/login.html';
}