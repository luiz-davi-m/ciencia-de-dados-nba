import os

# Caminho base
base_dir = "resultados"
output_html = "index.html"

# Função para gerar o HTML
def generate_html(base_dir):
    html = "<html><body>\n"
    html += "<h1>Galeria de Imagens</h1>\n"
    
    # Percorre as pastas
    for parte in sorted(os.listdir(base_dir)):
        parte_path = os.path.join(base_dir, parte)
        if os.path.isdir(parte_path):
            html += f"<h2>{parte}</h2>\n"
            graficos_path = os.path.join(parte_path, "graficos")
            
            if os.path.exists(graficos_path):
                for img_file in sorted(os.listdir(graficos_path)):
                    if img_file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                        img_path = os.path.join(graficos_path, img_file)
                        html += f'<img src="{img_path}" alt="{img_file}" style="width:200px;padding:5px;">\n'
    html += "</body></html>"
    return html

html_content = generate_html(base_dir)
with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML gerado em {output_html}")