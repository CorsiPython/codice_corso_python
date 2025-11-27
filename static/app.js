async function fetchProducts() {
  const limit = document.getElementById('limit').value || 10;
  try {
    const res = await fetch(`/prodotti?limite=${encodeURIComponent(limit)}`);
    const data = await res.json();
    const tbody = document.getElementById('products-body');
    tbody.innerHTML = '';
    if (!Array.isArray(data) || data.length === 0) {
      tbody.innerHTML = '<tr><td colspan="3" class="text-muted">Nessun prodotto</td></tr>';
      return;
    }
    data.forEach(p => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${escapeHtml(p.nome)}</td>
        <td>€ ${Number(p.prezzo).toFixed(2)}</td>
        <td>${p.disponibile ? 'Sì' : 'No'}</td>
      `;
      tbody.appendChild(tr);
    });
  } catch (err) {
    console.error(err);
  }
}

function escapeHtml(unsafe) {
  return unsafe
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

async function createProduct(e) {
  e.preventDefault();
  const nome = document.getElementById('nome').value.trim();
  const prezzo = parseFloat(document.getElementById('prezzo').value);
  const disponibile = document.getElementById('disponibile').checked;
  const alertDiv = document.getElementById('form-alert');
  alertDiv.innerHTML = '';

  if (!nome || Number.isNaN(prezzo)) {
    alertDiv.innerHTML = '<div class="alert alert-warning">Compila tutti i campi correttamente.</div>';
    return;
  }

  const payload = { nome, prezzo, disponibile };
  try {
    const res = await fetch('/prodotti', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (res.status === 201) {
      alertDiv.innerHTML = '<div class="alert alert-success">Prodotto creato!</div>';
      document.getElementById('product-form').reset();
      document.getElementById('disponibile').checked = true;
      fetchProducts();
    } else {
      const text = await res.text();
      alertDiv.innerHTML = `<div class="alert alert-danger">Errore: ${res.status} ${escapeHtml(text)}</div>`;
    }
  } catch (err) {
    alertDiv.innerHTML = `<div class="alert alert-danger">Errore di rete</div>`;
  }
}

document.getElementById('product-form').addEventListener('submit', createProduct);
document.getElementById('refresh').addEventListener('click', fetchProducts);
window.addEventListener('load', fetchProducts);
