import base64

font_path = "fonts/FSEX300_0.ttf"

# Codificar a fonte em Base64
with open(font_path, "rb") as font_file:
    encoded_font = base64.b64encode(font_file.read()).decode('utf-8')

svg_output_path = "root_ex_machina_logo_typed.svg"

svg_content = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="300">
    <!-- Fundo do terminal -->
    <rect width="600" height="300" fill="black" rx="10" ry="10" />
    
    <!-- Cabecalho do terminal -->
    <path d="M0 10 Q0 0 10 0 H590 Q600 0 600 10 V30 H0 Z" fill="#333" />
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
    <text x="20" y="70" font-size="28">
        ~# whoami
    </text>
    <text x="20" y="110" font-size="28">
        root
    </text>
    <text x="20" y="150" font-size="28">
        ~# █
    </text>

</svg>
"""

with open(svg_output_path, 'w', encoding='utf-8') as svg_file:
    svg_file.write(svg_content)

print(f"SVG gerado com sucesso: {svg_output_path}")