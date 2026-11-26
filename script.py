import csv
import time

# 1. FUNÇÃO GERADORA: Cria o arquivo com 1 milhão de linhas para teste
def criar_arquivo_gigante_teste(nome_arquivo):
    print("✨ Criando um arquivo gigante de teste (1 milhão de linhas)...")
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        for i in range(1, 1000001):
            if i == 500000:
                f.write(f"Linha {i}: DADO_SECRETO_ENCONTRADO\n")
            else:
                f.write(f"Linha {i}: Apenas um dado comum de preenchimento\n")
    print("✅ Arquivo de teste criado com sucesso!")

# 2. FUNÇÃO FILTRADORA (PROCEDURAL): Lê linha por linha de forma eficiente
def buscar_termo_no_arquivo(nome_arquivo, termo_busca):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        for numero_linha, linha in enumerate(f, 1):
            if termo_busca in linha:
                yield numero_linha, linha.strip()

# 3. PROCEDIMENTO PRINCIPAL (O Pipeline)
def executar_analise():
    arquivo = "meu_primeiro_big_data.txt"
    
    # Executa a criação do arquivo de teste
    criar_arquivo_gigante_teste(arquivo)
    
    # Interação com o usuário
    termo = input("\n✍️ Digite a palavra exata que quer buscar no arquivo: ")
    
    print(f"\n🔍 Iniciando busca procedural pelo termo '{termo}'...")
    inicio = time.time()
    
    encontrou_algo = False
    for linha_num, conteudo in buscar_termo_no_arquivo(arquivo, termo):
        print(f"🎯 Achou! Linha {linha_num}: {conteudo}")
        encontrou_algo = True
        
    fim = time.time()
    
    if not encontrou_algo:
        print("❌ Nenhum resultado foi encontrado com esse termo.")
        
    print(f"⏱️ Tempo total de processamento: {fim - inicio:.4f} segundos!")

# 🔥 ESTAS DUAS LINHAS ABAIXO SÃO O GATILHO QUE FAZ O PROGRAMA RODAR!
if __name__ == "__main__":
    executar_analise()
