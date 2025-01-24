document.getElementById("extract-news-btn").addEventListener("click", async () => {
    try {
      const response = await fetch("/extract_news");
      const data = await response.json();
      const newsContainer = document.getElementById("news-container");
      newsContainer.innerHTML = "<h3>Noticias Extraídas:</h3>";
      data.news.forEach(item => {
        newsContainer.innerHTML += `<p>${item.title}</p>`; // Corregido: Uso de backticks (`) en lugar de comillas angulares (< >)
      });
    } catch (error) {
      console.error("Error al extraer noticias:", error);
    }
  });
  
  document.getElementById("generate-content-btn").addEventListener("click", async () => {
    try {
      const style = document.getElementById("content-style").value;
      const response = await fetch("/create_content", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ style: style })
      });
  
      const data = await response.json();
      const contentContainer = document.getElementById("content-container");
      contentContainer.innerHTML = `<h3>Contenido Generado:</h3><p>${data.generated_content}</p>`; // Corregido
    } catch (error) {
      console.error("Error al generar contenido:", error);
    }
  });
  
  document.getElementById("save-memory-btn").addEventListener("click", async () => {
    try {
      const response = await fetch("/save_memory", { method: "POST" });
      const data = await response.json();
      const status = document.getElementById("status");
      status.innerHTML = `<p>${data.message}</p>`; // Corregido
    } catch (error) {
      console.error("Error al guardar memoria:", error);
    }
  });
  