# Aplicativo de Diagnóstico de Falhas em Eletroímãs

Este aplicativo é uma ferramenta de diagnóstico de falhas em eletroímãs, auxiliando na identificação e resolução de falhas comuns. Ele facilita o processo de diagnóstico e reparo, fornecendo informações detalhadas sobre causas, probabilidades e ações de mitigação.

## Funcionalidades

- **Seleção do Efeito de Falha:** Lista de efeitos de falha comuns ordenados por probabilidade decrescente.
- **Entrada de Dados de Medição:** Registro manual de valores de medição do campo magnético (até 30 medições) e cálculo automático da média.
- **Diagnóstico:** Determina se o eletroímã está bom ou ruim com base na média das medições e no efeito de falha selecionado.
- **Ações de Mitigação:** Instruções detalhadas sobre como realizar o reparo para cada ação de mitigação recomendada.

## Estrutura do Projeto

- `app.py`: Código principal do aplicativo em Flask.
- `templates/index.html`: Interface HTML para interação com o usuário.
- `static/style.css`: Estilos CSS para a interface.

## Como Executar

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/Ayrlla/analise-fmea.git
    cd analise-fmea
    ```

2. **Instale as Dependências:**
    ```bash
    pip install flask
    ```

3. **Execute o Aplicativo:**
    ```bash
    python app.py
    ```

4. **Acesse o Aplicativo:**
    Abra um navegador web e vá para `http://127.0.0.1:5000`.

## Exemplo de Uso

1. **Diagnóstico de Desimantação Lenta:**
    - Selecione "Demora na desimantação".
    - Veja as causas mais prováveis (ex: "Ressecamento do cabo elétrico").
    - Selecione a causa mais provável e obtenha instruções de reparo (ex: verificar valores de isolação dos cabos).

2. **Diagnóstico de Baixa Imantação:**
    - Selecione "Baixa imantação".
    - Veja as causas mais prováveis (ex: "Alta temperatura nos eletroímãs").
    - Selecione a causa mais provável e obtenha instruções de reparo (ex: criar plano de medição de isolamento).

## Contribuição

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas melhorias ou correções.

## Licença

Este projeto está licenciado sob a [GD License](LICENSE).


## Como Executar

1. Clone o repositório.
2. Execute python electro_magnet_diagnosis.py.
