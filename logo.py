import base64

font_path = "fonts/FSEX300_0.ttf"

# Codificar a fonte em Base64
with open(font_path, "rb") as font_file:
    encoded_font = base64.b64encode(font_file.read()).decode('utf-8')

svg_output_path = "root_ex_machina_terminal_logo.svg"

svg_content = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400">
    <!-- Fundo do terminal -->
    <rect width="400" height="400" fill="black" rx="10" ry="10" />
    
    <!-- Cabecalho do terminal -->
    <rect width="400" height="30" fill="#333" rx="10" ry="10" />
    <circle cx="20" cy="15" r="7" fill="#FF5F57" />
    <circle cx="40" cy="15" r="7" fill="#FFBD2E" />
    <circle cx="60" cy="15" r="7" fill="#28C940" />
    
    <!-- Definicao de estilo com fonte embutida -->
    <defs>
        <style type="text/css">
            @font-face {{
                font-family: "fixedsys";
                src: url(data:font/ttf;base64,{encoded_font}) format('truetype');
            }}
            text {{
                font-family: "fixedsys";
                fill: lime;
            }}
        </style>
    </defs>
    
    <!-- Texto do terminal -->
    <text x="20" y="90" font-size="64">
        ~# whoami
    </text>
    <text x="20" y="150" font-size="64">
        root
    </text>
    <text x="20" y="220" font-size="64">
        ~# █
    </text>
    
</svg>
"""

with open('root_ex_machina_logo.svg', 'w', encoding='utf-8') as svg_file:
    svg_file.write(svg_content)

print(f"SVG gerado com sucesso: {svg_output_path}")