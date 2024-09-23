import csv

# Função para criar um vCard para cada linha do CSV
def csv_para_vcard(arquivo_csv, arquivo_vcard):
    with open(arquivo_csv, mode='r', encoding='utf-8') as csvfile:
        leitor_csv = csv.DictReader(csvfile)
        with open(arquivo_vcard, mode='w', encoding='utf-8') as vcf:
            for linha in leitor_csv:
                vcf.write("BEGIN:VCARD\n")
                vcf.write("VERSION:3.0\n")
                vcf.write(f"FN:{linha['Nome']}\n")
                vcf.write(f"TEL;TYPE=CELL:{linha['Celular']}\n")
                vcf.write("END:VCARD\n\n")


csv_para_vcard('contatos.csv', 'contatos.vcf')
