import base64

font_path = "fonts/FSEX300_0.ttf"

# Codificar a fonte em Base64
with open(font_path, "rb") as font_file:
    encoded_font = base64.b64encode(font_file.read()).decode('utf-8')

svg_output_path = "root_ex_machina_logo_typing.svg"

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
    
    <!-- Cursor piscante -->
    <rect id="cursor" x="60" y="60" width="10" height="24" fill="lime">
        <animate attributeName="opacity" from="1" to="0" dur="1s" repeatCount="indefinite" />
    </rect>
    
    <!-- Texto do terminal -->
    <text x="20" y="80" fill="lime" font-size="28">
        <tspan id="line1">~# </tspan>
        <tspan id="command" />
        <tspan id="line2" x="20" dy="40" style="visibility: hidden;" />
        <tspan id="finalPrompt" x="20" dy="40" style="visibility: hidden;">~#</tspan>
    </text>
    
    <!-- Animacao -->
    <script type="application/ecmascript">
        <![CDATA[

        const command = "whoami";
        const response = "root";
        const typingSpeed = 200; // Velocidade de digitacao (ms por caractere)
        const pauseAfterCommand = 500; // Pausa apos o comando
        const pauseAfterResponse = 500; // Pausa apos a resposta
        const commandElement = document.getElementById("command");
        const line2Element = document.getElementById("line2");
        const finalPromptElement = document.getElementById("finalPrompt");
        const cursor = document.getElementById("cursor");

        let currentIndex = 0;

        function moveCursor(x, y) {{
            cursor.setAttribute("x", x);
            cursor.setAttribute("y", y);
        }}

        function typeCommand() {{
            if (currentIndex < command.length) {{
                commandElement.textContent += command[currentIndex];
                currentIndex++;
                moveCursor(20 + (commandElement.textContent.length + 3) * 14, 60); // Atualiza o cursor
                setTimeout(typeCommand, typingSpeed);
            }} else {{
                // Após o comando ser digitado, aguarde antes de mostrar a resposta
                setTimeout(showResponse, pauseAfterCommand);
            }}
        }}

        function showResponse() {{
            line2Element.textContent = response;
            line2Element.style.visibility = "visible"; // Exibe a resposta
            cursor.style.visibility = "hidden"; // Esconde o cursor durante a resposta
            setTimeout(showFinalPrompt, pauseAfterResponse);
        }}

        function showFinalPrompt() {{
            finalPromptElement.style.visibility = "visible"; // Mostra o último prompt
            moveCursor(20 + (finalPromptElement.textContent.length + 1) * 14, 140); // Move o cursor para o próximo prompt
            cursor.style.visibility = "visible"; // Mostra o cursor novamente
        }}

        // Inicia a digitacao do comando
        setTimeout(() => {{ typeCommand() }}, 1000);
        ]]>
    </script>
</svg>
"""

with open(svg_output_path, 'w', encoding='utf-8') as svg_file:
    svg_file.write(svg_content)

print(f"SVG gerado com sucesso: {svg_output_path}")