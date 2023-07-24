#! /bin/bash

# Utilizar com ./teste_funcao <URL de invocação>

URL=$1
for c in 1 5 10 15 20
do
    echo "Executando 3000 requisições utilizando $c processo(s)..."
    time seq 1 3000 | xargs -I @ -P $c curl -s -o /dev/null --write-out '%{http_code}\n' $URL | sort -n | uniq -c
    echo 'Aguardando 4 minutos...'
    sleep 4m
done
