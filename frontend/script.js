async function fetchQuote() {
  const res = await fetch('/quote');
  const data = await res.json();
  document.getElementById('quote').innerText = `"${data.quote}"`;
  document.getElementById('author').innerText = `— ${data.author}`;
}

fetchQuote();
