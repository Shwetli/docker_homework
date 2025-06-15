async function send() {
    const content = document.getElementById('msg').value;
    await fetch('http://localhost:5000/api/messages', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ content })
    });
    document.getElementById('msg').value = '';
    loadMessages();
}

async function loadMessages() {
    const res = await fetch('http://localhost:5000/api/messages');
    const data = await res.json();
    const table = document.getElementById('messages');
    table.innerHTML = '';
    data.forEach(([id, content]) => {
        const row = `<tr><td>${id}</td><td>${content}</td></tr>`;
        table.innerHTML += row;
    });
}

loadMessages();