Procedural Big Data Parser

Um pipeline estruturado em **Python** focado em eficiência máxima para processar e extrair dados específicos em arquivos massivos (1 milhão+ de linhas) diretamente via terminal, sem depender de ferramentas pesadas.

Destaque de Performance
* **Tempo de execução:** `0.2290 segundos` para varrer 1 milhão de linhas.
* **Consumo de memória:** Praticamente nulo, evitando travamentos comuns em ferramentas tradicionais (como Excel ou editores de texto).
 Como funciona
Em vez de carregar todo o arquivo na memória RAM de uma só vez, o script utiliza o paradigma de **Programação Procedural** aliado ao conceito de *streaming* de dados com **Generators (`yield`)**. Isso permite ler e filtrar arquivos gigantescos linha por linha de forma instantânea.

Essa abordagem é a base de motores de processamento de dados (**ETL**), auditorias fiscais automatizadas e *parsers* de cibersegurança.

## 🛠️ Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com
   ```
2. Acesse a pasta do projeto e execute o script:
   ```bash
   cd procedural-bigdata-parser
   python script.py
   ```
