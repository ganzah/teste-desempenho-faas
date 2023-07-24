## Teste de execução de funções na aws e digitalocean

### Orientações

- Criar conta na digitalocean
- Criar conta na aws
- Instalar ferramenta cli da digitalocean e configurá-la com token de acesso pessoal com escopo de leitura e escrita
- Criar um bucket no serviço de spaces da digitalocean
- Criar um bucket no serviço de s3 da aws
- Fazer upload do arquivo `seqdna.csv` nos buckets criados
- editar o arquivo aws-function/function.py e o arquivo digital-ocean-function/packages/teste/function/function.py preenchendo as seguintes informações com os dados relevantes da aws e da digitalocean respectivamente:
        
        aws_access_key_id
        aws_secret_access_key
        endpoint_url
        region_name
        bucket_name

- Criar namespace de função na digitalocean

        doctl serverless namespaces create --label "ppgitsc-2023" --region "sfo3"

- Realizar deploy da função na digitalocean

        doctl serverless deploy digital-ocean-function

- Criar a função na AWS usando o código disponível no arquivo aws-function/function.py (solicitar a criação de URL pública da função)
- Recuperar as URLs das funções criadas
- Executar os testes e aguardar

        ./teste_funcao <url_da_funcao>

- Remover os recursos criados nos provedores (arquivo e bucket, funções, namespaces, etc...)
